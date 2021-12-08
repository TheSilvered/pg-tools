from .stack import Stack


class Node:
    def add_node(self, name, node):
        if not hasattr(self, name):
            setattr(self, name, node)

    def empty(self):
        for attr in dir(self):
            if attr[:3] == "__" or attr in ("empty", "get", "reload", "load"):
                break
            else:
                delattr(self, attr)


class Lang(Node):
    def get(self, attrs):
        try:
            return eval(f"self.{attrs}")
        except Exception:
            return attrs

    def reload(self, *args, **kwargs):
        self.empty()
        self.load(*args, **kwargs)

    def load(self, path, encoding="utf-8", log=True):
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
                if char != " ":
                    l = l[idx:]
                    break

            l = l.replace("'", "\\'").replace('"', '\\"')

            if l[:2] == "::": continue

            elif l[:2] == "!=":
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
                vals = l[3:].split(";")
                if len(vals) != 2:
                    raise SyntaxError(
                        f"line {l_no + 1} of {path}, invalid syntax"
                    )
                attr, get_text_abs = vals

            elif l[:1] == "&":
                l = l[1:-1]

            else:
                l = l[:-1] + "\\n"

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
