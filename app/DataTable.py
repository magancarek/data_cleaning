import wx.grid

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'
DANGER_OUTLIER_COLOUR = '#FF0000'


class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None, outlierLimit=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data
        self.outlierLimit = outlierLimit

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    def GetColLabelValue(self, col):
        return str(self.data.columns[col])

    def GetTypeName(self, row, col):
        return wx.grid.GRID_VALUE_STRING

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)

        if self.outlierLimit and self.data[row][col] >= self.outlierLimit:
            attr.SetBackgroundColour(DANGER_OUTLIER_COLOUR)
        return attr
