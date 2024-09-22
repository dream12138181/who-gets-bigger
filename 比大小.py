import wx,random
random.seed(10)
random.seed(10)


class Myframe(wx.Frame):
    def __init__(self,name):
        wx.Frame.__init__(self,None,-1,name+'',size=(400,400))
        self.panel = wx.Panel(self)
        self.box=wx.BoxSizer(wx.VERTICAL)
        self.fgz=wx.FlexGridSizer(wx.HSCROLL)
        botton1=wx.Button(self.panel,pos=(0,300),size=(400,100),label='开始游戏')
        self.fgz.Add(botton1,0,wx.ALIGN_CENTER_VERTICAL)
        self.show_text=wx.TextCtrl(self.panel, size=(400,300),style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.box.Add(self.show_text,0,wx.ALIGN_CENTER)
        self.box.Add(self.fgz,0,wx.ALIGN_CENTER)
        self.panel.SetSizer(self.box)
        self.Bind(wx.EVT_BUTTON,self.start,botton1)
        self.showdata='游戏规则：双方各投掷一次骰子，点数大的一方获胜'
        self.show_text.AppendText(self.showdata)
    def start(self,event):
        self.dig=dialog(None,'游戏界面')
        self.dig.ShowModal()
        self.dig.Destroy()

    def juge(self,event):
        if num>num2:
            data='蓝方获胜'
            self.dig.show_text4.AppendText(data)
        elif num<num2:
            data='红方获胜'
            self.dig.show_text4.AppendText(data)
        else:
            data='双方平局'
            self.dig.show_text4.AppendText(data)
class App(wx.App):
    def __init__(self):
        super(App,self).__init__()
        self.frame = Myframe('对局界面')
        self.frame.Show(True)



class dialog(wx.Dialog):
    def __init__(self,parent,title):
        super(dialog,self).__init__(parent,style=wx.DEFAULT_DIALOG_STYLE,size=(600,400))
        self.app=wx.App()
        self.panel2=wx.Panel(self)
        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.fgz2 = wx.FlexGridSizer(wx.HSCROLL)
        self.botton2 = wx.Button(self.panel2, pos=(0,0), size=(200, 100), label='蓝方投掷')
        self.botton3 = wx.Button(self.panel2, pos=(200,0), size=(200, 100), label='红方投掷')
        self.botton4=wx.Button(self.panel2,pos=(400,0),size=(200,100),label='查看结果')

        self.fgz2.Add(self.botton2, 0, wx.EXPAND)
        self.fgz2.Add(self.botton3, 0, wx.EXPAND)
        self.fgz2.Add(self.botton4, 0, wx.EXPAND)

        self.box2.Add(self.fgz2, 0, wx.EXPAND)
        self.panel2.SetSizer(self.box2)
        self.show_text2 = wx.TextCtrl(self.panel2, size=(600, 100), pos=(0, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.show_text3 = wx.TextCtrl(self.panel2, size=(600, 100), pos=(0, 200),
                                      style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.box2.Add(self.show_text2, 0, wx.EXPAND)
        self.box2.Add(self.show_text3, 0, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.workblue, self.botton2)
        self.Bind(wx.EVT_BUTTON, self.workred, self.botton3)
        self.Bind(wx.EVT_BUTTON, self.judge, self.botton4)

        self.show_text4 = wx.TextCtrl(self.panel2, size=(600, 100), pos=(0, 300),style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.box2.Add(self.show_text4, 0, wx.EXPAND)




    def workblue(self,event):

        global num
        num = random.randint(1, 6)


        self.show_text2.AppendText(f'蓝方投掷的点数为{num}\t\t')


        return num
    def workred(self,event):

        global num2
        num2 = random.randint(1, 6)


        self.show_text3.AppendText(f'红方投掷的点数为{num2}\t\t')


        return num2
    def judge(self,event):
        if num > num2:
            data = '蓝方获胜\t\t'
            self.show_text4.AppendText(data)
        elif num < num2:
            data = '红方获胜\t\t'
            self.show_text4.AppendText(data)
        else:
            data = '双方平局\t\t'
            self.show_text4.AppendText(data)

if __name__ == '__main__':
    name=input('请输入对局双方的用户名：')
    app=wx.App()
    fr=Myframe('开始界面')
    fr.Show()
    app.MainLoop()













