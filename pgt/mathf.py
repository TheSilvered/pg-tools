"""
pgt.mathf

Type: module

Easing functions taken and adapted from https://easings.net/

Every easing function takes one argument (x) that is a floating point
value between 0 (start of the animation) and 1 (end of the animation)
and returns a value between 0 and 1 (elastic and back functions can
return a value bigger than 1 or smaller than 0)

Easing functions:
    e_in_sin,     e_out_sin,     e_in_out_sin
    e_in_quad,    e_out_quad,    e_in_out_quad
    e_in_cubic,   e_out_cubic,   e_in_out_cubic
    e_in_quart,   e_out_quart,   e_in_out_quart
    e_in_quint,   e_out_quint,   e_in_out_quint
    e_in_exp,     e_out_exp,     e_in_out_exp
    e_in_circ,    e_out_circ,    e_in_out_circ
    e_in_back,    e_out_back,    e_in_out_back
    e_in_elastic, e_out_elastic, e_in_out_elastic
    e_in_bounce,  e_out_bounce,  e_in_out_bounce

Additional functions:
    clamp(value, min_, max_): keeps value between min_ and max_
    get_i(c1, c2): returns the hypotenuse given the two catheti
    get_c(i, c): returns a cathetus given the hypotenuse and the other
                 cathetus
    distance(p1, p2): returns the distance between 2 points (can return
                      negative values)
    abs_distance(p1, p2): returns the absolute distance between two
                          points
"""

from math import sqrt, pi, sin, cos

clamp = lambda value, min_, max_: min(max(value, min_), max_)

get_i = lambda c1, c2: sqrt(c1*c1 + c2*c2)
get_c = lambda i, c: sqrt(i*i - c*c)

distance = lambda p1, p2: get_i(*(p2 - p1).list())
abs_distance = lambda p1, p2: abs(distance(p1, p2))

sign = lambda x: -1 if x < 0 else 1

############################### Easing functions ###############################
e_in_sin = lambda x: 1 - cos((x * pi) / 2)
e_out_sin = lambda x: sin((x * pi) / 2)
e_in_out_sin = lambda x: -(cos(pi * x) - 1) / 2

e_in_quad = lambda x: x * x
e_out_quad = lambda x: 1 - (1 - x) * (1 - x)
e_in_out_quad = lambda x: 2 * x**2 if x < .5 else 1 - (-2 * x + 2)**2 / 2

e_in_cubic = lambda x: x ** 3
e_out_cubic = lambda x: 1 - (1 - x)**3
e_in_out_cubic = lambda x: 4 * x**3 if x < .5 else 1 - (-2 * x + 2)**3 / 2

e_in_quart = lambda x: x ** 4
e_out_quart = lambda x: 1 - (1 - x)**4
e_in_out_quart = lambda x: 8 * x**4 if x < .5 else 1 - (-2 * x + 2)**4 / 2

e_in_quint = lambda x: x ** 5
e_out_quint = lambda x: 1 - (1 - x)**5
e_in_out_quint = lambda x: 16 * x**5 if x < .5 else 1 - (-2 * x + 2)**5 / 2

e_in_exp = lambda x: 0 if x == 0 else 2 ** (10 * (x - 1))
e_out_exp = lambda x: 1 if x == 1 else 1 - 2 ** (-10 * x)
e_in_out_exp = lambda x: e_in_exp(x * 2) / 2 if x < .5 else \
                         e_out_exp(x * 2 - 1) / 2 + .5

e_in_circ = lambda x: 1 - sqrt(1 - x ** 2)
e_out_circ = lambda x: sqrt(1 - (x - 1)**2)
e_in_out_circ = lambda x: e_in_circ(x * 2) / 2 if x < .5 else\
                          e_out_circ(x * 2 - 1) / 2 + .5

e_in_back = lambda x: 2.70158 * x**3 - 1.70158 * x**2
e_out_back = lambda x: 1 + 2.70158 * (x - 1)**3 + 1.70158 * (x - 1)**2
e_in_out_back = lambda x: e_in_back(x * 2) / 2 if x < .5 else\
                          e_out_back(x * 2 - 1) / 2 + .5


def e_in_elastic(x: float) -> float:
    if x in (0, 1): return x
    return -2 ** (10 * x - 10) * sin((x * 10 - 10.75) * 2.09439)


def e_out_elastic(x: float) -> float:
    if x in (0, 1): return x
    return 2**(-10 * x) * sin((x * 10 - 0.75) * 2.09439) + 1


e_in_out_elastic = lambda x: e_in_elastic(x * 2) / 2 if x < .5 else\
                             e_out_elastic(x * 2 - 1) / 2 + .5


def e_out_bounce(x: float) -> float:
    if x < 4 / 11:
        return 121 * x * x / 16
    elif x < 8 / 11:
        return (363 / 40 * x * x) - (99 / 10 * x) + 17 / 5
    elif x < 9 / 10:
        return (4356 / 361 * x * x) - (35442 / 1805 * x) + 16061 / 1805
    return (54 / 5 * x * x) - (513 / 25 * x) + 268 / 25


e_in_bounce = lambda x: 1 - e_out_bounce(1 - x)
e_in_out_bounce = lambda x: (1 - e_out_bounce(1 - 2 * x)) / 2 if x < .5 else \
                            (1 + e_out_bounce(2 * x - 1)) / 2
