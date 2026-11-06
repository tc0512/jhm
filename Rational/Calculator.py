from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QVBoxLayout, QPushButton, QMessageBox)
import ast
from fractions import Fraction
import sys


def eval_rational(expr):
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)

        if isinstance(node, ast.Constant):
            v = node.value
            if isinstance(v, bool):
                raise ValueError("不支持布尔值")
            if isinstance(v, int):
                return Fraction(v)
            if isinstance(v, float):
                return Fraction(str(v))     # 字符串构造，避免浮点误差
            raise ValueError("只支持数字")

        if isinstance(node, ast.BinOp):
            l = _eval(node.left)
            r = _eval(node.right)
            if isinstance(node.op, ast.Add):      return l + r
            if isinstance(node.op, ast.Sub):      return l - r
            if isinstance(node.op, ast.Mult):     return l * r
            if isinstance(node.op, ast.Div):
                if r == 0:
                    raise ZeroDivisionError("除数不能为 0")
                return l / r
            if isinstance(node.op, ast.FloorDiv):
                if r == 0:
                    raise ZeroDivisionError("除数不能为 0")
                return Fraction(l // r)
            if isinstance(node.op, ast.Mod):
                if r == 0:
                    raise ZeroDivisionError("除数不能为 0")
                return l % r
            if isinstance(node.op, ast.Pow):
                if r.denominator != 1:
                    raise ValueError("指数必须为整数")
                return l ** r.numerator
            raise ValueError(f"不支持的运算符 {type(node.op).__name__}")

        if isinstance(node, ast.UnaryOp):
            v = _eval(node.operand)
            if isinstance(node.op, ast.USub): return -v
            if isinstance(node.op, ast.UAdd): return +v
            raise ValueError("不支持的一元运算符")

        raise ValueError(f"不支持的语法：{type(node).__name__}")

    return _eval(ast.parse(expr, mode="eval"))


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("jhm>有理数>有理数计算器")
        self.resize(320, 130)

        layout = QVBoxLayout(self)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("请输入表达式，如 0.1 + 0.2")
        self.edit.setEchoMode(QLineEdit.Normal)
        self.edit.setMaxLength(100)
        layout.addWidget(self.edit)

        self.btn = QPushButton("计算")
        self.btn.clicked.connect(self.on_submit)
        layout.addWidget(self.btn)

        self.edit.returnPressed.connect(self.on_submit)

    def on_submit(self):
        text = self.edit.text().strip()

        if not text:
            QMessageBox.warning(self, "提示", "表达式不能为空！")
            return

        try:
            result = eval_rational(text)
        except ZeroDivisionError as e:
            QMessageBox.warning(self, "计算错误", f"除零错误：{e}")
            return
        except SyntaxError:
            QMessageBox.warning(self, "计算错误", "表达式语法有误")
            return
        except Exception as e:
            QMessageBox.warning(self, "计算错误", f"无法计算：{e}")
            return

        # 显示
        if result.denominator == 1:
            res_part = str(result.numerator)
        else:
            res_part = f"{result.numerator}/{result.denominator}"
        float_part = float(result)
        if float_part>0:
            sym_part = "+"
        if float_part==0:
            sym_part = "0"
        if float_part<0:
            sym_part = "-"
        # 有理数分类
        if float_part.is_integer(): #整数
            if sym_part=="+":
                category_part = "正整数"
            if sym_part=="0":
                category_part = "0"
            if sym_part=="-":
                category_part = "负整数"
        else: #分数
            category_part = "正分数" if sym_part=="+" else "负分数"
        msg = (f"结果: {res_part}<br>"
               f"数值近似: {float_part}<br>"
               f"符号: {sym_part}<br>"
               f"类别: {category_part}<br>"
               "数轴: <br>")
        QMessageBox.information(self, "计算结果", msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
