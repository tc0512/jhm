import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QDialog,
    QVBoxLayout, QTextBrowser
)
from PyQt5.QtCore import Qt
from rich import print

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
                <h2>1. 什么是正数和负数?</h2>
                <p>像3, 1.8%, 3.5这样大于0的数叫作正数</p>
                <p>像-3, -2.8%, -53.5, -1.2这样大于0的数叫作负数</p>
                <h2>2. 如何认识`0`?</h2>
                <p>0既不是正数, 也不是复数。0是正数和负数的分界</p>
                <h2>3. 什么是具有相反意义的量?</h2>
                <p>为了用数表示具有相反意义的量, 我们把某种量的一种意义规定为正的, 
                而把与它相反的一种意义规定为负的。描述一对具有相反意义的量的词语一
                般是一对反义词, 如上升和下降, 收入与支出等。</p>
            """
            win = RichTextWindow(title="jhm>有理数>正数和负数", html=html, parent=self)
            win.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
