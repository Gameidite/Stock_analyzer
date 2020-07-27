def get_data_by_attr(data, symbol, attr):
    symbol = symbol.upper()
    tmp = []
    
    for i in data:
        if symbol in i:
            if attr in i:
                tmp+=data[i]
                
    return tmp

def get_stock_volumes(stock_hist):
    volumes = []
    
    for i in (stock_hist):
        volumes.append(i["Volume"])

    return volumes
def get_stock_lows(stock_hist):
    lows = []
    
    for i in (stock_hist):
        lows.append(i["Low"])

    return lows
def get_stock_highs(stock_hist):
    highs = []
    
    for i in (stock_hist):
        highs.append(i["High"])
        
    return highs

def get_stock_opens(stock_hist):
    opens = []
    
    for i in stock_hist:
        opens.append(i["Open"])
        
    return opens
    
def get_stock_closes(stock_hist):
    closes = []
    
    for i in (stock_hist):
        closes.append(i["Close"])
        
    return closes

def get_stock_dates(stock_hist):
    dates = stock_hist[0]["Open"].keys().tolist()
    tmp = []
    [tmp.append(i.to_datetime64()) for i in dates]
    
    return tmp

def get_stock_avgs(stock_hist):
    opens = get_stock_opens(stock_hist)
    closes = get_stock_closes(stock_hist)
    dates = get_stock_dates(stock_hist)
    avgs = []
    
    for i in range(len(stock_hist)):
        _open = opens[i]
        _close = closes[i]
        avgs.append(_open-_close)

        
    return avgs
    
def get_data(stock_hist, stock):
    avgs = get_stock_avgs(stock_hist)
    highs = get_stock_highs(stock_hist)
    lows = get_stock_lows(stock_hist)
    opens = get_stock_opens(stock_hist)
    closes = get_stock_closes(stock_hist)
    volumes = get_stock_volumes(stock_hist)
    
    for i in range(len(avgs)):        
        stock.add(symbols[i], [avgs[i], [highs[i], lows[i], opens[i], closes[i], volumes[i]]])
        
    return stock

def build_stocks(symbols):
    from stocks import stocks
    
    stock = stocks()
    
    for i in symbols:
        stock.add(i)
    
    return stock

def search():
    from stock_search import stock_search
    
    ss = stock_search()
    ss.set_tickers(symbols)

    ss.set_start_date("2020/07/06")
    ss.set_end_date("2020/07/23")
    return ss.get_hist()

def render(stock, dates):
    from ui import ui
    
    plot = ui()
    
    plot.load_data(stock)
    plot.load(dates)

if __name__ == '__main__':
    symbols = ["GOOGL", "INVE", "AMC", "APHA", "NOK", "TSLA", "AAPL"]
    stock = build_stocks(symbols)

    stock_hist = search()

    data = get_data(stock_hist, stock)

    dates = get_stock_dates(stock_hist)

    render(data, dates)
