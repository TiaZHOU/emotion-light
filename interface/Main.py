from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import json
import cv2 as cv
import numpy as np
import sys
from startpage import Ui_StartPage
from readCamera import MainApp
from lightColorDashboard import Ui_lightColor
from color_mapping  import generate


class mainWindow(QMainWindow, Ui_StartPage):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class cameraWindow(MainApp):

    def __init__(self):
        QWidget.__init__(self)
        self.video_size = QSize(800, 500)
        self.setup_ui()
        self.setup_camera()

    def capturePicture(self):
        # Click the 'Start Recording" button
        # The Azure camera should be connected and capture pictures and save them into a file
        pass

    def uploadPicture(self):
        # Click the 'Upload" button
        # The pictures will be uploaded and processed by emotion recognition to generate results with level
        # The dashboard should be activated
        pass

class colorDashboard(QMainWindow, Ui_lightColor):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.finishButton.clicked.connect(self.finishEditing)
        #self.previewButton.clicked.connect(self.previewLight)

    def happyColor(self):
        # The color selected for each emotion will be transmitted in the format of RGB
        global happy
        if self.happyRed.isChecked():
            happy = 1
        elif self.happyOrange.isChecked():
            happy = 2
        elif self.happyYellow.isChecked():
            happy = 3
        elif self.happyGreen.isChecked():
            happy = 4
        elif self.happySky.isChecked():
            happy = 5
        elif self.happyBlue.isChecked():
            happy = 6
        elif self.happyIndigo.isChecked():
            happy = 7
        elif self.happyPurple.isChecked():
            happy = 8
        else:
            pass

    def surprisedColor(self):
        global surprised
        if self.surprisedRed.isChecked():
            surprised = 1
        elif self.surprisedOrange.isChecked():
            surprised = 2
        elif self.surprisedYellow.isChecked():
            surprised = 3
        elif self.surprisedGreen.isChecked():
            surprised = 4
        elif self.surprisedSky.isChecked():
            surprised = 5
        elif self.surprisedBlue.isChecked():
            surprised = 6
        elif self.surprisedndigo.isChecked():
            surprised = 7
        elif self.surprisedPurple.isChecked():
            surprised = 8
        else:
            pass

    def neutralColor(self):
        global neutral
        if self.neutralRed.isChecked():
            neutral = 1
        elif self.neutralOrange.isChecked():
            neutral = 2
        elif self.neutralYellow.isChecked():
            neutral = 3
        elif self.neutralGreen.isChecked():
            neutral = 4
        elif self.neutralSky.isChecked():
            neutral = 5
        elif self.neutralBlue.isChecked():
            neutral = 6
        elif self.neutralndigo.isChecked():
            neutral = 7
        elif self.neutralPurple.isChecked():
            neutral = 8
        else:
            pass

    def sadColor(self):
        global sad
        if self.sadRed.isChecked():
            sad = 1
        elif self.sadOrange.isChecked():
            sad = 2
        elif self.sadYellow.isChecked():
            sad = 3
        elif self.sadGreen.isChecked():
            sad = 4
        elif self.sadSky.isChecked():
            sad = 5
        elif self.sadBlue.isChecked():
            sad = 6
        elif self.sadIndigo.isChecked():
            sad = 7
        elif self.sadPurple.isChecked():
            sad = 8
        else:
            pass

    def contemptColor(self):
        global contempt
        if self.contemptRed.isChecked():
            contempt = 1
        elif self.contemptOrange.isChecked():
            contempt = 2
        elif self.contemptYellow.isChecked():
            contempt = 3
        elif self.contemptGreen.isChecked():
            contempt = 4
        elif self.contemptSky.isChecked():
            contempt = 5
        elif self.contemptBlue.isChecked():
            contempt = 6
        elif self.contemptIndigo.isChecked():
            contempt = 7
        elif self.contemptPurple.isChecked():
            contempt = 8
        else:
            pass

    def angerColor(self):
        global anger
        if self.angerRed.isChecked():
            anger = 1
        elif self.angerOrange.isChecked():
            anger = 2
        elif self.angerYellow.isChecked():
            anger = 3
        elif self.angerGreen.isChecked():
            anger = 4
        elif self.angerSky.isChecked():
            anger = 5
        elif self.angerBlue.isChecked():
            anger = 6
        elif self.angerIndigo.isChecked():
            anger = 7
        elif self.angerPurple.isChecked():
            anger = 8
        else:
            pass

    def fearColor(self):
        global fear
        if self.fearRed.isChecked():
            fear = 1
        elif self.fearOrange.isChecked():
            fear = 2
        elif self.fearYellow.isChecked():
            fear = 3
        elif self.fearGreen.isChecked():
            fear = 4
        elif self.fearSky.isChecked():
            fear = 5
        elif self.fearBlue.isChecked():
            fear = 6
        elif self.fearIndigo.isChecked():
            fear = 7
        elif self.fearPurple.isChecked():
            fear = 8
        else:
            pass

    def disgustColor(self):
        global disgust
        if self.disgustRed.isChecked():
            disgust = 1
        elif self.disgustOrange.isChecked():
            disgust = 2
        elif self.disgustYellow.isChecked():
            disgust = 3
        elif self.disgustGreen.isChecked():
            disgust = 4
        elif self.disgustSky.isChecked():
            disgust = 5
        elif self.disgustBlue.isChecked():
            disgust = 6
        elif self.disgustIndigo.isChecked():
            disgust = 7
        elif self.disgustPurple.isChecked():
            disgust = 8
        else:
            pass

    def emotionBright(self):
        # The brightness will be adjusted through sliders and the value should be divided by 100 as percentage
        global happyBright, surprisedBright, neutralBright, sadBright, contemptBright, angerBright, fearBright, disgustBright
        happyBright = self.happySlider.value()/100
        surprisedBright = self.surprisedSlider.value()/100
        neutralBright = self.neutralSlider.value()/100
        sadBright = self.sadSlider.value()/100
        contemptBright = self.contemptSlider.value()/100
        angerBright = self.angerSlider.value()/100
        fearBright = self.fearSlider.value()/100
        disgustBright = self.disgustSlider.value()/100

    def playSpeed(self):
        # The range of value on slider is from 100 to 1000, set as times speed
        global speedValue
        speedValue = self.speedSlider.value()

    def previewLight(self):
        # main begin
        pictureGenerate = generate()
        model = [1, 2, 3, 4, 4, 4, 7, 1]  # initial color model, numbers refer to colors, positions refer to emotions
        saturate = [0.49, 1, 0.08, 1, 0.27, 1, 0.12, 0.9]
        speed = 10
        # colors explain
        '''
        pos 0   "anger"         num 0   "red"
        pos 1   "contempt"      num 1   "orange"
        pos 2   "disgust"       num 2   "yellow"
        pos 3   "fear"          num 3   "green"
        pos 4   "happiness"     num 4   "cyan"
        pos 5   "neutral"       num 5   "blue"
        pos 6   "sadness"       num 6   "purple"
        pos 7   "surprise"      num 7   "white"
        '''

        emotion = generate.read_emotion(saturate)
        # emotion = set_saturate(saturate, emotion)
        # print(emotion)
        color_list = generate.max_two_emo(emotion)
        # print(color_list)

        # simulate user change color3 to emotion5
        # TODO set color change API for interface
        # color_change(model, 3, 5)

        # generate two pic then merge on weight
        #
        output = [[0 for i in range(4)] for i in range(len(color_list))]
        display = [0 for i in range(len(color_list))]
        for i in range(len(color_list)):
            img1 = generate.color_pick(pictureGenerate, model[color_list[i][0]])
            img2 = generate.color_pick(pictureGenerate, model[color_list[i][1]])
            # TODO the add should more sensitive because many neutral
            clA = cv.addWeighted(img1, emotion[i][color_list[i][0]], img2, emotion[i][color_list[i][1]], 0)
            # cv.imshow('clA', clA)
            # cv.waitKey(0)
            output[i][0] = int(clA[0][0][0].astype(str))
            output[i][1] = int(clA[0][0][1].astype(str))
            output[i][2] = int(clA[0][0][2].astype(str))
            output[i][3] = int(1000 / speed)
            print(output[i])  # final result RGB code
            # display[i] = create_image(r=clA[i][0][0], g=clA[i][0][1], b=clA[i][0][2])
            # ser = serial.Serial("COM5", 9600, timeout=5)
        # TODO transfer the result into Arduino kit
        size = len(output)
        pictureGenerate.preview(output, size)
        # store(output)
        # number info
        '''
        color_list[0][0]  # pos 5 in first pic, refer to neutral
        color_list[0][1]  # pos 6 in first pic, refer to sadness

        model[color_list[0][0]] # num 5 refer color5
        model[color_list[0][1]] # num 6 refer color6
        '''

        # display testing code
        '''
        cl11 = color_pick(model[color_list[0][0]])  
        cl12 = color_pick(model[color_list[0][1]])
        cl21 = color_pick(model[color_list[1][0]])
        cl22 = color_pick(model[color_list[1][1]])

        clA = cv.addWeighted(cl11, emotion[0][color_list[0][0]], cl12, emotion[0][color_list[0][1]], 0)
        clB = cv.addWeighted(cl21, emotion[1][color_list[1][0]], cl22, emotion[1][color_list[1][1]], 0)
        # print(clA[0][0])
        # print(clB[0][0])
        cv.imshow('clA', clA)
        cv.imshow('clB', clB)
        cv.waitKey(0)
        '''

    def finishEditing(self):
        # Click 'Finish' button to upload the parameters, meanwhile opening dialog to indicate upload successfully
        print(happy, surprised, neutral, sad, contempt, anger, fear, disgust)
        print(happyBright, surprisedBright, neutralBright, sadBright, contemptBright, angerBright, fearBright,
              disgustBright)
        print(speedValue)

class successDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Upload Successfully")
        self.resize(300, 200)

        self.result = QLabel("Uploading successfully! You may see the light!")
        homeButton = QPushButton("HOME")
        exitButton = QPushButton("QUIT")

        homeButton.setStyleSheet(u"QPushButton {color: #333;\n"
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
        exitButton.setStyleSheet(u"QPushButton {color: #333;\n"
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

        layout = QGridLayout()
        layout.addWidget(self.result, 0, 0, 1, -1)
        layout.addWidget(homeButton, 1, 0, -1, 1)
        layout.addWidget(exitButton, 1, 1, -1, 1)

        self.setLayout(layout)

        homeButton.clicked.connect(form.show)
        homeButton.clicked.connect(dashboard.close)
        homeButton.clicked.connect(self.close)
        exitButton.clicked.connect(exit)

class previewDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Preview")
        self.resize(300, 200)

        image = QPixmap('imageGenerated.jpg')
        self.progress = QLabel()
        self.progress.setPixmap(image)

        backButton = QPushButton("Back")

        backButton.setStyleSheet(u"QPushButton {color: #333;\n"
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

        layout = QVBoxLayout()
        layout.addWidget(self.progress)
        layout.addWidget(backButton)

        self.setLayout(layout)
        backButton.clicked.connect(self.close)

app = QApplication(sys.argv)
form=mainWindow()
form.show()

camera = cameraWindow()
form.started.clicked.connect(camera.show)
form.started.clicked.connect(form.close)

dashboard = colorDashboard()
camera.Upload.clicked.connect(dashboard.show)
camera.Upload.clicked.connect(camera.close)

dashboard.happyRed.clicked.connect(dashboard.happyColor)
dashboard.happyYellow.clicked.connect(dashboard.happyColor)
dashboard.happyOrange.clicked.connect(dashboard.happyColor)
dashboard.happyGreen.clicked.connect(dashboard.happyColor)
dashboard.happySky.clicked.connect(dashboard.happyColor)
dashboard.happyBlue.clicked.connect(dashboard.happyColor)
dashboard.happyIndigo.clicked.connect(dashboard.happyColor)
dashboard.happyPurple.clicked.connect(dashboard.happyColor)

dashboard.surprisedRed.clicked.connect(dashboard.surprisedColor)
dashboard.surprisedYellow.clicked.connect(dashboard.surprisedColor)
dashboard.surprisedOrange.clicked.connect(dashboard.surprisedColor)
dashboard.surprisedGreen.clicked.connect(dashboard.surprisedColor)
dashboard.surprisedSky.clicked.connect(dashboard.surprisedColor)
dashboard.surprisedBlue.clicked.connect(dashboard.surprisedColor)
dashboard.surprisedndigo.clicked.connect(dashboard.surprisedColor)
dashboard.surprisedPurple.clicked.connect(dashboard.surprisedColor)

dashboard.neutralRed.clicked.connect(dashboard.neutralColor)
dashboard.neutralOrange.clicked.connect(dashboard.neutralColor)
dashboard.neutralYellow.clicked.connect(dashboard.neutralColor)
dashboard.neutralGreen.clicked.connect(dashboard.neutralColor)
dashboard.neutralSky.clicked.connect(dashboard.neutralColor)
dashboard.neutralBlue.clicked.connect(dashboard.neutralColor)
dashboard.neutralndigo.clicked.connect(dashboard.neutralColor)
dashboard.neutralPurple.clicked.connect(dashboard.neutralColor)

dashboard.sadRed.clicked.connect(dashboard.sadColor)
dashboard.sadOrange.clicked.connect(dashboard.sadColor)
dashboard.sadYellow.clicked.connect(dashboard.sadColor)
dashboard.sadGreen.clicked.connect(dashboard.sadColor)
dashboard.sadSky.clicked.connect(dashboard.sadColor)
dashboard.sadBlue.clicked.connect(dashboard.sadColor)
dashboard.sadIndigo.clicked.connect(dashboard.sadColor)
dashboard.sadPurple.clicked.connect(dashboard.sadColor)

dashboard.contemptRed.clicked.connect(dashboard.contemptColor)
dashboard.contemptOrange.clicked.connect(dashboard.contemptColor)
dashboard.contemptYellow.clicked.connect(dashboard.contemptColor)
dashboard.contemptGreen.clicked.connect(dashboard.contemptColor)
dashboard.contemptSky.clicked.connect(dashboard.contemptColor)
dashboard.contemptBlue.clicked.connect(dashboard.contemptColor)
dashboard.contemptIndigo.clicked.connect(dashboard.contemptColor)
dashboard.contemptPurple.clicked.connect(dashboard.contemptColor)

dashboard.angerRed.clicked.connect(dashboard.angerColor)
dashboard.angerOrange.clicked.connect(dashboard.angerColor)
dashboard.angerYellow.clicked.connect(dashboard.angerColor)
dashboard.angerGreen.clicked.connect(dashboard.angerColor)
dashboard.angerSky.clicked.connect(dashboard.angerColor)
dashboard.angerIndigo.clicked.connect(dashboard.angerColor)
dashboard.angerBlue.clicked.connect(dashboard.angerColor)
dashboard.angerPurple.clicked.connect(dashboard.angerColor)

dashboard.fearRed.clicked.connect(dashboard.fearColor)
dashboard.fearOrange.clicked.connect(dashboard.fearColor)
dashboard.fearYellow.clicked.connect(dashboard.fearColor)
dashboard.fearGreen.clicked.connect(dashboard.fearColor)
dashboard.fearSky.clicked.connect(dashboard.fearColor)
dashboard.fearBlue.clicked.connect(dashboard.fearColor)
dashboard.fearIndigo.clicked.connect(dashboard.fearColor)
dashboard.fearPurple.clicked.connect(dashboard.fearColor)

dashboard.disgustRed.clicked.connect(dashboard.disgustColor)
dashboard.disgustOrange.clicked.connect(dashboard.disgustColor)
dashboard.disgustYellow.clicked.connect(dashboard.disgustColor)
dashboard.disgustGreen.clicked.connect(dashboard.disgustColor)
dashboard.disgustSky.clicked.connect(dashboard.disgustColor)
dashboard.disgustBlue.clicked.connect(dashboard.disgustColor)
dashboard.disgustIndigo.clicked.connect(dashboard.disgustColor)
dashboard.disgustPurple.clicked.connect(dashboard.disgustColor)

dashboard.happySlider.sliderReleased.connect(dashboard.emotionBright)
dashboard.surprisedSlider.sliderReleased.connect(dashboard.emotionBright)
dashboard.neutralSlider.sliderReleased.connect(dashboard.emotionBright)
dashboard.sadSlider.sliderReleased.connect(dashboard.emotionBright)
dashboard.contemptSlider.sliderReleased.connect(dashboard.emotionBright)
dashboard.angerSlider.sliderReleased.connect(dashboard.emotionBright)
dashboard.fearSlider.sliderReleased.connect(dashboard.emotionBright)
dashboard.disgustSlider.sliderReleased.connect(dashboard.emotionBright)

dashboard.speedSlider.sliderReleased.connect(dashboard.playSpeed)

status = successDialog()
dashboard.finishButton.clicked.connect(status.show)

preview = previewDialog()

dashboard.speedSlider.sliderReleased.connect(dashboard.previewLight)
dashboard.previewButton.clicked.connect(preview.show)

app.exec_()
