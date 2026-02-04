import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5
    assert fun1(-1, 1) == 0
    assert fun1(0, 0) == 0

def test_fun2():
    assert fun2(5, 3) == 2
    assert fun2(3, 5) == -2
    assert fun2(0, 0) == 0

def test_fun3():
    assert fun3(2, 3) == 6
    assert fun3(-1, 5) == -5
    assert fun3(0, 100) == 0

def test_fun4():
    # fun4 = fun1 + fun2 + fun3
    assert fun4(2, 3) == fun1(2, 3) + fun2(2, 3) + fun3(2, 3)
    assert fun4(-1, 1) == fun1(-1, 1) + fun2(-1, 1) + fun3(-1, 1)

