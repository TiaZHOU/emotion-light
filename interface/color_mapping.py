import json
import cv2 as cv
import numpy as np
import requests
import time

class generate:

    # store color results into .txt
    def store(data):
        file = open('displayList.txt', 'w')
        for ip in data:
            for i in ip:
                file.write(i)
                file.write(' ')
            file.write('\n')
        file.close()


    # load json data from file
    # read data from .json file from azure
    def read_emotion(saturate):
        with open('result', 'r') as f:
            data = json.load(f)
        # count how many face
        counter = 0
        for key in data:
            if key:
                counter = counter + 1
        # define lists for different emotions
        emotion = [[0 for i in range(8)] for i in range(counter)]
        for i in range(counter):
            emotion[i][0] = data[i]['faceAttributes']['emotion']['happiness'] * saturate[0]
            emotion[i][1] = data[i]['faceAttributes']['emotion']['surprise'] * saturate[1]
            emotion[i][2] = data[i]['faceAttributes']['emotion']['neutral'] * saturate[2]*0.1
            emotion[i][3] = data[i]['faceAttributes']['emotion']['sadness'] * saturate[3]
            emotion[i][4] = data[i]['faceAttributes']['emotion']['contempt'] * saturate[4]
            emotion[i][5] = data[i]['faceAttributes']['emotion']['anger'] * saturate[5]
            emotion[i][6] = data[i]['faceAttributes']['emotion']['fear'] * saturate[6]
            emotion[i][7] = data[i]['faceAttributes']['emotion']['disgust'] * saturate[7]
        print('total ' + counter.__str__() + ' pictures are send')
        return emotion
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


    # sample for color display
    def create_image(self, g, b, r):
        img = np.zeros([400, 400, 3], np.uint8)
        img[:, :, 0] = np.zeros([400, 400]) + b
        img[:, :, 1] = np.zeros([400, 400]) + g
        img[:, :, 2] = np.zeros([400, 400]) + r
        return img


    def color_pick(self, color_num):
        color0_red = self.create_image(r=255, g=0, b=0)
        color1_orange = self.create_image(r=255, g=165, b=0)
        color2_yellow = self.create_image(r=255, g=255, b=0)
        color3_green = self.create_image(r=0, g=255, b=0)
        color4_sky = self.create_image(r=135, g=206, b=235)
        color5_blue = self.create_image(r=0, g=0, b=255)
        color6_indigo = self.create_image(r=75, g=0, b=130)
        color7_purple = self.create_image(r=128, g=0, b=128)
        if color_num == 1:
            return color0_red
        elif color_num == 2:
            return color1_orange
        elif color_num == 3:
            return color2_yellow
        elif color_num == 4:
            return color3_green
        elif color_num == 5:
            return color4_sky
        elif color_num == 6:
            return color5_blue
        elif color_num == 7:
            return color6_indigo
        elif color_num == 8:
            return color7_purple


    # define function which user change color for specific emotion
    def color_change(formal_model, color, emo):
        formal_model[emo] = color
        return formal_model


    def set_saturate(saturate_list, emotion_list):
        for i in range(len(emotion_list)):
            emotion_list[i] = emotion_list[i] * saturate_list[i]
        return emotion_list


    def max_two_emo(emotion_result):
        set = [[0 for i in range(2)] for i in range(len(emotion_result))]
        for i in range(len(emotion_result)):
            counter = 0.0
            counter2 = 0.0
            set[i][0] = 0
            set[i][1] = 0
            for j in range(8):
                if emotion_result[i][j] > 0.0 and emotion_result[i][j] > counter:  # try for the 2nd large
                    set[i][1] = j
                    counter = emotion_result[i][j]
                if emotion_result[i][j] > counter2:  # try 1st large
                    set[i][0] = j
                    counter = 0  # clear 2nd large pos take before
                    counter2 = emotion_result[i][j]
        return set


    def preview(sel, output_list, size):
        pos = 0
        img = np.zeros((30, 200, 3), np.uint8)
        for i in range(size):
            ptStart = (pos, 00)
            ptEnd = (pos, 30)
            point_color = (output_list[i][0], output_list[i][1], output_list[i][2])  # BGR
            thickness = int(200/size)
            lineType = 5
            pos = pos + thickness
            cv.line(img, ptStart, ptEnd, point_color, thickness, lineType)
        #cv.namedWindow("image")
        #cv.imshow('image', img)
        cv.imwrite('imageGenerated.jpg', img)
        #cv.waitKey(0)

    def OutString(i):
        if i > 99:
            return str(i)
        if i < 10:
            return "00" + str()
        if i > 10 & i < 100:
            return "0" + str(i)


    def finalout(result):
        r = requests.get('http://10.0.0.33/W')
        time.sleep(0.1)
        r = requests.get('http://10.0.0.33/D')
        time.sleep(0.1)
        r = requests.get('http://10.0.0.33/W')
        url = "http://10.0.0.33/"
        finder = "_light"
        for i in range(len(result)):
            red = generate.OutString(result[i][2])
            green = generate.OutString(result[i][1])
            blue = generate.OutString(result[i][0])
            send = url + red + '_' + green + '_' + blue + finder
            r = requests.post(send)
            time.sleep(result[i][3] / 1000)
        r = requests(url+"000_000_000_light")



