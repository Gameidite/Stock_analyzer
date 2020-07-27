class stock_search():
    def __init__(self):
        self.start_date = ""
        self.end_date = ""
        self.tickers = ""
        
        self.set_start_date(self.get_cur_date())

    #ticker_str can either be a string of stock symbols like "NEXA RLGY" or
    #a list of strs like ["NEXA, "RLGY"])
    def get_hist(self):
        import yfinance as yf
        hist = []
        for i in self.tickers:
            ticker = yf.Ticker(i)
            hist.append(ticker.history(start=self.start_date, end=self.end_date))
        return hist
    
    def set_tickers(self, tickers):
            self.tickers = tickers

    def stock_symbol_format(self, symbols):
        if isinstance(symbols, str):
            if " " in symbols:
                symbols = symbols.split(" ")
            else:
                return symbols
            
        if isinstance(symbols, list):
            return self.get_symbols(symbols)
        
        return -1

    #gets the symbols correctly formatted from choice
    def get_symbols(self, symbol_list):
        ticker_str = ""
        for i in symbol_list:
            if len(i) > 5 or len(i) < 3:
                print("Err: Stock {} is incorrectly formatted".format(i))
            else:
                ticker_str+= " " + i.upper()
        return ticker_str
    
    #checks if date comes after the start date       
    def is_after_start_date(self, date):
        if not self.is_date(date):
            return False
        if "-" in date:
            date = date.split("-")
        print(date)
        split_start = self.start_date.split("-")
        print(self.start_date)
        if int(split_start[1]) > int(date[1]):
            return False
        if int(split_start[1]) >= int(date[1]) and int(split_start[2]) > int(date[2]):
            return False
        return True
        
    #checks is format meets yyyy-mm-dd format 
    def is_date(self, date):
        import re
        if not isinstance(date, str):
            pass
        elif re.match("[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]", date):
            return True
        
        print("Err: date is incorrect format")
        return False

    #sets start date while checking date for correct formatting
    def set_start_date(self, date):
        if "/" in date:
            date = date.replace("/","-")
        if self.is_date(date):
            self.start_date = date
    
    def set_end_date(self, date):
        if "/" in date:
            date = date.replace("/","-")
        if self.is_date(date):
            if self.is_after_start_date(date):               
                self.end_date = date
            else:
                print("Err: End date entered is after start date")


    #returns str of the current date in format yyyy-mm-dd  
    def get_cur_date(self):
        import datetime
        
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")

    #returns a string with start time, end time, and symbols for the search
    def __str__(self):
        return("Start:{}\nEnd:{}\nTickers:{}".format(self.start_date, self.end_date, self.tickers))


            

