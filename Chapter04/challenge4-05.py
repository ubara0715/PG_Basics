def f(x):
    try:
        x = float(x)
        return x
    except ZeroDivisionError:
        print("b cannot be zero.")
'''
Returns float x
:param x: string.
:return: xを文字列からfloat型に変える
'''

print(f(0.04))
