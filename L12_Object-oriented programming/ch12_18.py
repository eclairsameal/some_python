class Grandfather():
    def ation1(self):
        print("Grandfather")

class Father(Grandfather):
    def ation2(self):      # 定義ation2
        print("Father")
        
class Uncle(Grandfather):
    def ation2(self):      # 定義ation2
        print("Uncle")

class Ivan(Father, Uncle):
    def ation3(self):
        print("Ivan")

ivan = Ivan()
ivan.ation3()    # Ivan
ivan.ation2()    # Ivan -> Father
ivan.ation1()    # Ivan -> Father -> Grandfather