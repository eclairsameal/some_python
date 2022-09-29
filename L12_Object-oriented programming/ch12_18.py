class Grandfather():
    def ation1(self):
        print("Grandfather")

class Father(Grandfather):
    def ation2(self):
        print("Father")
        
class Uncle(Grandfather):
    def ation2(self):
        print("Uncle")

class Ivan(Father, Uncle):
    def ation3(self):
        print("Ivan")

ivan = Ivan()
ivan.ation3()
ivan.ation2()
ivan.ation1()