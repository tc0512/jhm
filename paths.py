import sys
from pathlib import Path

if hasattr(sys, "_MEIPASS"):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent   # jhm/ 根，一层就够

IMG_DIR = BASE_DIR / "images"

if getattr(sys, "frozen", False):
    APP_DIR = Path(sys.executable).resolve().parent
else:
    APP_DIR = Path(__file__).resolve().parent    # jhm/ 根

TMP_DIR = APP_DIR / "tmp"
TMP_DIR.mkdir(exist_ok=True)
