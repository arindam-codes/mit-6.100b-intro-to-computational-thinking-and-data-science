
class StockTicker():
    
    def __init__(self, name, price, expectedReturn):
        self.name = name
        self.price = price
        self.expectedReturn = expectedReturn
        
    def get_name(self):
        return self.name
        
    def get_price(self):
        return self.price
    
    def get_expectedReturn(self):
        return self.expectedReturn
    

def stockmodeller(names, prices, expectedReturns):
    
    totalStock = []
    for i in range(len(names)):
        stock = StockTicker(names[i], prices[i], expectedReturns[i])
        totalStock.append(stock)
    
    return totalStock
        
def greedy(stocks, budget, keyFunction):
    
    stockItems = sorted(stocks, key = keyFunction, reverse=True)
    profitableStocks = []
    investment = 0
    
    for stock in stockItems:
        if stock.get_price() + investment <= budget:
            profitableStocks.append(stock)
            investment += stock.get_price()
            
    return profitableStocks


def stockPredicter(stocks, budget):
    
    def stockPrinter(probablestocks):
        for stock in probablestocks:
            print(f"Stock: {stock.get_name()} - returns {stock.get_expectedReturn()}")
        print("\n")
        
    # returns by expected return
    r_probablestocks = greedy(stocks, budget, lambda stock: stock.get_expectedReturn())
    stockPrinter(r_probablestocks)
    
    # returns by price (cost)
    c_probablestocks = greedy(stocks, budget, lambda stock: 1 / stock.get_price())
    stockPrinter(c_probablestocks)
    
    # returns by return per dollar 
    rpd_probablestocks = greedy(stocks, budget, lambda stock: stock.get_expectedReturn() / stock.get_price())
    stockPrinter(rpd_probablestocks)
    

stocks = [
    ("AAPL", 175, 15),
    ("GOOG", 140, 12),
    ("MSFT", 330, 28),
    ("AMZN", 145, 11),
    ("TSLA", 200, 18),
    ("META", 320, 25),
    ("NFLX", 500, 40),
    ("NVDA", 800, 70)
]

names = [stock[0] for stock in stocks]
prices = [stock[1] for stock in stocks]
expectedReturns = [stock[2] for stock in stocks]

stock = stockmodeller(names, prices, expectedReturns)

stockPredicter(stock, 1000)    
