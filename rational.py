import sys
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QDialog,
    QVBoxLayout, QTextBrowser
)
from PyQt5.QtCore import Qt
from rich import print

work_dir = str(Path(__file__).resolve().parent)

class RichTextWindow(QDialog):
    def __init__(self, title, html, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(500, 400)

        layout = QVBoxLayout(self)

        browser = QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.setHtml(html)
        layout.addWidget(browser)

        btn = QPushButton("关闭")
        btn.clicked.connect(self.accept)
        layout.addWidget(btn)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("jhm>有理数")
        self.resize(800, 600)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QGridLayout(central)
        layout.setSpacing(10)  # 同时控制 hgap 和 vgap
        layout.setContentsMargins(10, 10, 10, 10)

        buttons = [
            ["正数和负数", "有理数", "有理数的加减法"],
            ["有理数的乘除法", "有理数的乘方", "小工具"]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = QPushButton(text)
                btn.setMinimumHeight(285)
                btn.clicked.connect(self.on_click)
                layout.addWidget(btn, r, c)

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_click(self):
        btn = self.sender()
        label = btn.text().replace("\n", "")
        print(f"[[green]INFO [/green]] clicked: `{label}`")
        if label=="正数和负数":
            html = """
                <h2>1. 什么是正数和负数? </h2>
                <p>像3, 1.8%, 3.5这样大于0的数叫作正数</p>
                <p>像-3, -2.8%, -53.5, -1.2这样大于0的数叫作负数</p>
                <h2>2. 如何认识`0`? </h2>
                <p>0既不是正数, 也不是复数。0是正数和负数的分界</p>
                <h2>3. 什么是具有相反意义的量? </h2>
                <p>为了用数表示具有相反意义的量, 我们把某种量的一种意义规定为正的, 而把与它相反的一种意义规定为负的。描述一对具有相反意义的量的词语一般是一对反义词, 如上升和下降, 收入与支出等。</p>
            """
            win = RichTextWindow(title="jhm>有理数>正数和负数", html=html, parent=self)
            win.exec_()
        if label=="有理数":
            html = f"""
                <h2>1. 什么是有理数? </h2>
                <p>正整数、0、负整数统称为整数; 正分数、负分数统称为分数 (因为小数可以化成分数, 所以也将其看成分数) 。整数和分数统称为有理数。</p>
                <h2>2. 有理数是如何分类的? </h2>
                <h3>(1)按整数和分数的关系分类: </h3>
                <img src="{work_dir}/images/rational-picture1.jpg" alt="🖼️" width="300">
                <h3>(2)按正数、0和负数的关系分类: </h3>
                <img src="{work_dir}/images/rational-picture2.jpg" alt="🖼️" width="300">
                <h2>3. 什么是数轴? </h2>
                <p>数轴是规定了原点、正方向和单位长度的直线。</p>
                <img src="{work_dir}/images/rational-picture3.jpg" alt="🖼️" width="300">
                <p>(*) 数轴的三要素: 原点、正方向和单位长度, 三者缺一不可。</p>
                <h2>4. 数轴上的点和有理数的关系是什么</h2>
                <p>一般地, 设a是一个实数, 则数轴上表示数a的点在原点的右边, 与原点的距离是a个单位长度; 表示数-a的点在原点的左边, 与原点的距离是a个单位长度。任何一个有理数都能在数轴上找到表示它位置的点, 而且是唯一确定的点。</p>
                <h2>5. 什么是相反数? </h2>
                <p>  像2和-2, 5和-5这样, 只有符号不同的数叫作互为相反数。</p>
                <p>  一般地, a和-a互为相反数。特别地, 0的相反数是0。这里, a表示任意一个数, 可以是正数、负数, 也可以是0。</p>
                <p>(*) 数轴上表示相反数的两个点分布在原点两旁, 且到原点的距离相等, 这两点关于原点对称。</p>
                <p>(*) 如果a, b互为相反数, 那么a+b=0或a=-b或b=-a; 反之, 若a+b=0, 那么a, b互为相反数。</p>
                <p>(*) 相反数是它本身的数是0。</p>
                <h2>6. 什么是绝对值? </h2>
                <p>(1)绝对值的定义: 一般地, 数轴上表示数a的点与原点的距离叫做数a的绝对值, 记作|a|。</p>
                <p>(2)由绝对值的定义可知: 一个正数的绝对值是它本身; 一个负数的绝对值是它的相反数; 0的绝对值是0。即</p>
                <p>①如果a&gt;0, 那么|a|=a; </p>
                <p>②如果a=0, 那么|a|=0; </p>
                <p>③如果a&lt;0, 那么|a|=-a。</p>
                <p>(*) 绝对值是a (a&gt;0) 的数有两个, 它们互为相反数, 即为±a。</p>
                <p>(*) 绝对值相等的两个数相等或互为相反数, 即: 若|a|=|b|, 则a=b或a+b=0。</p>
                <p>(*) 任意实数的绝对值都是非负数, 即|a|≥0。</p>
                <h2>7. 如何比较有理数大小? </h2>
                <p>在数轴上表示有理数, 它们从左到右的顺序, 就是从小到大的顺序, 即左边的数小于右边的数。从而可知: </p>
                <p>(1)正数大于0, 0大于负数, 正数大于负数; </p>
                <p>(2)两个负数, 绝对值大的反而小。</p>
            """
            win = RichTextWindow(title="jhm>有理数>有理数", html=html, parent=self)
            win.exec_()
        if label=="有理数的加减法":
            html = """
                <h2>1. 有理数的加法法则是什么? </h2>
                <p>(1)同号两数相加, 取相同的符号, 并把绝对值相加。</p>
                <p>(2)绝对值不相等的异号两数相加, 取绝对值较大的加数的符号, 并用较大的绝对值减去较小的绝对值。互为相反数的两个数相加得0。</p>
                <p>一个数同0相加, 仍得这个数。</p>
                <h2>2. 有理数加法的运算律是什么? </h2>
                <p>(1)加法交换律: a+b=b+a。</p>
                <p>(2)加法结合律: (a+b)+c=a+(b+c)。</p>
                <h2>3. 有理数的减法法则是什么? </h2>
                <p>减去一个数, 等于加这个数的相反数。即a-b=a+(-b)。</p>
                <h2>4. 有理数的加减混合运算有哪些技巧? </h2>
                <p>(1)有理数的加减混合运算可统一成加法运算。例如: (-8)-(-10)+(-6)-(+4)=(-8)+(+10)+(-6)+(-4)=-8。</p>
                <p>(2)有理数的加减混合运算统一成加法运算后可适当运用加法运算律, 使运算简便。</p>
                <p>(*) 加减混合运算中, 使用加法交换律时, 要连同前面的符号一起交换。</p>
            """
            win = RichTextWindow(title="jhm>有理数>有理数的加减法", html=html, parent=self)
            win.exec_()
        if label=="有理数的乘除法":
            html = f"""
                <h2>1. 有理数的乘法法则是什么? </h2>
                <p>  两数相乘, 同号得正, 异号得负, 并把绝对值相乘。</p>
                <p>  任何数与0相乘, 都得0。</p>
                <h2>2. 什么是倒数? </h2>
                <p>乘积是1的两个数互为倒数。即若ab=1, 则a, b互为倒数。例如1的倒数是1, -1的倒数是-1。</p>
                <h2>3. 如何确定积的符号? </h2>
                <p>  几个不为0的数相乘, 当负因数有偶数个时, 积为正; 当负因数有奇数个时, 积为负。</p>
                <p>当因数中有一个数为0时, 积为0。</p>
                <h2>4. 有理数乘法的运算律是什么? </h2>
                <p>(1)乘法交换律: ab=ba。</p>
                <p>(2)乘法结合律: (ab)c=a(bc)。</p>
                <p>(3)分配律: a(b+c)=ab+ac。</p>
                <p>逆用分配律, 可简化运算。</p>
                <h2>5. 有理数的除法法则是什么? </h2>
                <p>  除以一个不等于0的数, 等于乘这个数的倒数, 即<img src="{work_dir}/images/rational-picture4.png" alt="" style="vertical-align:middle;width:16px;height:16px;">。</p>
            """
            win = RichTextWindow(title="jhm>有理数>有理数的乘除法", html=html, parent=self)
            win.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
