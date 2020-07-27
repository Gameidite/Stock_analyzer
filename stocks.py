class stocks:
    def __init__(self):
        self.__datasets = {}
    
    def __len__(self):
        return len(self.__datasets)

    def add(self, symbol, data=""):
        self.__datasets[symbol] = data
        return {symbol: data}

    def __getitem__ (self, symbol):
        data = self.__datasets[symbol]
        if data:
            return data
        print("Err: {} not found".format(symbol))
    
    def get(self, symbol):
        data = self.__datasets[symbol]
        if data:
            return data

    def remove(self, symbol):
        popped = self.__datasets[symbol]

    def get_symbols(self):
        return list(self.__datasets)

    def get_data(self):
        tmp = self.__datasets
        return tmp
    
    def __str__(self):
        symbols = list(self.__datasets)
        tmp = ""
        for i in symbols:
            tmp += str(i) + ": "+ str(self.__datasets[i])+ "\n"
        return tmp
