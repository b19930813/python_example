def divmod(x,y):
    div = x//y
    mod = x% y
    return div,mod

a,b = divmod(100,7)
print("a=",a,"b=",b)
