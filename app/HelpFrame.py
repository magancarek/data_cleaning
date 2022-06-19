import wx

class HelpFrame(wx.Frame):
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        panel = HelpPanel(parent=self)
        self.Show()



class HelpPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent

        self.hsizer = wx.BoxSizer()
        self.hsizer.AddStretchSpacer()

        self.panel = wx.Panel(self)
        self.panel.SetSize((350, -1))

        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        self.static_text_title = wx.StaticText(self.panel, label="Uniwersytet Przyrodniczy we Wrocławiu \n\n")
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.static_text_title.SetFont(font)

        self.vsizer.Add(self.static_text_title,
                        flag=wx.EXPAND | wx.ALL | wx.ALIGN_TOP, border=5)

        label = (
            "Wartość odstająca to punkt danych, który różni się od innych obserwacji. Wartości odstające mogą powodować poważne problemy w analizach statystycznych. Aplikacja data cleaning pozwoli użytkownikowi zaobserwować wartości odstające."
            "\n\nAplikacja zawiera okno z przyciskiem DODAJ do wczytywania pliku z danymi w formacie csv, które będą analizowane. \n\n"
            "Po wczytaniu danych aplikacja zwróci w nowym oknie informacje o wartościach odstających - okno z wykresem punktowym mający na celu ich wizualną prezentację oraz macierz odległości."
        )
        style = wx.ALIGN_LEFT
        self.static_text = wx.StaticText(self.panel, label=label, style=style)

        self.vsizer.Add(self.static_text,
                        flag=wx.EXPAND | wx.ALL | wx.ALIGN_TOP, border=5)

        self.static_text_sign = wx.StaticText(self.panel, label="Marta Gancarek")
        font = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.static_text_sign.SetFont(font)

        self.vsizer.Add(self.static_text_sign, flag=wx.EXPAND | wx.ALL | wx.ALIGN_TOP, border=5)

        self.static_text.Wrap(self.panel.Size[0])

        self.panel.SetSizer(self.vsizer)
        self.hsizer.Add(self.panel, 1, flag=wx.EXPAND)
        self.hsizer.AddStretchSpacer()
        self.SetSizer(self.hsizer)

