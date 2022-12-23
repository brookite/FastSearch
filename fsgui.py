# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fsgui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_FSWindow(object):
    def setupUi(self, FSWindow):
        if not FSWindow.objectName():
            FSWindow.setObjectName(u"FSWindow")
        FSWindow.resize(623, 392)
        self.centralwidget = QWidget(FSWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.RichText)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.startServiceBtn = QPushButton(self.centralwidget)
        self.startServiceBtn.setObjectName(u"startServiceBtn")

        self.horizontalLayout.addWidget(self.startServiceBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setBaseSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 420, 169))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.langs = QListWidget(self.scrollAreaWidgetContents)
        self.langs.setObjectName(u"langs")

        self.verticalLayout_3.addWidget(self.langs)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.upLang = QPushButton(self.scrollAreaWidgetContents)
        self.upLang.setObjectName(u"upLang")

        self.horizontalLayout_5.addWidget(self.upLang)

        self.downLang = QPushButton(self.scrollAreaWidgetContents)
        self.downLang.setObjectName(u"downLang")
        self.downLang.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.downLang)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.copyToClipboard = QCheckBox(self.centralwidget)
        self.copyToClipboard.setObjectName(u"copyToClipboard")
        self.copyToClipboard.setChecked(True)

        self.horizontalLayout_4.addWidget(self.copyToClipboard)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchInWeb = QCheckBox(self.centralwidget)
        self.searchInWeb.setObjectName(u"searchInWeb")

        self.horizontalLayout_3.addWidget(self.searchInWeb)

        self.searchEngine = QComboBox(self.centralwidget)
        self.searchEngine.addItem("")
        self.searchEngine.addItem("")
        self.searchEngine.setObjectName(u"searchEngine")

        self.horizontalLayout_3.addWidget(self.searchEngine)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.savedRecordsBtn = QPushButton(self.centralwidget)
        self.savedRecordsBtn.setObjectName(u"savedRecordsBtn")

        self.verticalLayout.addWidget(self.savedRecordsBtn)

        FSWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FSWindow)
        self.statusbar.setObjectName(u"statusbar")
        FSWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FSWindow)

        QMetaObject.connectSlotsByName(FSWindow)
    # setupUi

    def retranslateUi(self, FSWindow):
        FSWindow.setWindowTitle(QCoreApplication.translate("FSWindow", u"FastSearch GUI", None))
        self.label.setText(QCoreApplication.translate("FSWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441 FastSearch \u043d\u0435 \u0437\u0430\u043f\u0443\u0449\u0435\u043d", None))
        self.startServiceBtn.setText(QCoreApplication.translate("FSWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.label_3.setText(QCoreApplication.translate("FSWindow", u"FastSearch \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0441 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439 \u0432 \u0431\u0443\u0444\u0435\u0440\u0435 \u043e\u0431\u043c\u0435\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("FSWindow", u"\u042f\u0437\u044b\u043a\u0438 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f:", None))
        self.upLang.setText(QCoreApplication.translate("FSWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.downLang.setText(QCoreApplication.translate("FSWindow", u"\u0412\u043d\u0438\u0437", None))
        self.copyToClipboard.setText(QCoreApplication.translate("FSWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430 \u043f\u043e\u0441\u043b\u0435 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f", None))
        self.searchInWeb.setText(QCoreApplication.translate("FSWindow", u"\u041f\u043e\u0438\u0441\u043a \u0432 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0435 \u043f\u043e\u0441\u043b\u0435 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f", None))
        self.searchEngine.setItemText(0, QCoreApplication.translate("FSWindow", u"\u042f\u043d\u0434\u0435\u043a\u0441", None))
        self.searchEngine.setItemText(1, QCoreApplication.translate("FSWindow", u"Google", None))

        self.savedRecordsBtn.setText(QCoreApplication.translate("FSWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
    # retranslateUi

