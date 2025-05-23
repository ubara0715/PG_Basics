'''
Returns float x
:param x: string.
:return: xを文字列からfloat型に変える
'''
def f(x):
    try:
        x = float(x)
        return x
    except ZeroDivisionError:
        print("b cannot be zero.")

print(f(0.04))
