def f(x,y,z,a = 3,b = 8):
    return x + (y + z) + a * b
'''
Return x + (y + z) + a * b
:param x: int.
:param y: int.
:param z: int.
:param a: int. initial value 3.
;param b: int. initial value 8.
:return: int sum of y and z. next, int product of a and b. next, int sum of x and (sum of)yz. next, int sum of (sum of)xyz and (product of)ab.
'''

print(f(4,1,2))
