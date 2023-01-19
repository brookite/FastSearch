from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QListWidgetItem, QMessageBox, QWidget, QApplication

from core import TesseractEngine
from recordsui import Ui_recordForm


class RecordWindow(QWidget, Ui_recordForm):
    def __init__(self, engine: TesseractEngine):
        super().__init__()
        self._engine = engine
        self.setupUi(self)
        self.copy.clicked.connect(self.copyClipboard)
        self._buf = []
        self.update_records()

    def changeEvent(self, event: QEvent):
        if event.type() == QEvent.ActivationChange and self.isActiveWindow():
            self.updateRecordsIfRequired()

    def show(self) -> None:
        self.update_records()
        super().show()

    def update_records(self):
        self.records.clear()
        self._buf = list(self._engine.records)
        for record in self._engine.records:
            self.records.addItem(record)

    def updateRecordsIfRequired(self):
        if self._buf != self._engine.records:
            self.update_records()

    def copyClipboard(self):
        self.updateRecordsIfRequired()
        selected = self.records.selectedItems()
        if len(selected):
            text = selected[0].text()
            QApplication.clipboard().setText(text)









