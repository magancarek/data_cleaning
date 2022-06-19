import wx
import wx.lib.agw.aui as aui
import matplotlib as mpl
from matplotlib.backends.backend_wxagg import (
    FigureCanvasWxAgg as FigureCanvas,
    NavigationToolbar2WxAgg as NavigationToolbar)

class Plot(wx.Panel):
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)

        #------------

        self.figure = mpl.figure.Figure(dpi=dpi, figsize=(2, 2))

        #------------

        self.canvas = FigureCanvas(self, -1, self.figure)

        #------------

        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)

class PlotNotebook(wx.Panel):
    def __init__(self, parent, id=-1):
        wx.Panel.__init__(self, parent, id=id)

        self.nb = aui.AuiNotebook(self)

        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def Add(self, name="plot"):
        """
        ...
        """

        page = Plot(self.nb)
        self.nb.AddPage(page, name)
        return page.figure

class PlotFrame(wx.Frame):
    def __init__(self, data, title, tresholdUp, tresholdDown):
        wx.Frame.__init__(self, None, -1, title, size=(450, 350))
        self.data = data
        self.tresholdUp = tresholdUp
        self.tresholdDown = tresholdDown
        self.CreateCtrls()

    def CreateCtrls(self):
        plotter = PlotNotebook(self)

        for num in range(0, len(self.data.columns)):
            for num2 in range(num + 1, len(self.data.columns)):
                figName = f'{self.data.columns[num]} {self.data.columns[num2]}'
                axes = plotter.Add(figName).gca()
                data1Bool = self.data[self.data.columns[num]].between(self.tresholdDown, self.tresholdUp)
                data2Bool = self.data[self.data.columns[num2]].between(self.tresholdDown, self.tresholdUp)

                axes.scatter(self.data[self.data.columns[num]][data1Bool], self.data[self.data.columns[num2]][data1Bool], c='blue')
                axes.scatter(self.data[self.data.columns[num]][~data1Bool], self.data[self.data.columns[num2]][~data1Bool], c='red')
                axes.scatter(self.data[self.data.columns[num]][~data2Bool], self.data[self.data.columns[num2]][~data2Bool], c='red')

