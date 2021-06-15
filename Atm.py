class Atm:
    def __init__(self, atmcardno, pin, money):
        self.atmcardno = atmcardno
        self.pin = pin
        self.money = money
    
    def PutAtmCardNo(self, atmcardno):
        print("put in atm card no")
        print(self.atmcardno)
    
    def PutPin(self,pin):
        print("put in pin")
        print(self.pin)

    def BalanceEnquiry(self, money):
        print("you have this much money left in your account")
        print(self.money)


Marinette = Atm(43111033030, 820292, "$5000")
Adrien = Atm(78129304568, 783004, "$7000")

Marinette.PutAtmCardNo("")
Marinette.PutPin("")
Marinette.BalanceEnquiry("")
Adrien.PutAtmCardNo("")
Adrien.PutPin("")
Adrien.BalanceEnquiry("")

