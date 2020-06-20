# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lightColorDashboard.ui'
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


class Ui_lightColor(object):
    def setupUi(self, lightColor):
        if not lightColor.objectName():
            lightColor.setObjectName(u"lightColor")
        lightColor.resize(800, 600)
        lightColor.setStyleSheet(u"background-color: rgb(111, 112, 112);")
        self.centralwidget = QWidget(lightColor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(250, 10, 301, 61))
        self.title.setStyleSheet(u"font: 36pt \"Copperplate\";\n"
"")
        self.happy = QLabel(self.centralwidget)
        self.happy.setObjectName(u"happy")
        self.happy.setGeometry(QRect(20, 90, 58, 16))
        self.happyRed = QPushButton(self.centralwidget)
        self.happyRed.setObjectName(u"happyRed")
        self.happyRed.setGeometry(QRect(20, 120, 10, 10))
        self.happyRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"\n"
"")
        self.happyRed.setCheckable(True)
        #self.happyRed.setChecked(False)
        self.happyOrange = QPushButton(self.centralwidget)
        self.happyOrange.setObjectName(u"happyOrange")
        self.happyOrange.setGeometry(QRect(40, 120, 10, 10))
        self.happyOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.happyOrange.setCheckable(True)
        self.happyYellow = QPushButton(self.centralwidget)
        self.happyYellow.setObjectName(u"happyYellow")
        self.happyYellow.setGeometry(QRect(60, 120, 10, 10))
        self.happyYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.happyYellow.setCheckable(True)
        self.happyGreen = QPushButton(self.centralwidget)
        self.happyGreen.setObjectName(u"happyGreen")
        self.happyGreen.setGeometry(QRect(80, 120, 10, 10))
        self.happyGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.happyGreen.setCheckable(True)
        self.happyBlue = QPushButton(self.centralwidget)
        self.happyBlue.setObjectName(u"happyBlue")
        self.happyBlue.setGeometry(QRect(120, 120, 10, 10))
        self.happyBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.happyBlue.setCheckable(True)
        self.happyIndigo = QPushButton(self.centralwidget)
        self.happyIndigo.setObjectName(u"happyIndigo")
        self.happyIndigo.setGeometry(QRect(140, 120, 10, 10))
        self.happyIndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.happyIndigo.setCheckable(True)
        self.happyPurple = QPushButton(self.centralwidget)
        self.happyPurple.setObjectName(u"happyPurple")
        self.happyPurple.setGeometry(QRect(160, 120, 10, 10))
        self.happyPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.happyPurple.setCheckable(True)
        self.happySky = QPushButton(self.centralwidget)
        self.happySky.setObjectName(u"happySky")
        self.happySky.setGeometry(QRect(100, 120, 10, 10))
        self.happySky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.happySky.setCheckable(True)
        self.surprised = QLabel(self.centralwidget)
        self.surprised.setObjectName(u"surprised")
        self.surprised.setGeometry(QRect(210, 90, 81, 16))
        self.surprisedRed = QPushButton(self.centralwidget)
        self.surprisedRed.setObjectName(u"surprisedRed")
        self.surprisedRed.setGeometry(QRect(210, 120, 10, 10))
        self.surprisedRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"}\n"
