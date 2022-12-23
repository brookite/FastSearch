import sys
from PySide6.QtWidgets import QApplication
from window import FSWindow
from core import find_tesseract, TesseractEngine


def main():
    app = QApplication(sys.argv)
    if tesseract_path := find_tesseract():
        engine = TesseractEngine(tesseract_path)
        mainwindow = FSWindow(engine)
        mainwindow.show()
    else:
        pass
    sys.exit(app.exec())


if __name__ == '__main__':
    main()