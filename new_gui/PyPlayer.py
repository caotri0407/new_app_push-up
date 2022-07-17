
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,\
     QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
import cv2
from tkinter import Tk
# import keras
import time
# import PoseModule as pm


# Tk().withdraw()

# model_up = keras.models.load_model("models/eff_loss_up.h5")
# model_down = keras.models.load_model("models/eff_acc_down.h5")


# def preprocessing_image(img):
#     img = cv2.resize(img, dsize=(224, 224))
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = img.reshape(1, 224, 224, 3)
#     return img


# def preprocessing_image2(img):
#     img = cv2.resize(img, dsize=(336, 336))
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = img.reshape(1, 336, 336, 3)
#     return img


# test_img = cv2.imread("sample_images/img1.jpg")
# predict_test_image = preprocessing_image(test_img)
# model_up.predict(predict_test_image)
# model_down.predict(predict_test_image)
# play_thread = None
# count, no_right, no_wrong = 0, 0, 0
# fps = 0

# up_list, down_list = [], []

# angle_list, filter_list = [], []
# eval = False

# running = True
class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Resources/icon.ico"))
        self.setWindowTitle("App Push-up")
        self.setGeometry(350, 100, 750, 500) # Điều chỉnh tọa độ Text
        palet = self.palette() # set background
        palet.setColor(QPalette.Window, Qt.gray)
        self.setPalette(palet)
        self.createPlayerVideo()

    def createPlayerVideo(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoFrame = QVideoWidget()

        self.openButton = QPushButton("Open Video")
        self.openButton.clicked.connect(self.openFile)


        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.playVideo)


        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.webcamButton = QPushButton("Open Webcam")
        self.webcamButton.clicked.connect(self.playWebcam)

        hBox = QHBoxLayout()
        hBox.setContentsMargins(0, 0, 0, 0)
        hBox.addWidget(self.openButton)
        hBox.addWidget(self.webcamButton)
        hBox.addWidget(self.playButton)
        hBox.addWidget(self.slider)
        hBox.addWidget(self.webcamButton)
        vBox = QVBoxLayout()
        vBox.addWidget(videoFrame)
        vBox.addLayout(hBox)
        self.mediaPlayer.setVideoOutput(videoFrame)
        self.setLayout(vBox)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

    def openFile(self): # Xử lí file
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video File")
        if fileName != '':   # If fileName != null
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def playVideo(self): # Xử lí video
        # # global bg, running, btn_list
        # # global count, no_right, no_wrong, fps, up_list, down_list
        # # global angle_list, filter_list, eval

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        #     count, no_right, no_wrong = 0, 0, 0
        #     detector = pm.poseDetector()

        #     angle_list = [160]
        #     filter_list = [140]

        #     frame_count = 0
        #     frame_skip_rate = 6

        #     T = 50
        #     beta = 1 - frame_skip_rate / T

        #     high = True

        #     up_right = True
        #     no_right, no_wrong = 0, 0

        #     up_list = []
        #     down_list = []

        #     target_frame, target_angle = None, 0

        #     cap = cv2.VideoCapture()
        #     pTime = 0

        #     while running:
        #         success, org_frame = cap.read()
        #         if not success:
        #             break
        #         frame = detector.findPose(frame, draw=False)
        #         lmList = detector.findPosition(frame, draw=False)
        #         if lmList:
        #             # frame, _ = detector.findBoundingBox(frame, draw=True)
        #             if not detector.left():
        #                 cur_angle = detector.findAngle(frame, 12, 14, 16, draw=True)
        #             else:
        #                 cur_angle = detector.findAngle(frame, 11, 13, 15, draw=True)

        #             if (frame_count + 1) % frame_skip_rate == 0:
        #                 cur_angle = max(60, cur_angle)
        #                 angle_list.append(cur_angle)

        #                 if high and cur_angle > target_angle:
        #                     target_frame, target_angle = org_frame, cur_angle
        #                 if not high and cur_angle < target_angle:
        #                     target_frame, target_angle = org_frame, cur_angle

        #                 Fn = beta * filter_list[-1] + (1 - beta) * cur_angle
        #                 filter_list.append(Fn)

        #                 if high and Fn > cur_angle:
        #                     count += 0.5
        #                     high = False

        #                     predict_image = preprocessing_image(target_frame)
        #                     rate = model_up.predict(predict_image)[0][0]
        #                     if rate < 0.5:
        #                         up_right = True
        #                         print("up right")
        #                     else:
        #                         up_right = False
        #                         print("up wrong", rate)

        #                     up_list.append((target_frame, up_right, rate))

        #                     target_angle = 200

        #                 if not high and Fn < cur_angle:
        #                     count += 0.5
        #                     high = True

        #                     predict_image = preprocessing_image(target_frame)
        #                     rate = model_down.predict(predict_image)[0][0]
        #                     if rate < 0.5:
        #                         down_right = True
        #                         print("down right")
        #                     else:
        #                         down_right = False
        #                         print("down wrong", rate)

        #                     down_list.append((target_frame, down_right, rate))

        #                     if up_right and down_right:
        #                         no_right += 1
        #                     else:
        #                         no_wrong += 1

        #                     target_angle = 0

        #             frame_count += 1
        #         cTime = time.time()
        #         fps = 1 / (cTime - pTime)
        #         pTime = cTime
        #         cv2.waitKey(1)

        #     eval = True
        else:
            self.mediaPlayer.play()


    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState: # Khi video chạy thì hiển thị nút pause
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else: # ngược lại hiển thị nút play
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.slider.setValue(position)

    def durationChanged(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def playWebcam(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(1, 1080)
        self.cap.set(2, 860)
        while True:
            succees, img = self.cap.read()
            cv2.imshow("Webcam: ", img)
            if cv2.waitKey(10) & 0xFF == ord("q"):
                break
        self.cap.release()
        cv2.distroyAllWindows()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