"\n"
"")
        self.surprisedRed.setCheckable(True)
        self.surprisedOrange = QPushButton(self.centralwidget)
        self.surprisedOrange.setObjectName(u"surprisedOrange")
        self.surprisedOrange.setGeometry(QRect(230, 120, 10, 10))
        self.surprisedOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.surprisedOrange.setCheckable(True)
        self.surprisedYellow = QPushButton(self.centralwidget)
        self.surprisedYellow.setObjectName(u"surprisedYellow")
        self.surprisedYellow.setGeometry(QRect(250, 120, 10, 10))
        self.surprisedYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.surprisedYellow.setCheckable(True)
        self.surprisedGreen = QPushButton(self.centralwidget)
        self.surprisedGreen.setObjectName(u"surprisedGreen")
        self.surprisedGreen.setGeometry(QRect(270, 120, 10, 10))
        self.surprisedGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.surprisedGreen.setCheckable(True)
        self.surprisedSky = QPushButton(self.centralwidget)
        self.surprisedSky.setObjectName(u"surprisedSky")
        self.surprisedSky.setGeometry(QRect(290, 120, 10, 10))
        self.surprisedSky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.surprisedSky.setCheckable(True)
        self.surprisedBlue = QPushButton(self.centralwidget)
        self.surprisedBlue.setObjectName(u"surprisedBlue")
        self.surprisedBlue.setGeometry(QRect(310, 120, 10, 10))
        self.surprisedBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.surprisedBlue.setCheckable(True)
        self.surprisedndigo = QPushButton(self.centralwidget)
        self.surprisedndigo.setObjectName(u"surprisedndigo")
        self.surprisedndigo.setGeometry(QRect(330, 120, 10, 10))
        self.surprisedndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.surprisedndigo.setCheckable(True)
        self.surprisedPurple = QPushButton(self.centralwidget)
        self.surprisedPurple.setObjectName(u"surprisedPurple")
        self.surprisedPurple.setGeometry(QRect(350, 120, 10, 10))
        self.surprisedPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.surprisedPurple.setCheckable(True)
        self.neutral = QLabel(self.centralwidget)
        self.neutral.setObjectName(u"neutral")
        self.neutral.setGeometry(QRect(400, 90, 81, 16))
        self.neutralRed = QPushButton(self.centralwidget)
        self.neutralRed.setObjectName(u"neutralRed")
        self.neutralRed.setGeometry(QRect(400, 120, 10, 10))
        self.neutralRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"}\n"
"\n"
"")
        self.neutralRed.setCheckable(True)
        self.neutralOrange = QPushButton(self.centralwidget)
        self.neutralOrange.setObjectName(u"neutralOrange")
        self.neutralOrange.setGeometry(QRect(420, 120, 10, 10))
        self.neutralOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.neutralOrange.setCheckable(True)
        self.neutralYellow = QPushButton(self.centralwidget)
        self.neutralYellow.setObjectName(u"neutralYellow")
        self.neutralYellow.setGeometry(QRect(440, 120, 10, 10))
        self.neutralYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.neutralYellow.setCheckable(True)
        self.neutralGreen = QPushButton(self.centralwidget)
        self.neutralGreen.setObjectName(u"neutralGreen")
        self.neutralGreen.setGeometry(QRect(460, 120, 10, 10))
        self.neutralGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.neutralGreen.setCheckable(True)
        self.neutralSky = QPushButton(self.centralwidget)
        self.neutralSky.setObjectName(u"neutralSky")
        self.neutralSky.setGeometry(QRect(480, 120, 10, 10))
        self.neutralSky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.neutralSky.setCheckable(True)
        self.neutralBlue = QPushButton(self.centralwidget)
        self.neutralBlue.setObjectName(u"neutralBlue")
        self.neutralBlue.setGeometry(QRect(500, 120, 10, 10))
        self.neutralBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.neutralBlue.setCheckable(True)
        self.neutralndigo = QPushButton(self.centralwidget)
        self.neutralndigo.setObjectName(u"neutralndigo")
        self.neutralndigo.setGeometry(QRect(520, 120, 10, 10))
        self.neutralndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.neutralndigo.setCheckable(True)
        self.neutralPurple = QPushButton(self.centralwidget)
        self.neutralPurple.setObjectName(u"neutralPurple")
        self.neutralPurple.setGeometry(QRect(540, 120, 10, 10))
        self.neutralPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.neutralPurple.setCheckable(True)
        self.sad = QLabel(self.centralwidget)
        self.sad.setObjectName(u"sad")
        self.sad.setGeometry(QRect(590, 90, 81, 16))
        self.sadRed = QPushButton(self.centralwidget)
        self.sadRed.setObjectName(u"sadRed")
        self.sadRed.setGeometry(QRect(590, 120, 10, 10))
        self.sadRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"}\n"
