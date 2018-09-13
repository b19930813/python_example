#guess number
import random

num = random.randint(1,3)
answer = eval(input("請輸入一個數字"))
print(num,"==",answer,"is",num==answer)
