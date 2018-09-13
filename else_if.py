scrore = eval(input("請輸入0~100的分數"))

if scrore >=90:
    print("優等")
elif scrore <90 and scrore >=80:
    print("甲等")
elif scrore <80 and scrore >=70:
    print("乙等")
elif scrore <70 and scrore >=60:
    print("丙等")
else:
    print("不及格")
