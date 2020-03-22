#  Authors: Sylvain Marie <sylvain.marie@se.com>
#
#  Copyright (c) Schneider Electric Industries, 2020. All right reserved.
from textwrap import dedent

from makefun import compile_fun


def test_compilefun():

    @compile_fun
    def foo(a, b):
        return a + b

    assert foo(5, -5.0) == 0

    ref = """
    @compile_fun
    def foo(a, b):
        return a + b
        """
    assert foo.__source__ == dedent(ref[1:])


def test_compilefun_nested():

    def foo(a, b):
        return a + b

    @compile_fun
    def bar(a, b):
        return foo(a, b)

    assert bar(5, -5.0) == 0

# def test_compileclass_decorator():
#
#     @compile_fun
#     class A(object):
#         pass
#
#     assert A() is not None
#
#     @compile_fun
#     class A(int, object):
#         pass
#
#     assert A() is not None
#
#     @compile_fun
#     class A(object):
#         def __init__(self):
#             pass
#
#     assert A() is not None
#
#     @compile_fun
#     class A(int):
#         pass
#         # def compute(self):
#         #     return self + 2
#
#     assert A(2) + 2 == 4
