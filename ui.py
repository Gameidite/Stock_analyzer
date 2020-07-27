class ui:
    def __init__(self):
        import matplotlib.pyplot as plt
        plt.rcParams['toolbar'] = 'None'
        
        self.__fig, ax = plt.subplots()
        ax.set_visible(False)

        self.__fig.canvas.set_window_title("Stock Analysis")
        
        plt.subplots_adjust(left=.125, bottom=.1, right=.9, top=.9, wspace=.5, hspace=.5)
        
        
        
        
        self.axes = []
        self.home_axes = []
        #demensions for plot layout
        self.dems = []
        
        self.dates = []
    def set_dems(self, size):
        import math
        sqrt_size = math.sqrt(size);

        x = round(sqrt_size)
        y = int(size/x) + size%x

        self.dems = [x,y]
        return [x,y]
    
    def set_size(self, size):
        dems = self.set_dems(size)
        self.__fig.set_size_inches(3*dems[0], 2.5*dems[1])

    def load_data(self, datasets):
        self.dataset = datasets
        self.set_size(len(datasets))

    def generate_graphs(self, title, data, n):
        import matplotlib.pyplot as plt
        
        ax = self.__fig.add_subplot(5, 1, n)
        ax.set_title(title)
        
        _min = self.get_min(data)
        _max = self.get_max(data)
        
        self.set_yrange(ax, _min, _max)
        ax.tick_params(labelrotation=30)
        if n < 5:
            plt.setp(ax.get_xticklabels(), visible=False)
            
        l, = ax.plot(self.dates, data)
        return ax
        
    def clickevent(self, event):
        import matplotlib.pyplot as plt
        
        clicked_axes = None
        
        try:
            clicked_axes = event.inaxes
        except:
            pass
        
        if not clicked_axes == None:
            symbol = clicked_axes.get_title()
            
            if symbol in self.symbols:
                self.axes = []
                print("Hello there")
                plt.clf()
                    
                data = self.dataset[symbol][1]
                
                ct = 1
                for ser in data:
                    self.axes.append(self.generate_graphs(symbol+" "+ ser.name, ser.tolist(), ct))
                    ct+=1
                    
                plt.draw()
                return
            
        if self.axes == self.home_axes:
            return
        print("General Kenobi")
        plt.clf()
        self.load(self.dates)

    def leave(self, event):
        self.leave = True
        
    def show(self):
        self.__fig.show()

    def set_yrange(self, ax, _min, _max):
        import numpy as np
        ax.set_yticks(np.arange(_min, _max + ((_max-_min)*.01), (_max-_min)/5))
       
    def get_min(self, data):
        _min = data[0]
        for i in data:
            if i < _min:
                _min = i
        return _min

    def get_max(self, data):
        _max = data[0]
        for i in data:
            if i > _max:
                _max = i
        return _max

    def load(self, dates):
        import matplotlib.pyplot as plt

        self.symbols = self.dataset.get_symbols()
        self.dates = dates
        ct = 0    
        
        for i in range(self.dems[0]):
            for j in range(self.dems[1]):
                if ct < len(self.dataset):
                    tmp = self.__fig.add_subplot(self.dems[1], self.dems[0], ct+1)
                    tmp.set_title(self.symbols[ct])
                    
                    data = self.dataset.get(self.symbols[ct])[1][0]
                    _min = self.get_min(data)
                    _max = self.get_max(data)
                    
                    self.set_yrange(tmp, _min, _max)
                    tmp.tick_params(labelrotation=30)
                    if self.dems[0]+self.dems[1]-(ct+1) > 1:
                        plt.setp(tmp.get_xticklabels(), visible=False)
                    
                    l, = tmp.plot(dates, data)
                    l.figure.canvas.mpl_connect('button_press_event', self.clickevent)

                    
                    ct+=1
                    
                self.axes.append(tmp)
        self.home_axes = self.axes
        plt.show()
