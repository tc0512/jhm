import wx
from rich import print

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="jhm", size=(800, 600))

        panel = wx.Panel(self)
        sizer = wx.GridSizer(rows=5, cols=6, hgap=6, vgap=6)

        buttons = [
            ["有理数", "整式的加减", "一元一次方程", "几何图形初步", "相交线与平行线", "实数"],
            ["平面直角坐标系", "二元一次方程组", "不等式与不等式组", "数据的收集、\n整理与描述", "三角形", "全等三角形"],
            ["轴对称", "整式的乘法与\n因式分解", "分式", "二次根式", "勾股定理", "平行四边形"],
            ["一次函数", "数据的分析", "一元二次方程", "二次函数", "旋转", "圆"],
            ["概率初步", "反比例函数", "相似", "锐角三角函数", "投影与视图", "设置"],
        ]

        for row in buttons:
            for text in row:
                btn = wx.Button(panel, label=text, size=(-1, 65))
                btn.Bind(wx.EVT_BUTTON, self.on_click)
                sizer.Add(btn, 0, wx.EXPAND)

        panel.SetSizer(sizer)
        self.Centre()
        self.Show()

    def on_click(self, event):
        btn = event.GetEventObject()
        label = btn.GetLabel().replace("\n", "")
        print(f"[[green]INFO[/green]] clicked: `{label}`")

if __name__ == "__main__":
    app = wx.App()
    MainFrame()
    app.MainLoop()
