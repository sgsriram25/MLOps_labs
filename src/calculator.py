# calculator.py

def fun1(x, y):
    """Return the sum of x and y"""
    return x + y

def fun2(x, y):
    """Return x minus y"""
    return x - y

def fun3(x, y):
    """Return x multiplied by y"""
    return x * y

def fun4(x, y):
    """Return the sum of fun1, fun2, fun3"""
    return fun1(x, y) + fun2(x, y) + fun3(x, y)


# from calculator import fun1, fun2, fun3, fun4

# print(fun1(2,3))  # 5
# print(fun2(5,2))  # 3
# print(fun3(3,4))  # 12
# print(fun4(2,3))  # 5+(-1)+6=10
