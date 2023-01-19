# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'records.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_recordForm(object):
    def setupUi(self, recordForm):
        if not recordForm.objectName():
            recordForm.setObjectName(u"recordForm")
        recordForm.resize(565, 336)
        recordForm.setToolTipDuration(-1)
        self.verticalLayout = QVBoxLayout(recordForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.records = QListWidget(recordForm)
        QListWidgetItem(self.records)
        QListWidgetItem(self.records)
        self.records.setObjectName(u"records")
        self.records.setProperty("isWrapping", False)
        self.records.setWordWrap(True)

        self.verticalLayout.addWidget(self.records)

        self.copy = QPushButton(recordForm)
        self.copy.setObjectName(u"copy")

        self.verticalLayout.addWidget(self.copy)


        self.retranslateUi(recordForm)

        QMetaObject.connectSlotsByName(recordForm)
    # setupUi

    def retranslateUi(self, recordForm):
        recordForm.setWindowTitle(QCoreApplication.translate("recordForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))

        __sortingEnabled = self.records.isSortingEnabled()
        self.records.setSortingEnabled(False)
        ___qlistwidgetitem = self.records.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("recordForm", u"\u041c\u0435\u043d\u044e\n"
"How can I get the indices of QListWidget::selectedItems()?\n"
"stackoverflow.com\u203a\u2026how\u2026of-qlistwidgetselecteditems\n"
"I have QListWidget and I need to get the indices of selected items. QListWidget has a method named selectedIndexes as well, but it is a protected one, so you have to use such a tricky way to get them. Share. Improve this answer.", None));
        ___qlistwidgetitem1 = self.records.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("recordForm", u"gdfgfgfgfgfgfgfgfgfggfgfgdgfddfg", None));
        self.records.setSortingEnabled(__sortingEnabled)

        self.copy.setText(QCoreApplication.translate("recordForm", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430", None))
    # retranslateUi

