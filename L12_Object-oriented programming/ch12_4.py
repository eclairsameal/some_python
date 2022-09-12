class Banks():
    """ 定義Banks類別 """
    bankname = "Taipei Bank"
    def __init__(self, uname, money):    # 初始化方法
        self.name = uname                # 設定存款者姓名
        self.balance = money             # 設定所存的錢

    def save_money(self, money):         # 設定存款
        self.balance += money
        print("存款 {} 完成".format(money))
      
    def withdraw_money(self, money):     # 設定提款
        self.balance -= money
        print("提款 {} 完成".format(money))   
      
    def get_balance(self):              # 獲得存款餘額
        print("{} 目前餘額: {}".format(self.name.title(), self.balance))

maxbank = Banks("max", 100)
maxbank.get_balance()
maxbank.save_money(300)
maxbank.get_balance()
maxbank.withdraw_money(200)
maxbank.get_balance()