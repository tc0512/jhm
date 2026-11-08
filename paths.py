import sys
from pathlib import Path

# 资源目录（只读）：打包后 _MEIPASS，开发时项目根
if hasattr(sys, "_MEIPASS"):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent.parent   # paths.py 在 Rational/ 下

IMG_DIR = BASE_DIR / "images"

# 可写目录：打包后 exe 同级，开发时项目根
if getattr(sys, "frozen", False):
    APP_DIR = Path(sys.executable).resolve().parent
else:
    APP_DIR = Path(__file__).resolve().parent.parent

TMP_DIR = APP_DIR / "tmp"
TMP_DIR.mkdir(exist_ok=True)
