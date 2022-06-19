import wx
import wx.grid
import wx.lib.agw.aui as aui

import os
from scripts import importData
from scripts import standarizeData
from scripts import normalizeData
from scripts import getMatrixOdDistance
from scripts import getMatrixOfDistanceWithMax
from app.DataTable import DataTable
from app.PlotFrame import PlotFrame
import wx.lib.inspection

class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent, size=(500,500), style=wx.BORDER_RAISED)
        self.parent = parent
        self.SetBackgroundColour(wx.Colour(186, 203, 218))
        self.button = wx.Button(parent=self, label='Dodaj dane', pos=(20, 20), size=(200, 100))
        self.button.SetBackgroundColour(wx.Colour(93, 101, 109))
        self.button.SetOwnForegroundColour('white')
        self.button.Bind(wx.EVT_BUTTON, self.onOpen)
        self.tittle = wx.StaticText(self, label="Data cleanig", style=wx.ALIGN_CENTRE)
        self.font = wx.Font(24, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.tittle.SetFont(self.font)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.AddSpacer(30)
        self.vbox.Add(self.tittle, 0, wx.ALIGN_CENTER_HORIZONTAL, 100)
        self.vbox.AddSpacer(30)
        self.vbox.Add(self.button, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(self.vbox)
        # wx.lib.inspection.InspectionTool().Show()


    def onOpen(self, event):
        wildcard = "CSV files (*.csv)|*.csv"
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return None

        path = dialog.GetPath()

        if os.path.exists(path):
            self.DestroyChildren()

            data = importData(path)

            self.nb = aui.AuiNotebook(self)

            matrixOfDistancePanel = MatrixOfDistanceTable(self, data)
            matrixOfDistanceWithMaxPanel = MatrixOfDistanceWithMax(self, data)

            self.nb.AddPage(matrixOfDistancePanel, 'Macierz odległości')
            self.nb.AddPage(matrixOfDistanceWithMaxPanel, 'Macierz odległości (wartości standaryzowane)')

            sizer = wx.BoxSizer()
            sizer.Add(self.nb, 1, wx.EXPAND | wx.ALL)
            self.SetSizer(sizer)
            self.Layout()
            self.Fit()

            standarizedData = standarizeData(data)
            normalizedData = normalizeData(data)

            plotFrame = PlotFrame(standarizedData, 'Wykresy 1', 2, -2)
            plotFrame.Show(True)

            plotFrame2 = PlotFrame(normalizedData, 'Wykresy 2', 0.95, 0.05)
            plotFrame2.Show(True)


class MatrixOfDistanceTable(wx.Panel):
    def __init__(self, parent, data):
        super().__init__(parent=parent)

        standarizedData = standarizeData(data)
        matrixOfDistance = getMatrixOdDistance(standarizedData)
        table = DataTable(matrixOfDistance, 3)

        grid = wx.grid.Grid(self, -1)
        grid.SetTable(table, takeOwnership=True)
        grid.AutoSizeColumns()

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer.Add(grid, 0, wx.EXPAND)

        mainSizer.Add(sizer, 0, wx.ALL, 5)

        sizer.SetSizeHints(self)
        self.SetSizerAndFit(mainSizer)

class MatrixOfDistanceWithMax(wx.Panel):
    def __init__(self, parent, data):
        super().__init__(parent=parent)

        matrixOfDistance = getMatrixOfDistanceWithMax(data)
        table = DataTable(matrixOfDistance, 1.1)

        grid = wx.grid.Grid(self, -1)
        grid.SetTable(table, takeOwnership=True)
        grid.AutoSizeColumns()

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer.Add(grid, 0, wx.EXPAND)

        mainSizer.Add(sizer, 0, wx.ALL, 5)

        sizer.SetSizeHints(self)
        self.SetSizerAndFit(mainSizer)



