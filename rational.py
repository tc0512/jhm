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
            """
            win = RichTextWindow(title="jhm>有理数>有理数", html=html, parent=self)
            win.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
