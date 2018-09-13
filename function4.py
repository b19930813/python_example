def add(*numbers):
    total = 0
    for i in numbers:
        total = total +i
    return total

print(add(1))
print(add(5,2))
print(add(5,2,5))
