class Banks():
    """ 定義Banks類別 """
    def __init__(self, uname):    # 初始化方法
        self.__name = uname              # 設定存款者姓名
        self.__balance = 0               # 設定所存的錢
        self.__bankname = "Taipei Bank"  
        self.__rate = 30                 # 預設美金與台幣換匯比率 
        self.__service_charge = 0.01     # 換匯的服務費

    def save_money(self, money):         # 設定存款
        self.__balance += money
        print("存款 {} 完成".format(money))
      
    def withdraw_money(self, money):     # 設定提款
        self.__balance -= money
        print("提款 {} 完成".format(money))   
      
    def get_balance(self):              # 獲得存款餘額
        print("{} 目前餘額: {}".format(self.__name.title(), self.__balance))

    def usa_to_taiwan(self, usa_d):     # 美金兌換台幣的方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):        # 計算換匯(私有變數)
        return int(usa_d * self.__rate * (1 - self.__service_charge))
      
maxbank = Banks("max")
print("{} 美金可以兌換 {} 台幣".format(50, maxbank.usa_to_taiwan(50)))