"\n"
"")
        self.sadRed.setCheckable(True)
        self.sadOrange = QPushButton(self.centralwidget)
        self.sadOrange.setObjectName(u"sadOrange")
        self.sadOrange.setGeometry(QRect(610, 120, 10, 10))
        self.sadOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.sadOrange.setCheckable(True)
        self.sadYellow = QPushButton(self.centralwidget)
        self.sadYellow.setObjectName(u"sadYellow")
        self.sadYellow.setGeometry(QRect(630, 120, 10, 10))
        self.sadYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.sadYellow.setCheckable(True)
        self.sadGreen = QPushButton(self.centralwidget)
        self.sadGreen.setObjectName(u"sadGreen")
        self.sadGreen.setGeometry(QRect(650, 120, 10, 10))
        self.sadGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.sadGreen.setCheckable(True)
        self.sadSky = QPushButton(self.centralwidget)
        self.sadSky.setObjectName(u"sadSky")
        self.sadSky.setGeometry(QRect(670, 120, 10, 10))
        self.sadSky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.sadSky.setCheckable(True)
        self.sadBlue = QPushButton(self.centralwidget)
        self.sadBlue.setObjectName(u"sadBlue")
        self.sadBlue.setGeometry(QRect(690, 120, 10, 10))
        self.sadBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.sadBlue.setCheckable(True)
        self.sadIndigo = QPushButton(self.centralwidget)
        self.sadIndigo.setObjectName(u"sadIndigo")
        self.sadIndigo.setGeometry(QRect(710, 120, 10, 10))
        self.sadIndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.sadIndigo.setCheckable(True)
        self.sadPurple = QPushButton(self.centralwidget)
        self.sadPurple.setObjectName(u"sadPurple")
        self.sadPurple.setGeometry(QRect(730, 120, 10, 10))
        self.sadPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.sadPurple.setCheckable(True)
        self.contemptYellow = QPushButton(self.centralwidget)
        self.contemptYellow.setObjectName(u"contemptYellow")
        self.contemptYellow.setGeometry(QRect(60, 240, 10, 10))
        self.contemptYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.contemptYellow.setCheckable(True)
        self.contemptIndigo = QPushButton(self.centralwidget)
        self.contemptIndigo.setObjectName(u"contemptIndigo")
        self.contemptIndigo.setGeometry(QRect(140, 240, 10, 10))
        self.contemptIndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.contemptIndigo.setCheckable(True)
        self.contemptOrange = QPushButton(self.centralwidget)
        self.contemptOrange.setObjectName(u"contemptOrange")
        self.contemptOrange.setGeometry(QRect(40, 240, 10, 10))
        self.contemptOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.contemptOrange.setCheckable(True)
        self.contemptGreen = QPushButton(self.centralwidget)
        self.contemptGreen.setObjectName(u"contemptGreen")
        self.contemptGreen.setGeometry(QRect(80, 240, 10, 10))
        self.contemptGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.contemptGreen.setCheckable(True)
        self.contemptPurple = QPushButton(self.centralwidget)
        self.contemptPurple.setObjectName(u"contemptPurple")
        self.contemptPurple.setGeometry(QRect(160, 240, 10, 10))
        self.contemptPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.contemptPurple.setCheckable(True)
        self.contemptBlue = QPushButton(self.centralwidget)
        self.contemptBlue.setObjectName(u"contemptBlue")
        self.contemptBlue.setGeometry(QRect(120, 240, 10, 10))
        self.contemptBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.contemptBlue.setCheckable(True)
        self.contemptSky = QPushButton(self.centralwidget)
        self.contemptSky.setObjectName(u"contemptSky")
        self.contemptSky.setGeometry(QRect(100, 240, 10, 10))
        self.contemptSky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.contemptSky.setCheckable(True)
        self.contemptRed = QPushButton(self.centralwidget)
        self.contemptRed.setObjectName(u"contemptRed")
        self.contemptRed.setGeometry(QRect(20, 240, 10, 10))
        self.contemptRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"}\n"
