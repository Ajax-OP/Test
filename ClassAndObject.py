class wappnet:

    def __init__(self,name):
        self.name = name

    def ceo(self):
        pass

    def cto(self):
        pass

    def hr(self):
        pass

    def employe(self,empid,wday):
        self.empid = empid
        self.wday = wday
        pdsal = 500
        sal = pdsal*wday
        return sal
        #return print(f"{self.name} salary is {sal}")

name = input("Enter your name : ")
emp1 = wappnet(name)

empid = int(input(f"Hey {name}, Enter your empid : "))
wday = int(input(f"Hey {name}, Enter your wday : "))

a = emp1.employe(empid,wday)
print(a)




