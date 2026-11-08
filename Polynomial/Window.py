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