"\n"
"")
        self.contemptRed.setCheckable(True)
        self.contempt = QLabel(self.centralwidget)
        self.contempt.setObjectName(u"contempt")
        self.contempt.setGeometry(QRect(20, 210, 81, 16))
        self.angerYellow = QPushButton(self.centralwidget)
        self.angerYellow.setObjectName(u"angerYellow")
        self.angerYellow.setGeometry(QRect(250, 240, 10, 10))
        self.angerYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.angerYellow.setCheckable(True)
        self.angerIndigo = QPushButton(self.centralwidget)
        self.angerIndigo.setObjectName(u"angerIndigo")
        self.angerIndigo.setGeometry(QRect(330, 240, 10, 10))
        self.angerIndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.angerIndigo.setCheckable(True)
        self.angerOrange = QPushButton(self.centralwidget)
        self.angerOrange.setObjectName(u"angerOrange")
        self.angerOrange.setGeometry(QRect(230, 240, 10, 10))
        self.angerOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.angerOrange.setCheckable(True)
        self.angerGreen = QPushButton(self.centralwidget)
        self.angerGreen.setObjectName(u"angerGreen")
        self.angerGreen.setGeometry(QRect(270, 240, 10, 10))
        self.angerGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.angerGreen.setCheckable(True)
        self.angerPurple = QPushButton(self.centralwidget)
        self.angerPurple.setObjectName(u"angerPurple")
        self.angerPurple.setGeometry(QRect(350, 240, 10, 10))
        self.angerPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.angerPurple.setCheckable(True)
        self.angerBlue = QPushButton(self.centralwidget)
        self.angerBlue.setObjectName(u"angerBlue")
        self.angerBlue.setGeometry(QRect(310, 240, 10, 10))
        self.angerBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.angerBlue.setCheckable(True)
        self.angerSky = QPushButton(self.centralwidget)
        self.angerSky.setObjectName(u"angerSky")
        self.angerSky.setGeometry(QRect(290, 240, 10, 10))
        self.angerSky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.angerSky.setCheckable(True)
        self.angerRed = QPushButton(self.centralwidget)
        self.angerRed.setObjectName(u"angerRed")
        self.angerRed.setGeometry(QRect(210, 240, 10, 10))
        self.angerRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"}\n"
"\n"
"")
        self.angerRed.setCheckable(True)
        self.anger = QLabel(self.centralwidget)
        self.anger.setObjectName(u"anger")
        self.anger.setGeometry(QRect(210, 210, 58, 16))
        self.fearYellow = QPushButton(self.centralwidget)
        self.fearYellow.setObjectName(u"fearYellow")
        self.fearYellow.setGeometry(QRect(440, 240, 10, 10))
        self.fearYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.fearYellow.setCheckable(True)
        self.fearIndigo = QPushButton(self.centralwidget)
        self.fearIndigo.setObjectName(u"fearIndigo")
        self.fearIndigo.setGeometry(QRect(520, 240, 10, 10))
        self.fearIndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.fearIndigo.setCheckable(True)
        self.fearOrange = QPushButton(self.centralwidget)
        self.fearOrange.setObjectName(u"fearOrange")
        self.fearOrange.setGeometry(QRect(420, 240, 10, 10))
        self.fearOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.fearOrange.setCheckable(True)
        self.fearGreen = QPushButton(self.centralwidget)
        self.fearGreen.setObjectName(u"fearGreen")
        self.fearGreen.setGeometry(QRect(460, 240, 10, 10))
        self.fearGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.fearGreen.setCheckable(True)
        self.fearPurple = QPushButton(self.centralwidget)
        self.fearPurple.setObjectName(u"fearPurple")
        self.fearPurple.setGeometry(QRect(540, 240, 10, 10))
        self.fearPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.fearPurple.setCheckable(True)
        self.fearBlue = QPushButton(self.centralwidget)
        self.fearBlue.setObjectName(u"fearBlue")
        self.fearBlue.setGeometry(QRect(500, 240, 10, 10))
        self.fearBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.fearBlue.setCheckable(True)
        self.fearSky = QPushButton(self.centralwidget)
        self.fearSky.setObjectName(u"fearSky")
        self.fearSky.setGeometry(QRect(480, 240, 10, 10))
        self.fearSky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.fearSky.setCheckable(True)
        self.fearRed = QPushButton(self.centralwidget)
        self.fearRed.setObjectName(u"fearRed")
        self.fearRed.setGeometry(QRect(400, 240, 10, 10))
        self.fearRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"}\n"
