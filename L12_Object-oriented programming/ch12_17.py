class Animals():
    """ Animals基底類別 """
    def __init__(self, animal_name):
        self.name = animal_name
    def which(self):
        return "My pet " + self.name.title()
    def action(self):
        return " sleeping"
        
class Dogs(Animals):
    """ Dogs是衍生類別 """
    def __init__(self, dog_name):
        super().__init__(dog_name.title())
    def action(self):
        return "running in the street"
    
class Monkeys():
    """ Monkeys是其他類別 """
    def __init__(self, monkeys_name):
        self.name = "My monkey " + monkeys_name.title()
    def which(self):
        return self.name
    def action(self):
        return "running in the forest"

def doing(obj):    # 傳入實例
    print(obj.which(), "is", obj.action())

mycat = Animals("lucy")
doing(mycat)
mydog = Dogs("gimi")
doing(mydog)
mymonkey = Monkeys("tayior")
doing(mymonkey)