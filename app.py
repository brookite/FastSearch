import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from window import FSWindow
from core import find_tesseract, TesseractEngine


def main():
    app = QApplication(sys.argv)
    if tesseract_path := find_tesseract():
        engine = TesseractEngine(tesseract_path)
        mainwindow = FSWindow(engine)
        mainwindow.show()
    else:
        QMessageBox.crtitical(None, "Tesseract не найден",
                              "Проверьте, находится ли библиотека tesseract в одноименной папке рядом с проектом или переменной PATH")
    sys.exit(app.exec())


if __name__ == '__main__':
    main()