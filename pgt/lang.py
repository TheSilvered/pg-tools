"""
lang.py

Type: module

Description: a parser for a filetype that makes it easier to implement
    various languages in the game

Classes:
    - Node (not automatically imported)
    - Lang

See the syntax of the file with help(Lang)
"""
from .stack import Stack


class Node:
    """Used by the Lang class to create connections"""
    def add_node(self, name: str, node):
        if not hasattr(self, name):
            setattr(self, name, node)

    def empty(self) -> None:
        for attr in dir(self):
            if attr[:2] == "__" or attr in ("empty", "get", "reload", "load"):
                break
            else:
                delattr(self, attr)

    def __del__(self):
        self.empty()


class Lang(Node):
    """
    Lang

    Type: Class

    Description: a type that parses and stores the data inside a file

    Args:
        'path' (str?): the path of the file to load
        'encoding' (str): the encoding to load the file with
        'log' (bool): if the errors while parsing the file should be
            logged to the console

    Methods:
        'get(attrs_str)' (str): gets a name without returning an error
            'attrs_str' (str): the sets and attribute names separated
                by points
        'load(path, encoding="utf-8", log=True)' (None): loads the
            specified files, for the arguments see the __init__
            arguments
        'reload(path, encoding="utf-8", log=True)' (None): loads a new
            file, removing the old attributes and sets
        'empty()' (None): deletes the old sets and attributes

    Lang file structure:
        a Lang file can be divided into sets that contain other sets or
        attributes, there is always a base set.

    To create a set:
    $set_name

    To create a sub_set you must add a dollar sign for every level of
    subordination
    $set_on_level_1
      $set_on_level_2_under_level_1

    To create an attribute you write:
    @attribute_name

    Any text following that line will be set as the value of the
    attribute (new lines included). To make a one-line attribute write
    @attribute_name:attribute_value

    Local References are used to set the value of an attribute to the
    value of another one in the same set. The attribute you're taking
    the value from must be already declared
    ~@new_attribute_name;other_attribute_name

    Absolute Reverences are used to set the value of an attribute to
    the value of another one declared anywhere, to access the varius
    sets use the names separated by points `.`
    .~@new_attribute;set1.set2.attribute

    Comments start with a double colon, can only be the entire line
    :: this is a comment

    The and-percent `&` is used to remove the newline character at the
    end of the line.
    @attribute1
    &This is line 1
    this is also line 1

    The value of attribute1 is 'This is line 1this is also line 1\\n'

    Spaces and tabs at the start of a line are ignored.
    To escape special characters or instructions ($, @, ~@, .~@, &, ::)
    or to keep the indent use a backslash at the start

    To specify the encoding of the file write
    %=UTF-8
    or any other encoding supported by python. This line should always
    be put before any set or attribute declaration

    @attribute2
    \\ the indent is kept

    Value attribute2: '  the indent is kept'

    To access within code the various attributes
    """
    def __init__(self, path=None, encoding="utf-8", log=True):
        if path is not None:
            self.load(path, encoding, log)

    def get(self, attrs_str: str) -> str:
        try:
            return eval(f"self.{attrs_str}")
        except Exception:
            return attrs_str

    def reload(self, *args, **kwargs) -> None:
        self.empty()
        self.load(*args, **kwargs)

    def load(self, path: str, encoding: str = "utf-8", log: bool = True) -> None:
        file = open(f"{path}", "r", encoding=encoding)
        sets = Stack()
        node_str = ""
        attr = ""
        get_text_local = None
        get_text_abs = None
        def_after_attr = None
        exec_statements = []

        for l_no, l in enumerate(file):
            for idx, char in enumerate(l):
                if char != " " or char == "\t":
                    l = l[idx:]
                    break

            if l[:2] == "::": continue

            elif l[:2] == "%=":
                if l[2:-1].lower() != encoding.lower():
                    return self.load(path, l[2:-1], log)
                continue

            elif l[:1] == "$":
                set_count = -1

                for idx, char in enumerate(l):
                    if char != "$":
                        l = l[idx:]
                        break
                    set_count += 1

                if set_count > len(sets):
                    raise SyntaxError(
                        f"line {l_no + 1} of {path}, tried to access child set"
                        f" of level {set_count + 1} with no parent"
                    )

                while len(sets) > set_count:
                    sets.pop()

                if l[:-1] != "!":
                    node_str = ".".join(reversed([i for i in sets]))
                    if node_str: node_str += "."
                    exec_statements.append(
                        f"self.{node_str}add_node('{l[:-1]}', Node())"
                    )
                    self.add_node(l[:-1], Node())
                    sets.push(l[:-1])

                node_str = ".".join(reversed([i for i in sets])) + "."
                continue

            elif l[:1] == "@":
                has_value = l[1:-1].find(":") + 1
                if not has_value:
                    attr = l[1:-1]
                    continue
                else:
                    attr = l[1:has_value]
                    def_after_attr = l[has_value + 1:]
                    if len(def_after_attr) > 0 and def_after_attr[-1] == "\n":
                        def_after_attr = def_after_attr[:-1]

            elif l[:3] == ".~@":
                if l[-1] == "\n": l = l[:-1]
                vals = l[3:].split(";")
                if len(vals) != 2:
                    raise SyntaxError(
                        f"line {l_no + 1} of {path}, invalid syntax"
                    )
                attr, get_text_local = vals

            elif l[:2] == "~@":
                if l[-1] == "\n": l = l[:-1]
                vals = l[2:].split(";")
                if len(vals) != 2:
                    raise SyntaxError(
                        f"line {l_no + 1} of {path}, invalid syntax"
                    )
                attr, get_text_abs = vals

            elif l[:1] == "&":
                l = l[1:-1]

            elif l[:1] == "\\":
                l = l[1:]

            else:
                l = l[:-1] + "\\n"

            l = l.replace("'", "\\'").replace('"', '\\"')

            if get_text_local is not None:
                exec_statements.append(f"self.{node_str}{attr} = "
                               f"self.{node_str}{get_text_local}")
                get_text_local = None

            elif get_text_abs is not None:
                exec_statements.append(f"self.{node_str}{attr} = "
                                       f"self.{get_text_abs}")
                get_text_abs = None

            elif def_after_attr is not None:
                exec_statements.append(f"self.{node_str}{attr} = "
                                       f"'{def_after_attr}'")
                def_after_attr = None

            else:
                exec_statements.append(
                    f"try:\n"
                    f"    self.{node_str}{attr} += '{l}'\n"
                    f"except AttributeError:\n"
                    f"    self.{node_str}{attr} = '{l}'"
                )

        exec("\n".join(exec_statements))

        file.close()
