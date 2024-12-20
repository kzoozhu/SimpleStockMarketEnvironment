
class tradingEnvironment:
    balance = 0
    position = False
    longOrShort = ""
    quanity = 0
    initalBalance = 0
    def __init__(self, balance):
        self.balance = balance
        self.initalBalance = balance
    def buy(self, priceEntered, quanity):
        if self.position == False:
            self.position = True
            self.longOrShort = "Long"
            self.entryPrice = priceEntered
            self.quanity = quanity
            self.balance = self.balance - (self.entryPrice * self.quanity)
            return "Success"
        else:
            return "Currently In Trade"

    def sell(self, priceEntered, quanity):
        if self.position == False:
            self.position  = True
            self.longOrShort = "Short"
            self.entryPrice = priceEntered
            self.quanity = quanity
            self.balance = self.balance - (self.entryPrice * self.quanity)
            return "Success"
        else:
            return "Currently In Trade"

    def currentPLOfPosition(self,currentStockValue):
        if self.position:
            if self.longOrShort == "Long":
                return (currentStockValue*self.quanity) - (self.entryPrice * self.quanity)
            elif self.longOrShort == "Short":
                return (self.entryPrice * self.quanity) - (currentStockValue*self.quanity)
        else:
            return None

    def closePosition(self, currentStockValue):
        if self.position:
            self.position = False
            if self.longOrShort == "Long":
                self.balance += (currentStockValue) * self.quanity
            elif self.longOrShort == "Short":
                self.balance += (self.entryPrice * self.quanity) - (currentStockValue*self.quanity) + (self.entryPrice*self.quanity)

    def getBalance(self):
        return self.balance

    def getInitalBalace(self):
        return self.initalBalance
    
    def getPostion(self):
        return self.position
