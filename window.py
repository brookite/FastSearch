import os.path

from PySide6.QtCore import Qt
from PySide6.QtGui import QColorConstants
from PySide6.QtWidgets import QMainWindow, QListWidgetItem

from core import TesseractEngine, ClipboardImageListener, JSONSettings
from fsgui import Ui_FSWindow


class FSWindow(QMainWindow, Ui_FSWindow):
    def __init__(self, engine: TesseractEngine):
        super().__init__()
        self._engine = engine
        self._settings = JSONSettings(os.path.expanduser("~/.fastsearch"))
        self._launch_state = False
        self._background_service = ClipboardImageListener(self.send2tesseract)
        self.setupUi(self)
        for lang in self._engine.langs:
            item = QListWidgetItem(lang, self.langs)
            item.setCheckState(Qt.Unchecked)
        self.langs.itemChanged.connect(self.select_lang)
        self.upLang.clicked.connect(self.moveUpLang)
        self.downLang.clicked.connect(self.moveDownLang)
        self._checked_langs = self._collect_checked_langs()
        self.startServiceBtn.clicked.connect(self.handle_launch)
        for lang in self._settings["langs"][::-1]:
             for i in range(self.langs.count()):
                item = self.langs.item(i)
                if item.text() == lang:
                    item.setCheckState(Qt.Checked)


    def send2tesseract(self, img):
        return self._engine.img2tesseract(
            img, self.searchInWeb.isChecked(), self.copyToClipboard.isChecked(),
            True, self.searchEngine.currentIndex()
        )

    def handle_launch(self):
        self._launch_state = not self._launch_state
        if self._launch_state:
            self._background_service.start()
            self.startServiceBtn.setText("Остановить")
            self.label.setText("Сервис FastSearch запущен")
            palette = self.label.palette()
            palette.setColor(self.label.foregroundRole(), QColorConstants.Green)
            self.label.setPalette(palette)
        else:
            self._background_service.destroy()
            del self._background_service
            self._background_service = ClipboardImageListener(self.send2tesseract)
            self.startServiceBtn.setText("Запуск")
            self.label.setText("Сервис FastSearch остановлен")
            palette = self.label.palette()
            palette.setColor(self.label.foregroundRole(), QColorConstants.Red)
            self.label.setPalette(palette)

    def move_to_pos(self, old_index, new_index):
        item = self.langs.takeItem(old_index)
        self.langs.removeItemWidget(item)
        self.langs.insertItem(new_index, item)
        self.langs.setCurrentItem(item)

    def _collect_checked_langs(self):
        checked_langs = []
        for i in range(self.langs.count()):
            item = self.langs.item(i)
            checked_langs.append(item.checkState() == Qt.CheckState.Checked)
        return checked_langs

    def _compare_bool_lists(self, list1, list2):
        assert len(list1) == len(list2)
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return i

    def select_lang(self):
        i = self._compare_bool_lists(self._collect_checked_langs(), self._checked_langs)
        item = None
        if i is not None:
            item = self.langs.item(i)
            if item.checkState() == Qt.CheckState.Checked and item.text() not in self._engine.selected_langs:
                self._engine.selected_langs.insert(0, item.text())
                self.move_to_pos(self.langs.row(item), 0)
            elif item.text() in self._engine.selected_langs:
                self._engine.selected_langs.remove(item.text())
                self.move_to_pos(self.langs.row(item), self.langs.count() - 1)
        self._checked_langs = self._collect_checked_langs()
        self._settings["langs"] = self._engine.selected_langs
        self._settings.save()
        print(self._engine.selected_langs)
        return item

    def moveUpLang(self):
        items = self.langs.selectedItems()
        for item in items:
            index = self.langs.row(item)
            if item.checkState() and index != 0 \
                    and self.langs.item(index - 1).checkState() == Qt.CheckState.Checked:
                self.move_to_pos(index, index - 1)
                self._engine.selected_langs.remove(item.text())
                self._engine.selected_langs.insert(index - 1, item.text())
                self._settings["langs"] = self._engine.selected_langs
                self._settings.save()
                print(self._engine.selected_langs)

    def moveDownLang(self):
        items = self.langs.selectedItems()
        for item in items:
            index = self.langs.row(item)
            if item.checkState() and index != self.langs.count() - 1 \
                    and self.langs.item(index + 1).checkState() == Qt.CheckState.Checked:
                self.move_to_pos(index, index + 1)
                self._engine.selected_langs.remove(item.text())
                self._engine.selected_langs.insert(index + 1, item.text())
                self._settings["langs"] = self._engine.selected_langs
                self._settings.save()
                print(self._engine.selected_langs)