"\n"
"")
        self.fearRed.setCheckable(True)
        self.fear = QLabel(self.centralwidget)
        self.fear.setObjectName(u"fear")
        self.fear.setGeometry(QRect(400, 210, 58, 16))
        self.disgustYellow = QPushButton(self.centralwidget)
        self.disgustYellow.setObjectName(u"disgustYellow")
        self.disgustYellow.setGeometry(QRect(630, 240, 10, 10))
        self.disgustYellow.setStyleSheet(u"QPushButton {background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.disgustYellow.setCheckable(True)
        self.disgustIndigo = QPushButton(self.centralwidget)
        self.disgustIndigo.setObjectName(u"disgustIndigo")
        self.disgustIndigo.setGeometry(QRect(710, 240, 10, 10))
        self.disgustIndigo.setStyleSheet(u"QPushButton {background-color: rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(75, 0, 130);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(75, 0, 130);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.disgustIndigo.setCheckable(True)
        self.disgustOrange = QPushButton(self.centralwidget)
        self.disgustOrange.setObjectName(u"disgustOrange")
        self.disgustOrange.setGeometry(QRect(610, 240, 10, 10))
        self.disgustOrange.setStyleSheet(u"QPushButton {background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 165, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 165, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.disgustOrange.setCheckable(True)
        self.disgustGreen = QPushButton(self.centralwidget)
        self.disgustGreen.setObjectName(u"disgustGreen")
        self.disgustGreen.setGeometry(QRect(650, 240, 10, 10))
        self.disgustGreen.setStyleSheet(u"QPushButton {background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 255, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 255, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.disgustGreen.setCheckable(True)
        self.disgustPurple = QPushButton(self.centralwidget)
        self.disgustPurple.setObjectName(u"disgustPurple")
        self.disgustPurple.setGeometry(QRect(730, 240, 10, 10))
        self.disgustPurple.setStyleSheet(u"QPushButton {background-color: rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(128,0,128);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed ,\n"
"QPushButton:checked{\n"
"background-color:  rgb(128,0,128);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.disgustPurple.setCheckable(True)
        self.disgustBlue = QPushButton(self.centralwidget)
        self.disgustBlue.setObjectName(u"disgustBlue")
        self.disgustBlue.setGeometry(QRect(690, 240, 10, 10))
        self.disgustBlue.setStyleSheet(u"QPushButton {background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(0, 0, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(0, 0, 255);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.disgustBlue.setCheckable(True)
        self.disgustSky = QPushButton(self.centralwidget)
        self.disgustSky.setObjectName(u"disgustSky")
        self.disgustSky.setGeometry(QRect(670, 240, 10, 10))
        self.disgustSky.setStyleSheet(u"QPushButton {background-color: rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color:  rgb(135, 206, 235);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color:  rgb(135, 206, 235);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"}\n"
"")
        self.disgustSky.setCheckable(True)
        self.disgustRed = QPushButton(self.centralwidget)
        self.disgustRed.setObjectName(u"disgustRed")
        self.disgustRed.setGeometry(QRect(590, 240, 10, 10))
        self.disgustRed.setStyleSheet(u"QPushButton {background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 0, 0);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"background-color: rgb(255, 0, 0);\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:4px;\n"
" border-color: rgb(255, 255, 255);\n"
" max-width:8px;\n"
" max-height:8px;\n"
" min-width:8px;\n"
" min-height:8px;\n"
"\n"
"}\n"
"\n"
"")
        self.disgustRed.setCheckable(True)
        self.disgust = QLabel(self.centralwidget)
        self.disgust.setObjectName(u"disgust")
        self.disgust.setGeometry(QRect(590, 210, 58, 16))
        self.happySlider = QSlider(self.centralwidget)
        self.happySlider.setObjectName(u"happySlider")
        self.happySlider.setGeometry(QRect(10, 150, 160, 22))
        self.happySlider.setMaximum(100)
        self.happySlider.setOrientation(Qt.Horizontal)
        self.surprisedSlider = QSlider(self.centralwidget)
        self.surprisedSlider.setObjectName(u"surprisedSlider")
        self.surprisedSlider.setGeometry(QRect(200, 150, 160, 22))
        self.surprisedSlider.setMaximum(100)
        self.surprisedSlider.setOrientation(Qt.Horizontal)
        self.neutralSlider = QSlider(self.centralwidget)
        self.neutralSlider.setObjectName(u"neutralSlider")
        self.neutralSlider.setGeometry(QRect(390, 150, 160, 22))
        self.neutralSlider.setMaximum(100)
        self.neutralSlider.setOrientation(Qt.Horizontal)
        self.sadSlider = QSlider(self.centralwidget)
        self.sadSlider.setObjectName(u"sadSlider")
        self.sadSlider.setGeometry(QRect(580, 150, 160, 22))
        self.sadSlider.setMaximum(100)
        self.sadSlider.setOrientation(Qt.Horizontal)
        self.contemptSlider = QSlider(self.centralwidget)
        self.contemptSlider.setObjectName(u"contemptSlider")
        self.contemptSlider.setGeometry(QRect(10, 270, 160, 22))
        self.contemptSlider.setMaximum(100)
        self.contemptSlider.setOrientation(Qt.Horizontal)
        self.angerSlider = QSlider(self.centralwidget)
        self.angerSlider.setObjectName(u"angerSlider")
        self.angerSlider.setGeometry(QRect(200, 270, 160, 22))
        self.angerSlider.setMaximum(100)
        self.angerSlider.setOrientation(Qt.Horizontal)
        self.fearSlider = QSlider(self.centralwidget)
        self.fearSlider.setObjectName(u"fearSlider")
        self.fearSlider.setGeometry(QRect(390, 270, 160, 22))
        self.fearSlider.setMaximum(100)
        self.fearSlider.setOrientation(Qt.Horizontal)
        self.disgustSlider = QSlider(self.centralwidget)
        self.disgustSlider.setObjectName(u"disgustSlider")
        self.disgustSlider.setGeometry(QRect(580, 270, 160, 22))
        self.disgustSlider.setMaximum(100)
        self.disgustSlider.setOrientation(Qt.Horizontal)
        self.finishButton = QPushButton(self.centralwidget)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(300, 450, 112, 41))
        self.finishButton.resize(210,50)
        self.finishButton.setStyleSheet(u"QPushButton {color: #333;\n"
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

        lightColor.setCentralWidget(self.centralwidget)
        self.title.raise_()
        self.happy.raise_()
        self.happyRed.raise_()
        self.happyOrange.raise_()
        self.happyYellow.raise_()
        self.happyGreen.raise_()
        self.happyBlue.raise_()
        self.happyIndigo.raise_()
        self.happyPurple.raise_()
        self.happySky.raise_()
        self.surprised.raise_()
        self.surprisedRed.raise_()
        self.surprisedOrange.raise_()
        self.surprisedYellow.raise_()
        self.surprisedGreen.raise_()
        self.surprisedSky.raise_()
        self.surprisedBlue.raise_()
        self.surprisedndigo.raise_()
        self.surprisedPurple.raise_()
        self.neutral.raise_()
        self.neutralRed.raise_()
        self.neutralOrange.raise_()
        self.neutralYellow.raise_()
        self.neutralGreen.raise_()
        self.neutralSky.raise_()
        self.neutralBlue.raise_()
        self.neutralndigo.raise_()
        self.neutralPurple.raise_()
        self.sad.raise_()
        self.sadRed.raise_()
        self.sadOrange.raise_()
        self.sadYellow.raise_()
        self.sadGreen.raise_()
        self.sadSky.raise_()
        self.sadBlue.raise_()
        self.sadIndigo.raise_()
        self.sadPurple.raise_()
        self.contemptYellow.raise_()
        self.contemptIndigo.raise_()
        self.contemptOrange.raise_()
        self.contemptGreen.raise_()
        self.contemptPurple.raise_()
        self.contemptBlue.raise_()
        self.contemptSky.raise_()
        self.contemptRed.raise_()
        self.contempt.raise_()
        self.angerYellow.raise_()
        self.angerIndigo.raise_()
        self.angerOrange.raise_()
        self.angerGreen.raise_()
        self.angerPurple.raise_()
        self.angerBlue.raise_()
        self.angerSky.raise_()
        self.angerRed.raise_()
        self.anger.raise_()
        self.fearYellow.raise_()
        self.fearIndigo.raise_()
        self.fearOrange.raise_()
        self.fearGreen.raise_()
        self.fearPurple.raise_()
        self.fearBlue.raise_()
        self.fearSky.raise_()
        self.fearRed.raise_()
        self.fear.raise_()
        self.disgustYellow.raise_()
        self.disgustIndigo.raise_()
        self.disgustOrange.raise_()
        self.disgustGreen.raise_()
        self.disgustPurple.raise_()
        self.disgustBlue.raise_()
        self.disgustSky.raise_()
        self.disgustRed.raise_()
        self.disgust.raise_()
        self.happySlider.raise_()
        self.surprisedSlider.raise_()
        self.neutralSlider.raise_()
        self.sadSlider.raise_()
        self.contemptSlider.raise_()
        self.angerSlider.raise_()
        self.fearSlider.raise_()
        self.disgustSlider.raise_()
#        self.speedSlider.raise_()
 #       self.displaySpeed.raise_()
 #       self.previewButton.raise_()
        self.finishButton.raise_()

        self.retranslateUi(lightColor)
#        self.speedSlider.valueChanged.connect(self.label.setNum)

        QMetaObject.connectSlotsByName(lightColor)
    # setupUi

    def retranslateUi(self, lightColor):
        lightColor.setWindowTitle(QCoreApplication.translate("lightColor", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("lightColor", u"EMOTION LIGHT", None))
        self.happy.setText(QCoreApplication.translate("lightColor", u"HAPPY", None))
        self.happyRed.setText("")
        self.happyOrange.setText("")
        self.happyYellow.setText("")
        self.happyGreen.setText("")
        self.happyBlue.setText("")
        self.happyIndigo.setText("")
        self.happyPurple.setText("")
        self.happySky.setText("")
        self.surprised.setText(QCoreApplication.translate("lightColor", u"SURPRISED", None))
        self.surprisedRed.setText("")
        self.surprisedOrange.setText("")
        self.surprisedYellow.setText("")
        self.surprisedGreen.setText("")
        self.surprisedSky.setText("")
        self.surprisedBlue.setText("")
        self.surprisedndigo.setText("")
        self.surprisedPurple.setText("")
        self.neutral.setText(QCoreApplication.translate("lightColor", u"NEUTRAL", None))
        self.neutralRed.setText("")
        self.neutralOrange.setText("")
        self.neutralYellow.setText("")
        self.neutralGreen.setText("")
        self.neutralSky.setText("")
        self.neutralBlue.setText("")
        self.neutralndigo.setText("")
        self.neutralPurple.setText("")
        self.sad.setText(QCoreApplication.translate("lightColor", u"SAD", None))
        self.sadRed.setText("")
        self.sadOrange.setText("")
        self.sadYellow.setText("")
        self.sadGreen.setText("")
        self.sadSky.setText("")
        self.sadBlue.setText("")
        self.sadIndigo.setText("")
        self.sadPurple.setText("")
        self.contemptYellow.setText("")
        self.contemptIndigo.setText("")
        self.contemptOrange.setText("")
        self.contemptGreen.setText("")
        self.contemptPurple.setText("")
        self.contemptBlue.setText("")
        self.contemptSky.setText("")
        self.contemptRed.setText("")
        self.contempt.setText(QCoreApplication.translate("lightColor", u"CONTEMPT", None))
        self.angerYellow.setText("")
        self.angerIndigo.setText("")
        self.angerOrange.setText("")
        self.angerGreen.setText("")
        self.angerPurple.setText("")
        self.angerBlue.setText("")
        self.angerSky.setText("")
        self.angerRed.setText("")
        self.anger.setText(QCoreApplication.translate("lightColor", u"ANGER", None))
        self.fearYellow.setText("")
        self.fearIndigo.setText("")
        self.fearOrange.setText("")
        self.fearGreen.setText("")
        self.fearPurple.setText("")
        self.fearBlue.setText("")
        self.fearSky.setText("")
        self.fearRed.setText("")
        self.fear.setText(QCoreApplication.translate("lightColor", u"FEAR", None))
        self.disgustYellow.setText("")
        self.disgustIndigo.setText("")
        self.disgustOrange.setText("")
        self.disgustGreen.setText("")
        self.disgustPurple.setText("")
        self.disgustBlue.setText("")
        self.disgustSky.setText("")
        self.disgustRed.setText("")
        self.disgust.setText(QCoreApplication.translate("lightColor", u"DISGUST", None))
 #       self.displaySpeed.setText(QCoreApplication.translate("lightColor", u"DISPLAY SPEED", None))
 #      self.previewButton.setText(QCoreApplication.translate("lightColor", u"Open Light Projection Preview", None))
        self.finishButton.setText(QCoreApplication.translate("lightColor", u"Start Performance", None))
    # retranslateUi

