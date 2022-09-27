# Grandfather -> Father -> Ivan
class Grandfather():
    def __init__(self):
        self.grandfather_money = 10000
    def get_info1(self):
        print("Grandfather Information")

class Father(Grandfather):
    def __init__(self):
        self.father_money = 8000
        super().__init__()
    def get_info2(self):
        print("Father Information")
        
class Ivan(Father):
    def __init__(self):
        self.ivan_money = 3000
        super().__init__()
    def get_info3(self):
        print("Grandfather Information")
    def get_money(self):
        print("Ivan資產:{}".format(self.ivan_money))
        print("Father(資產:{}".format(self.father_money))
        print("Grandfather資產:{}".format(self.grandfather_money))

ivan = Ivan()
ivan.get_info3()
ivan.get_info2()
ivan.get_info1()
ivan.get_money()