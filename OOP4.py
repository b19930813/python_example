class Circle:
    PI = 3.14
    #初始設定
    #初始化之後再以self(這是預設的不得更改)自訂屬性
    def __init__(self,r=1):
        self.__radius = r  #前面__表示為private

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return self.PI * self.__radius * self.__radius
C1=Circle(10)
    
print("半徑為",C1.getRadius())
print("的圓面積",C1.getArea())

