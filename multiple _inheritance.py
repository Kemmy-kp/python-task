#=============inheritance===========

class parent1:
    def displayp1(self):
        print("this is parent class")
class parent2:
    def displayp2(self):
        print("this is parent class")
class Child(parent1,parent2):
    def displayC(self):
        print("print is child class")

o2=Child()
o2.displayC()
o2.displayp1()
o2.displayp2()
