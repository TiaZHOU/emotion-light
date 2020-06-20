from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import cv2
from recognition.noStreamCapture import VideoGet


class MainApp(QWidget):

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, NoneType=None, *args, **kwargs):
        super().__init__(parent, PySide2_QtWidgets_QWidget=None, NoneType=None, *args, **kwargs)

    def setup_ui(self):
        """Initialize widgets.
        """
        self.isRecognitionOn = False
        self.setStyleSheet(u"background-color: rgb(111, 112, 112);")
        self.resize(800, 600)
        self.emotionlight = QLabel("Emotion Light")
        self.emotionlight.setObjectName(u"emotionlight")
        self.emotionlight.setGeometry(QRect(260, 10, 281, 61))
        self.emotionlight.setStyleSheet(u"font: 36pt \"Copperplate\";")

        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.startRecording = QPushButton("Start Emotion Recognition")
        self.startRecording.setObjectName(u"startRecording")
        self.startRecording.setGeometry(QRect(220, 530, 121, 41))
        self.startRecording.setStyleSheet(u"QPushButton {color: #333;\n"
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
        self.Upload = QPushButton("Stop Recognition And Go To Color Mapping Again")
        self.Upload.setEnabled(False)
        self.Upload.setObjectName(u"Upload")
        self.Upload.setGeometry(QRect(460, 530, 121, 41))
        self.Upload.setStyleSheet(u"QPushButton {color: #333;\n"
                                  "border: 2px solid #555;\n"
                                  "border-radius: 11px;\n"
                                  "padding: 5px;\n"
                                  "background: #333;\n"
                                  "fx: 2.3, fy: -2.4,\n"
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

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.emotionlight, 0, 0, 1, -1)
        self.main_layout.addWidget(self.image_label, 1, 0, 1, -1)
        self.main_layout.addWidget(self.startRecording,2, 0, -1, 1)
        self.main_layout.addWidget(self.Upload,2, 1, -1, 1)

        self.setLayout(self.main_layout)

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(image))

    def stopRecognition(self):
       return self.recognition.stop()


    def startRecognition(self):
        self.recognition = VideoGet(self.capture)
        self.recognition.start()