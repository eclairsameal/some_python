class Grandfather():
    def ation1(self):
        print("Grandfather")

class Father(Grandfather):
    def ation3(self):      # 定義ation3
        print("Father")
        
class Uncle(Grandfather):
    def ation2(self):      # 定義ation3
        print("Uncle")

class Ivan(Father, Uncle):
    def ation4(self):
        print("Ivan")

ivan = Ivan()
ivan.ation4()    # Ivan
ivan.ation3()    # Ivan -> Father
ivan.ation2()    # Ivan -> Father -> Uncle
ivan.ation1()    # Ivan -> Father -> Uncle -> Grandfather