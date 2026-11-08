from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QVBoxLayout, QPushButton, QMessageBox)
import ast
from fractions import Fraction
import sys
from pathlib import Path
from ._libnumberline import number_line
from paths import TMP_DIR
tmp_dir = str(Path(__file__).resolve().parent)+"/../tmp"

ALLOWED_FUNCS = {
    "abs": lambda f: abs(f),   # Fraction 支持 abs()
}

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
                return Fraction(str(v))
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

        # ===== 新增：函数调用 =====
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("只支持简单函数名")
            name = node.func.id
            if name not in ALLOWED_FUNCS:
                raise ValueError(f"不支持的函数：{name}")
            if node.keywords:
                raise ValueError("不支持关键字参数")
            if len(node.args) != 1:
                raise ValueError(f"{name} 需要 1 个参数")
            arg = _eval(node.args[0])
            return ALLOWED_FUNCS[name](arg)

        raise ValueError(f"不支持的语法：{type(node).__name__}")

    return _eval(ast.parse(expr, mode="eval"))

def to_chinese_unit(x):
    x = float(x)
    abs_x = abs(x)
    sign = "-" if x < 0 else ""

    if abs_x >= 1e8:
        return f"{sign}{abs_x / 1e8:.3f}亿"
    elif abs_x >= 1e4:
        return f"{sign}{abs_x / 1e4:.3f}万"
    else:
        return f"{sign}{abs_x:.3f}"

class MainWindow(QWidget):
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

        #分数形式
        if result.denominator == 1:
            res_part = str(result.numerator)
        else:
            res_part = f"{result.numerator}/{result.denominator}"
        float_part = float(result) #数值
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
        # 生成数轴
        number_line(float_part)
        # 相反数
        negative_res = -result
        negative_part = f"{negative_res.numerator}/{negative_res.denominator}" if negative_res.denominator!=1 else str(negative_res.numerator)
        # 绝对值
        abs_res = abs(result)
        abs_part = f"{abs_res.numerator}/{abs_res.denominator}" if abs_res.denominator!=1 else str(abs_res.numerator)
        # 科学记数法
        sci_part = f"{float_part:e}"
        # 弹窗消息
        msg = (f"结果: {res_part}<br>"
               f"数值近似: {float_part}<br>"
               f"符号: {sym_part}<br>"
               f"类别: {category_part}<br>"
               "数轴: <br>"
               f'<img src="{TMP_DIR}/numberline.png" alt="🖼️" width="300">'
               f"相反数: {negative_part}<br>"
               f"绝对值: {abs_part}<br>"
               f"科学记数法: {sci_part}<br>"
               f"近似数: {to_chinese_unit(float_part)}")
        QMessageBox.information(self, "计算结果", msg)
