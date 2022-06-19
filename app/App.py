import wx
from app.MainFrame import MainFrame

class DataCleaningApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # init frame
        self.InitFrame()

    def InitFrame(self):
        frame = MainFrame(parent=None, title="DataCleaning", size=(500, 500))
        frame.OnInit()
        frame.Show(True)
