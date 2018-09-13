class Employee:
    #初始化設定員工的姓名
    def __init__(self,name):
        self.__name = name

    #回傳員工姓名
    def getName(self):
        return self.__name

    def getSalary(self,hours,payrate):
        return hours * payrate

class SalesPerson(Employee):
    def getSalary(self,hours,payrate,bonus):
        return hours * payrate+bonus

E1 = Employee("Frank")
E2 = SalesPerson("Kevin")
print("employee",E1.getName(),"Salary",E1.getSalary(120,150))
print("Saleman",E2.getName(),"Salary",E2.getSalary(120,150,3000))
