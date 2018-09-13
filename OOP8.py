class A:
    x = 1

class B:
    y = 2

class C(A,B):
    z = 3

obj = C()
print("x",obj.x)
print("y",obj.y)
print("z",obj.z)
