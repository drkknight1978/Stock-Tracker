#dependencies here :-
from datetime import datetime
import string
import json
from os import path
from time import sleep

'''#defs here:-
def loadportfolio(inPortfolio, fName):
    if path.exists(fName):
        mode = 'r'
        with open (fName, mode) as f:
            count = 0
            for l in f.readlines():
                if count == 0: #where we grab portfolio name.
                    Account = portfolio(str(l))
                else:
                    stockData = l.split(',')
                    desc = stockData [0]
                    price = float(stockData [1])
                    amount = float(stockData[2])
                    buytime = stockData[3] #datetime.strptime(stockData[3],'%Y-%m-%d')
                    Account.addStock(desc, price, amount, buytime)
                count += 1
    else:
        print ('File not found!')
    return (Account)'''

#Class code here :-
class portfolio():
    '''portfolio holds  stock portfolio.  it also provides functions for searching and displaying the stock
    as required'''
    def __init__(self, title = None):
        ''' init of portfolio at the moment (27-02-2020) it only holds a name
         further development...'''
        super().__init__()
        self.title = title
        self.stocks = []
        #self.addStock()
    
    def addStock(self, desc = 'cash', price = 1, amount = 0, buytime ='now'):
        '''adds a new stock.  if no stock is given zero cash is added (with warning).  Also, the 'cash' stock
        adds cash to the cash on account'''
        if self.existStock(desc) and desc == 'cash': #and self.title == None:
            self.stocks[0].amount += amount
        else:
            self.stocks.append(stock(desc, price, amount, buytime))
        '''highlight when something doesn't seem quite right'''    
        if (desc == 'cash') and (amount == 0):
            rtCode = 1
            print('note, no entry added')
        else:
            rtCode = 0
        return (rtCode)
    
    def existStock(self, desc):
        ''' check if a stock is already in the portfolio'''
        for stock in self.stocks:
            if stock.desc == desc:
                return (True)
        return(False)

    def searchStock():
        '''a searching methodology ideally use it to search for names and
        parts of names'''
        pass
    
    def printStocks(self):
        '''print a summary of all stocks'''
        for stock in self.stocks:
            print ('Name :- {}, Price:- {}, Amount:-{}, Value:- £{} brought on {}'.format(stock.desc, stock.price, \
                 stock.amount, stock.amount * stock.price / 100, stock.buytime))
    
    def savePortfolio(self, fName, port):
        '''Saves file in a propietry format (LOL) but scope to save as CSV 
        in the future and integrate with GUI'''
        if path.exists(fName) == True:
            OW = input('--------File Exists, overwrite with current data (Y/N)?').lower()
            if OW == 'y':
                print ('Overwriting file...')
                #mode = 'w+'
            elif OW == 'n':
                print ('Nothing saved...')
                return (0)
            else:
                print ('bullshit response...')
                return 0
        dataStr = str(port.title) #not sure if str is required
        f = open(fName, 'w+')
        with open (fName, 'w+') as f:
            for stock in port.stocks:
                if stock == dataStr:
                    pass
                else:
                    dataStr = (dataStr + str(stock.desc) + ',' \
                        + str(stock.price) + ','\
                        + str(stock.amount) + ','\
                            + datetime.strftime(stock.buytime,'%Y-%m-%d') + ',\n')
                    f.write(dataStr)
                    dataStr = ''


    @staticmethod
    def loadPortfolio(fName):
        ''' loads a portfolio'''
        if path.exists(fName):
            mode = 'r'
            with open (fName, mode) as f:
                for count, l in enumerate(f.readlines()):
                    if count == 0: #where we grab portfolio name.
                        Account = portfolio(str(l))
                    else:
                        stockData = l.split(',')
                        desc = stockData [0]
                        price = float(stockData [1])
                        amount = float(stockData[2])
                        buytime = stockData[3] #datetime.strptime(stockData[3],'%Y-%m-%d')
                        Account.addStock(desc, price, amount, buytime)
        else:
            print ('File not found!')
        return (Account)
'''
    @staticmethod
    def _filewrite(fName):
        with open (fName, 'w+') as f:
            with stock in f:
               if stock == fName:
                    pass
                else:
                    fileStr = (fileStr + str(stock.desc) + ',' \
                        + str(stock.price) + ','\
                        + str(stock.amount) + ','\
                            + datetime.strftime(stock.buytime,'%Y-%m-%d') + ',\n')
                    f.write()
                    fileStr = '''


class stock():
    def __init__(self, desc, price, amount, buytime):
        super().__init__()
        '''init the stock object. at this point it has a description, price,
         amount and date of purchase (DD-MM-YYYY)'''

        self.desc = desc
        self.price = price
        self.amount = amount
        if buytime.lower() == 'now':
            self.buytime = datetime.now().date()
        else:
            try:
                self.buytime = datetime.strptime(buytime, '%Y-%m-%d').date()
            except:
                print ("Error, date doesn't seem correct date should be in year-month-day")


class test():
    def __init__(self, x, y):
        self.x = x
        self.y = y

