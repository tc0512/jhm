import tkinter as tk
from tkinter import ttk
from rich import print
root = tk.Tk()
root.title("jhm")
root.geometry("600x500")
root.resizable(False, False)
frame = ttk.Frame(root, padding=10)
frame.pack()
buttons = [
    ["有理数", "整式的加减", "一元一次方程", "几何图形初步", "相交线与平行线", "实数"],
    ["平面直角坐标系", "二元一次方程组", "不等式与不等式组", "数据的收集、整理与描述", "三角形", "全等三角形"],
    ["轴对称", "整式的乘法与因式分解", "分式", "二次根式", "勾股定理", "平行四边形"],
    ["一次函数", "数据的分析", "一元二次方程", "二次函数", "旋转", "圆"],
    ["概率初步", "反比例函数", "相似", "锐角三角函数", "投影与视图", "设置"]
]
for i in range(5):
    for j in range(6):
        ttk.Button(frame, text=buttons[i][j], width=11,
                   command=lambda i=i, j=j: print(f"[[green]INFO[/green]] clicked: `{buttons[i][j]}`")).grid(row=i, column=j, padx=3, pady=3)
root.mainloop()
