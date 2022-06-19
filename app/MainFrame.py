import wx
from app.MainPanel import MainPanel
from app.HelpFrame import HelpFrame

class MainFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent=parent, title=title, size=size)
        self.frame_number = 1
        self.InitUI()

    def InitUI(self):
        menuBar = wx.MenuBar()

        helpm = wx.Menu()
        menuBar.Append(helpm, "&Help")
        self.Bind(wx.EVT_MENU, self.helpFrame)
        self.Bind(wx.EVT_MENU_OPEN, self.helpFrame)
        self.SetMenuBar(menuBar)
        self.Centre()
        self.Show(True)

    def helpFrame(self, event):
        title = 'Help'.format(self.frame_number)
        frame = HelpFrame(title=title)
        self.frame_number += 1

    def OnInit(self):
        panel = MainPanel(parent=self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizerAndFit(sizer)

