import json
# get .json file
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
    print(data[i])
    print(i)
    # anger
    emotion[i][0] = data[i]['faceAttributes']['emotion']['anger']
    emotion[i][1] = data[i]['faceAttributes']['emotion']['contempt']
    emotion[i][2] = data[i]['faceAttributes']['emotion']['disgust']
    emotion[i][3] = data[i]['faceAttributes']['emotion']['fear']
    emotion[i][4] = data[i]['faceAttributes']['emotion']['happiness']
    emotion[i][5] = data[i]['faceAttributes']['emotion']['neutral']
    emotion[i][6] = data[i]['faceAttributes']['emotion']['sadness']
    emotion[i][7] = data[i]['faceAttributes']['emotion']['surprise']

print(emotion)