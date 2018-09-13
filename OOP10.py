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
     def __init__(self,name,bonus):
              super().__init__(name)
              self.__bonus = bonus


     def getSalary(self,hours,payrate):
         return super().getSalary(hours,payrate) + self.__bonus

  

E1 = Employee("Frank")
E2 = SalesPerson("Kevin",3000)
print("employee",E1.getName(),"Salary",E1.getSalary(120,150))
print("Saleman",E2.getName(),"Salary",E2.getSalary(120,150))
