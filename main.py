import sys
from StockClass import stock, portfolio

class menu:
    '''display menu'''
    def __init__(self):
        self.port = portfolio('blank')
        self.choices ={
            'p' : self.printPortfolio,
            'a' : self.addStock,
            'r' : self.removeStock,
            'l' : self.loadPortfolio,
            's' : self.savePortfolio,
            'a' : self.addStock,
            'q' : self.quit
        }
    def display_menu(self):
        
        print ('''
        Stock Controller Menu
        
        p. Print Portfolio
        a. Add Stock
        r. Remove/Edit Stock
        l. Load Portfolio
        s. Save Portfolio
        q. Quit
        ''')

    def run(self):
        '''Display the menu'''
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print ('{0} is not a valid option'.format(choice))
    
    def removeStock(self):
        print('Select a stock to edit/remove...')
        selectList = []
        for indx, Sname in enumerate(self.port.stocks):
            print ('({}) - {}, Held : {} and brought: {}'.format(indx, Sname.desc, Sname.amount, Sname.buytime))
            selectList.append(indx)
        choice = input('Which item do you wish to edit? ')
        try:
            choice = int(choice)
        except:
            choice ='invalid'
        if not(choice in selectList):
            print ('invalid choice')
            return(0)
        else:
            action = input ('Remove or Edit (E/R)')
            if action.lower() == 'r':
                del self.port.stocks[choice]
            elif action.lower() == 'e':
                amt = input('enter new amount of stocks')
                try:
                    amt = int(amt)
                    self.port.stocks[choice].amount = amt
                except:
                    print('Invalid input!')
            else:
                print ('Invalid entry!')
        return(0)

    def printPortfolio(self):
        self.port.printStocks()

    def loadPortfolio(self):
        fName = input ('which file to load? : ')
        port = portfolio.loadPortfolio(fName)
        if port == 0 :
            print ("error loading file")
        else:
            print (' loaded...{}'.format(port.title))
            self.port = port

    def savePortfolio(self):
        fName = input ('file name to save to?')
        self.port.savePortfolio(fName, self.port)

    def addStock(self):
        print ('enter new stock info?. ')
        Sname = input('Stock name?: ')
        Sprice = int(input ('Curent market price?: '))
        Samount = int(input ('Number of stocks?: '))
        Sbuytime = input ('buy date? (YYYY-MM-DD:')
        self.port.addStock(Sname, Sprice, Samount, Sbuytime)


    def quit(self):
        sys.exit(0)

if __name__=="__main__":
    print('running')
    menu().run()