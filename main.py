import tkinter as tk
from tkinter import ttk
from rich import print
root = tk.Tk()
root.title("jhm")
root.resizable(False, False)
buttons = [
    ["有理数", "整式的加减", "一元一次方程", "几何图形初步", "相交线与平行线", "实数"],
    ["平面直角坐标系", "二元一次方程组", "不等式与不等式组", "数据的收集、整理与描述", "三角形", "全等三角形"],
    ["轴对称", "整式的乘法与因式分解", "分式", "二次根式", "勾股定理", "平行四边形"],
    ["一次函数", "数据的分析", "一元二次方程", "二次函数", "旋转", "圆"],
    ["概率初步", "反比例函数", "相似", "锐角三角函数", "投影与视图", "设置"]
]
def on_click(label):
    if label=="有理数":
        print("[[green]INFO[/green]]  clicked: `有理数`")
    if label=="整式的加减":
        print("[[green]INFO[/green]]  clicked: `整式的加减`")
    if label=="一元一次方程":
        print("[[green]INFO[/green]]  clicked: `一元一次方程`")
    if label=="几何图形初步":
        print("[[green]INFO[/green]]  clicked: `几何图形初步`")
    if label=="相交线与平行线":
        print("[[green]INFO[/green]]  clicked: `相交线与平行线`")
    if label=="实数":
        print("[[green]INFO[/green]]  clicked: `实数`")
    if label=="平面直角坐标系":
        print("[[green]INFO[/green]]  clicked: `平面直角坐标系`")
    if label=="二元一次方程组":
        print("[[green]INFO[/green]]  clicked: `二元一次方程组`")
    if label=="不等式与不等式组":
        print("[[green]INFO[/green]]  clicked: `不等式与不等式组`")
    if label=="数据的收集、整理与描述":
        print("[[green]INFO[/green]]  clicked: `数据的收集、整理与描述`")
    if label=="三角形":
        print("[[green]INFO[/green]]  clicked: `三角形`")
    if label=="全等三角形":
        print("[[green]INFO[/green]]  clicked: `全等三角形`")
    if label=="轴对称":
        print("[[green]INFO[/green]]  clicked: `轴对称`")
    if label=="整式的乘法与因式分解":
        print("[[green]INFO[/green]]  clicked: `整式的乘法与因式分解`")
    if label=="分式":
        print("[[green]INFO[/green]]  clicked: `分式`")
    if label=="二次根式":
        print("[[green]INFO[/green]]  clicked: `二次根式`")
    if label=="勾股定理":
        print("[[green]INFO[/green]]  clicked: `勾股定理`")
    if label=="平行四边形":
        print("[[green]INFO[/green]]  clicked: `平行四边形`")
    if label=="一次函数":
        print("[[green]INFO[/green]]  clicked: `一次函数`")
    if label=="数据的分析":
        print("[[green]INFO[/green]]  clicked: `数据的分析`")
    if label=="一元二次方程":
        print("[[green]INFO[/green]]  clicked: `一元二次方程`")
    if label=="二次函数":
        print("[[green]INFO[/green]]  clicked: `二次函数`")
    if label=="旋转":
        print("[[green]INFO[/green]]  clicked: `旋转`")
    if label=="圆":
        print("[[green]INFO[/green]]  clicked: `圆`")
    if label=="概率初步":
        print("[[green]INFO[/green]]  clicked: `概率初步`")
    if label=="反比例函数":
        print("[[green]INFO[/green]]  clicked: `反比例函数`")
    if label=="相似":
        print("[[green]INFO[/green]]  clicked: `相似`")
    if label=="锐角三角函数":
        print("[[green]INFO[/green]]  clicked: `锐角三角函数`")
    if label=="投影与视图":
        print("[[green]INFO[/green]]  clicked: `投影与视图`")
    if label=="设置":
        print("[[green]INFO[/green]]  clicked: `设置`")
