import sys
from pathlib import Path
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QDialog,
    QVBoxLayout, QTextBrowser
)
from PyQt5.QtCore import Qt
from rich import print
from paths import IMG_DIR

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
        self.setWindowTitle("jhm>整式")
        self.resize(800, 600)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QGridLayout(central)
        layout.setSpacing(10)  # 同时控制 hgap 和 vgap
        layout.setContentsMargins(10, 10, 10, 10)

        buttons = ["整式", "整式的加减", "整式加减计算器"]
        for i, text in enumerate(buttons):
            btn = QPushButton(text)
            btn.setMinimumWidth(253)
            btn.setMinimumHeight(580)
            btn.clicked.connect(self.on_click)
            layout.addWidget(btn, 0, i)
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
        if label=="整式":
            html = f"""
                <h2>1. 什么是单项式? </h2>
                <p>如100t, 0.8p, mn, <img src="{IMG_DIR}/polynomial-picture1.png" alt="🖼️" style="vertical-align:middle;width:16px;height:16p;">, -n, 这些式子都是数或字母的积, 像这样的式子叫作单项式。单独的一个数或一个字母也是单项式。</p>
                <p>(*) 单项式表示数与字母相乘时, 通常把数写在前面。</p>
                <h2>2. 什么是单项式的系数与次数? </h2>
                <p>单项式中的数字因数叫作这个单项式的系数。一个单项式中, 所有字母的指数的和叫作这个单项式的次数。对于一个非0的数, 规定它的次数为0。</p>
                <p>例如: 单项式<img src="{IMG_DIR}/polynomial-picture2.png" alt="🖼️" style="vertical-align:middle;width:16px;height:16p;">的系数是-1, 次数是6。</p>
                <p>(*) 单项式的系数是带分数时要化为假分数。</p>
                <p>(*) 单项式的系数包括系数前面的符号。</p>
                <p>(*) 若字母的指数是1, 书写时可省略, 但在计算单项式的次数时不能丢掉。</p>
                <h2>3. 什么是多项式? </h2>
                <p>几个单项式的和叫作多项式。其中, 每个单项式叫做多项式的项, 不含字母的项叫作常数项。例如: 多项式<img src="{IMG_DIR}/polynomial-picture3.png" alt="🖼️" style="vertical-align:middle;width:16px;height:16p;">的项是<img src="{IMG_DIR}/polynomial-picture4.png" alt="🖼️" style="vertical-align:middle;width:16px;height:16p;">, 2x与-18, 其中-18是常数项。</p>
                <h2>4. 什么是多项式的次数? </h2>
                <p>多项式里, 次数最高项的次数, 叫作这个多项式的次数。如: 多项式<img src="{IMG_DIR}/polynomial-picture5.png" alt="🖼️" style="vertical-align:middle;width:16px;height:16p;">中次数最高项是二次项<img src="{IMG_DIR}/polynomial-picture4.png" alt="🖼️" style="vertical-align:middle;width:16px;height:16p;">, 则这个多项式的次数是2。</p>
                <h2>5. 什么是整式? </h2>
                <p>单项式与多项式统称整式。</p>
            """
            win = RichTextWindow(title="jhm>整式>整式", html=html, parent=self)
            win.exec_()
