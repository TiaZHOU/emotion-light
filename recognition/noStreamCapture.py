'''
1.  change Url in blink() and final_output() when network environment changed
2.  Check if requests lines are commented or not , they are commented sometime because saving testing time
3.  make sure default model.txt and saturate.txt exist in root lib before run.
    If they are not here, commenting those two method in class VideoGet and run once to generate
4.  change the API key in processInAzure() into yours if exist one down

'''


from threading import Thread
import cv2 as cv
import json
import numpy as np
import requests
import time

'''
this is the default for users who forget set something
'''
global model
model = [0, 1, 2, 3, 4, 5, 6, 7]
global saturate
saturate = [1, 1, 1, 1, 1, 1, 1, 1]

def read_model():
    model_r = open("model.txt", 'r')
    models = model_r.readlines()
    i = 0
    for mod in models:
        models[i] = int(mod)
        i =i+1
    model_r.close()
    return models

def read_saturate():
    sat_r = open("saturate.txt", 'r')
    saturates = sat_r.readlines()
    i =0
    for sat in saturates:
        saturates[i] = float(sat)
    sat_r.close()
    return saturates


def max_two_emo(emotion_result):
    set = [0 for i in range(2)]
    counter = 0.0
    counter2 = 0.0
    set[0] = 0
    set[1] = 0
    for j in range(8):
        if emotion_result[j] > 0.0 and emotion_result[j] > counter:  # try for the 2nd large
            set[1] = j
            counter = emotion_result[j]
        if emotion_result[j] > counter2:  # try 1st large
            set[0] = j
            counter = 0  # clear 2nd large pos take before
            counter2 = emotion_result[j]
    return set


def read_emotion(data, order, saturates):
    # count how many face
    # define lists for different emotions
    emotion = [0 for i in range(8)]
    i = order
    emotion[0] = data[i]['faceAttributes']['emotion']['happiness'] * saturates[0]
    emotion[1] = data[i]['faceAttributes']['emotion']['surprise'] * saturates[1]
    emotion[2] = data[i]['faceAttributes']['emotion']['neutral'] * saturates[2] * 0.5
    emotion[3] = data[i]['faceAttributes']['emotion']['sadness'] * saturates[3]
    emotion[4] = data[i]['faceAttributes']['emotion']['contempt'] * saturates[4]
    emotion[5] = data[i]['faceAttributes']['emotion']['anger'] * saturates[5]
    emotion[6] = data[i]['faceAttributes']['emotion']['fear'] * saturates[6]
    emotion[7] = data[i]['faceAttributes']['emotion']['disgust'] * saturates[7]
    #print('The' + order.__str__() + 'th pictures is send')
    return emotion


def create_image(g, b, r):
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.zeros([400, 400]) + b
    img[:, :, 1] = np.zeros([400, 400]) + g
    img[:, :, 2] = np.zeros([400, 400]) + r
    return img


def color_pick(color_num):
    color0_red = create_image(r=255, g=0, b=0)
    color1_orange = create_image(r=255, g=165, b=0)
    color2_yellow = create_image(r=255, g=255, b=0)
    color3_green = create_image(r=0, g=255, b=0)
    color4_sky = create_image(r=135, g=206, b=235)
    color5_blue = create_image(r=0, g=0, b=255)
    color6_indigo = create_image(r=75, g=0, b=130)
    color7_purple = create_image(r=128, g=0, b=128)
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


def output(emotion, model_list, c_list):
    result = [0 for i in range(3)]
    img1 = color_pick(model_list[list[0]])
    img2 = color_pick(model_list[list[1]])
    # TODO the add should more sensitive because many neutral
    clA = cv.addWeighted(img1, emotion[c_list[0]], img2, emotion[c_list[1]], 0)
    result[0] = int(clA[0][0][0].astype(str))
    result[1] = int(clA[0][0][1].astype(str))
    result[2] = int(clA[0][0][2].astype(str))

def blink():
    url = "http://192.168.43.24/"
    r = requests.get(url+'W')
    time.sleep(0.05)
    r = requests.get(url+'D')
    time.sleep(0.05)
    r = requests.get(url+'W')
    print("blink done")


def OuttoString(i):
    if i > 99:
        return str(i)
    if i < 10:
        return "00"+str()
    if i >10 & i <100:
        return "0"+str(i)

def final_output(result):
    url = "http://192.168.43.24/"
    finder = "_light"
    red = OuttoString(result[2])
    green = OuttoString(result[1])
    blue = OuttoString(result[0])
    send = url + red + '_' + green + '_' + blue + finder
    r = requests.post(send)
    print(send)

class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """
    model = read_model()
    saturate = read_saturate()
    def __init__(self, stream):
        self.stream = stream
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.collectedData = []

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        count = 0
        order = 0
        frame_number = 0
        samples_per_second = 10
        sample_rate = 30 / samples_per_second
        blink()
        while not self.stopped:
            ret, frame = self.stream.read()
            frame_number = frame_number + 1;
            if frame_number > sample_rate:
                output = frame.copy()
                self.processInAzure(output, self.collectedData)
                # print(self.collectedData)
                try:
                    emotion = read_emotion(self.collectedData, order, saturate)
                    #print(emotion)
                    color_list = max_two_emo(emotion)
                    #print(color_list)
                    order += 1
                except Exception:
                    print("color mapping exception")

                try:
                    result = [0 for i in range(3)]
                    img1 = color_pick(model[color_list[0]])
                    img2 = color_pick(model[color_list[1]])
                    clA = cv.addWeighted(img1, emotion[color_list[0]], img2, emotion[color_list[1]], 0)
                    result[0] = int(clA[0][0][0].astype(str))
                    result[1] = int(clA[0][0][1].astype(str))
                    result[2] = int(clA[0][0][2].astype(str))
                    time.sleep(0.5)
                    #print(result)
                    final_output(result)
                except Exception:
                    print("output exception")
                count += 100  # i.e. at 30 fps, this advances one second
                self.stream.set(1, count)
                frame_number = 0
            elif ret:
                a = 1 + 1
            else:
                self.stream.release()
                break

    def stop(self):
        print("Tried to stop")
        self.stopped = True
        # print(self.collectedData)
        return self.collectedData

    def processInAzure(self, image, collectedData):
        img = cv.imencode('.jpg', image)[1].tostring()
        subscription_key = "747a8208ff0f422499c5ecdc7c059551"
        # replace <My Endpoint String> with the string from your endpoint URL
        face_api_url = 'https://eldar-face-recognition.cognitiveservices.azure.com/face/v1.0/detect?recognitionModel=recognition_01&returnRecognitionModel=false&detectionModel=detection_01'
        headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}

        params = {
            'returnFaceId': 'false',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion',
        }

        gotBack = [{'error': 'noDataReceived'}]
        try:
            response = requests.post(face_api_url, params=params,
                                     headers=headers, data=img)
            gotBack = response.json()
            # print(gotBack[0])
            collectedData.append(gotBack[0])
        except Exception:
            print("recognition exception")
