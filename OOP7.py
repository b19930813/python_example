class A:
    x = 1

class B(A):
    y = 2

class C(B):
    z=3

obj = C()
print("X:",obj.x)
print("Y:",obj.y)
print("Z:",obj.z)
