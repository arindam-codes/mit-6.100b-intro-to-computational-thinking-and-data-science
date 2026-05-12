class Trade:
    
    def __init__(self, name, expProfit, reqCap, rs):
        self.name = name
        self.expProfit = expProfit
        self.reqCap = reqCap
        self.rs = rs
    
    def getName(self):
        return self.name
    
    
    def getProfit(self):
        return self.expProfit
    
    def getCapital(self):
        return self.reqCap
    
    def getRisk(self):
        return self.rs
    
    def density(self):
        return self.getProfit() / self.getCapital() 
    

names = ["BANKNIFTY scalp", "Reliance breakout", "BTC momentum", "Infosys swing", 
         "Gold ETF move", "Smallcap gamble", "Mean reversion pair trade", "Options theta decay"]
expProfits = [9000, 5000, 12000, 4000, 3000, 15000, 6500, 7000]
reqCaps = [40000, 20000, 60000, 15000, 10000, 70000, 25000, 30000]
rs = [8, 3, 9, 2, 1, 10, 4, 5]
    
def trademodeler(names, expProfits, reqCaps, rs):
    trades = []
    for i in range(len(names)):
        trade = Trade(names[i], expProfits[i], reqCaps[i], rs[i])
        trades.append(trade)
        
    return trades

trades = trademodeler(names, expProfits, reqCaps, rs)

    ## strategy A - Profit Greedy
highestExpProfitTrades = sorted(trades, key=lambda x : x.getProfit(), reverse=True)

    ## strategy B - Cheap Capital Greedy
cheapTrades = sorted(trades, key=lambda x : 1 / x.getCapital(), reverse=True)

    ## strategy C - Profit Efficiency Greedy
densityTrades = sorted(trades, key=lambda x : x.density(), reverse = True)

    ## strategy D - Risk-adjusted Profit Efficiency Greedy
rsDensityTrades = sorted(trades, key=lambda x : x.getProfit() / (x.getCapital() * x.getRisk()), reverse=True)

def Greedy(lst):
    
    fineTrades = []
    capitalUsed = 0
    rscore = 0
    totalProfit = 0
    
    for eachTrade in lst:
        if eachTrade.getCapital() + capitalUsed <= 100000 and eachTrade.getRisk() + rscore <= 15:
            fineTrades.append(eachTrade)
            capitalUsed += eachTrade.getCapital()
            rscore += eachTrade.getRisk()
            totalProfit += eachTrade.getProfit()
    
    return fineTrades, capitalUsed, rscore, totalProfit

def optimisedTrades(lst):
    fineTrades, capitalUsed, rscore, totalProfit = Greedy(lst)
    for trade in fineTrades:
        print(f"{trade.getName()} expected {trade.getProfit()} | needs {trade.getCapital()} | {trade.getRisk()} rs")
    print(f"Total Profit = {totalProfit}\nTotal Capital = {capitalUsed}\nToal risk = {rscore}\n")
        
print("Highest Profits first")
optimisedTrades(highestExpProfitTrades)

print("Cheapest Capital Needed")
optimisedTrades(cheapTrades)

print("Highest Expected Profit per Capital")
optimisedTrades(densityTrades)

print("Risk-adjusted Expected Profit Efficient Greedy")
optimisedTrades(rsDensityTrades)

