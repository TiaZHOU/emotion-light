# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startpage.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import interface.pictures_rc

class Ui_StartPage(object):
    def setupUi(self, StartPage):
        if not StartPage.objectName():
            StartPage.setObjectName(u"StartPage")
        StartPage.resize(800, 600)
        StartPage.setStyleSheet(u"background-color: rgb(111, 112, 112);")
        self.centralwidget = QWidget(StartPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(460, -60, 341, 671))
        self.picture.setStyleSheet(u"color: rgba(92, 92, 92, 128);")
        self.picture.setPixmap(QPixmap(u":/pictures/face.jpg"))
        self.picture.setScaledContents(True)
        self.emotionlight = QLabel(self.centralwidget)
        self.emotionlight.setObjectName(u"emotionlight")
        self.emotionlight.setGeometry(QRect(100, 100, 261, 51))
        self.emotionlight.setStyleSheet(u"font: 36pt \"Copperplate\";")
        self.started = QPushButton(self.centralwidget)
        self.started.setObjectName(u"started")
        self.started.setGeometry(QRect(170, 220, 112, 41))
        self.started.setStyleSheet(u"QPushButton {color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}")
        self.instruction = QLabel(self.centralwidget)
        self.instruction.setObjectName(u"instruction")
        self.instruction.setGeometry(QRect(0, 380, 461, 121))
        self.instruction.setPixmap(QPixmap(u":/pictures/instruction.png"))
        self.instruction.setScaledContents(True)
        StartPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartPage)

        QMetaObject.connectSlotsByName(StartPage)
    # setupUi

    def retranslateUi(self, StartPage):
        StartPage.setWindowTitle(QCoreApplication.translate("StartPage", u"Emotion Light", None))
        self.picture.setText("")
        self.emotionlight.setText(QCoreApplication.translate("StartPage", u"Emotion Light", None))
        self.started.setText(QCoreApplication.translate("StartPage", u"Get Started", None))
        self.instruction.setText("")
    # retranslateUi

