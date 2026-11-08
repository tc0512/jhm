import sys
from pathlib import Path
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
)
from PyQt5.QtCore import Qt
from rich import print
from paths import BASE_DIR
print(f"[[green]INFO [/green]] jhm work directory is `{BASE_DIR}`")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("jhm")
        self.resize(800, 600)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QGridLayout(central)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        buttons = [
            ["有理数", "整式的加减", "一元一次方程", "几何图形初步", "相交线与平行线", "实数"],
            ["平面直角坐标系", "二元一次方程组", "不等式与不等式组", "数据的收集、\n整理与描述", "三角形", "全等三角形"],
            ["轴对称", "整式的乘法与\n因式分解", "分式", "二次根式", "勾股定理", "平行四边形"],
            ["一次函数", "数据的分析", "一元二次方程", "二次函数", "旋转", "圆"],
            ["概率初步", "反比例函数", "相似", "锐角三角函数", "投影与视图", "设置"],
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = QPushButton(text)
                btn.setMinimumHeight(90)
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
        if label=="有理数":
            from Rational import Window
            self.rational_window = Window.MainWindow()
            self.rational_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
