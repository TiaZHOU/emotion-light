import json
import cv2 as cv
import numpy as np


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
def read_emotion():
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
        emotion[i][0] = data[i]['faceAttributes']['emotion']['anger']
        emotion[i][1] = data[i]['faceAttributes']['emotion']['contempt']
        emotion[i][2] = data[i]['faceAttributes']['emotion']['disgust']
        emotion[i][3] = data[i]['faceAttributes']['emotion']['fear']
        emotion[i][4] = data[i]['faceAttributes']['emotion']['happiness']
        emotion[i][5] = data[i]['faceAttributes']['emotion']['neutral']
        emotion[i][6] = data[i]['faceAttributes']['emotion']['sadness']
        emotion[i][7] = data[i]['faceAttributes']['emotion']['surprise']
    print('total ' + counter.__str__() + ' pictures are send')
    return emotion


# sample for color display
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
    color4_cyan = create_image(r=0, g=127, b=255)
    color5_blue = create_image(r=0, g=0, b=255)
    color6_purple = create_image(r=139, g=0, b=255)
    color7_white = create_image(r=255, g=255, b=255)
    if color_num == 0:
        return color0_red
    elif color_num == 1:
        return color1_orange
    elif color_num == 2:
        return color2_yellow
    elif color_num == 3:
        return color3_green
    elif color_num == 4:
        return color4_cyan
    elif color_num == 5:
        return color5_blue
    elif color_num == 6:
        return color6_purple
    elif color_num == 7:
        return color7_white


# define function which user change color for specific emotion
def color_change(formal_model, color, emo):
    formal_model[emo] = color
    return formal_model


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


# main begin
model = [0, 1, 2, 3, 4, 5, 6, 7]  # initial color model, numbers refer to colors, positions refer to emotions
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

emotion = read_emotion()
# print(emotion)

color_list = max_two_emo(emotion)
# print(color_list)

# simulate user change color3 to emotion5
# TODO set color change API for  interface
color_change(model, 3, 5)

# generate two pic then merge on weight
#
output = [[0 for i in range(4)] for i in range(len(color_list))]
display = [0 for i in range(len(color_list))]
for i in range(len(color_list)):
    img1 = color_pick(model[color_list[i][0]])
    img2 = color_pick(model[color_list[i][1]])
    # TODO the add should more sensitive because many neutral
    clA = cv.addWeighted(img1, emotion[i][color_list[i][0]], img2, emotion[i][color_list[i][1]], 0)
    output[i][0] = clA[0][0][0].astype(str)
    output[i][1] = clA[0][0][1].astype(str)
    output[i][2] = clA[0][0][2].astype(str)
    output[i][3] = "1000"
    print(output[i])  # final result RGB code
    display[i] = create_image(r=clA[i][0][0], g=clA[i][0][1], b=clA[i][0][2])
# TODO transfer the result into Arduino kit
store(output)
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
