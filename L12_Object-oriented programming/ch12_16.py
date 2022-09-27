class Father():
    def __init__(self):
        self.father_money = 10000

class Ira(Father):
    def __init__(self):
        self.ira_money = 8000
        super().__init__()     # 將父類別屬性複製
        
class Ivan(Father):
    def __init__(self):
        self.ivan_money = 3000
        super().__init__()     # 將父類別屬性複製
    
    def get_money(self):
        print("Ivan資產:{}".format(self.ivan_money))
        print("Father(資產:{}".format(self.father_money))
        print("Ira資產:{}".format(Ira().ira_money))    #  取得兄弟類別的屬性
        
ivan = Ivan()
ivan.get_money()