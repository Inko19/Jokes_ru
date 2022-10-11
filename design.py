# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)
import background_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(826, 397)
        MainWindow.setMinimumSize(QSize(826, 397))
        MainWindow.setMaximumSize(QSize(826, 397))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(13)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"QWidget {\n"
"	font-family: Rubik;\n"
"	font-size: 13pt;\n"
"	font-weight: 300;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	border-color: 2px solid rgba(255, 238, 0, 150);\n"
"\n"
"	font-size: 14pt;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(239, 239, 239, 100);\n"
"	border-color: 2px solid rgba(255, 238, 0, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"\n"
"	background-color: rgba(232, 232, 232, 100);\n"
"}\n"
"QPlainTextEdit{\n"
"	border-color: 2px solid rgba(255, 238, 0, 150);\n"
"}\n"
"\n"
"QWidget[objectName = \"centralwidget\"]{\n"
"	\n"
"	image: url(:/newPrefix/pngwing.com(3).png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font: 16px \"Rubic\";\n"
"color:rgba(0, 0, 0, 200);")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_3, 5, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_9, 5, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setIconSize(QSize(16, 16))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_10, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_7.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.plainTextEdit.setPlainText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0430\u043d\u0435\u043a\u0434\u043e\u0442\u043e\u0432", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e \u0440\u044b\u0431\u0430\u043b\u043a\u0443", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e \u0447\u0443\u043a\u0447\u0443", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e \u043d\u0430\u0440\u043a\u043e\u043c\u0430\u043d\u043e\u0432", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0443", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e \u043f\u0435\u043d\u0441\u0438\u043e\u043d\u0435\u0440\u043e\u0432", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e \u0428\u0442\u0438\u0440\u043b\u0438\u0446\u0430", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e \u041e\u0431\u0430\u043c\u0443", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e \u0423\u043a\u0440\u0430\u0438\u043d\u0443", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e \u041f\u0443\u0442\u0438\u043d\u0430", None))
    # retranslateUi

