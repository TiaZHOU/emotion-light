from threading import Thread
import cv2
import json
import requests
import traceback

import http.client, urllib.request, urllib.parse, urllib.error, base64

class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

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
        frame_number = 0
        samples_per_second = 10000
        sample_rate = 30 / samples_per_second

        while not self.stopped:
            ret, frame = self.stream.read()
            frame_number = frame_number + 1;
            if frame_number > sample_rate:
                output = frame.copy()
                self.processInAzure(output, self.collectedData)
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
        print(self.collectedData)
        return self.collectedData

    def processInAzure(self ,image, collectedData):

        img = cv2.imencode('.jpg', image)[1].tostring()
        subscription_key = "747a8208ff0f422499c5ecdc7c059551"
        # replace <My Endpoint String> with the string from your endpoint URL
        face_api_url = 'https://eldar-face-recognition.cognitiveservices.azure.com/face/v1.0/detect?recognitionModel=recognition_01&returnRecognitionModel=false&detectionModel=detection_01'
        headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}

        params = {
            'returnFaceId': 'false',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion',
        }

        gotBack =  [{'error': 'noDataReceived'}]
        try:
            response = requests.post(face_api_url, params=params,
                                     headers=headers, data=img)
            gotBack = response.json()
            print(gotBack[0])
            collectedData.append(gotBack[0])
        except Exception:
            print("exception")