from threading import Thread
import cv2
import json
import requests


class CaptureRecognize:
    def __init__(self):
        self.a = 1


    def mainProcess(self):

        print("Enter s to begin, q to end")
        inputStr = input()
        video_getter = None
        if inputStr == "s":
            print("Selected capturing")
            try:
                video_getter = VideoGet().start()
                flag = False
                while flag == False:
                    secondInput = input()
                    if secondInput:
                        video_getter.stop()
                        flag = True

                    else:
                        continue
            except:
                print("Exception")


class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self):
        self.stream = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.collectedData = []

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):

        self.stream = cv2.VideoCapture(0)
        count = 0
        frame_number = 0
        samples_per_second = 0.5
        sample_rate = 30 / samples_per_second
        path = '/Users/e/PycharmProjects/DNI-project/input-pictures'

        while not self.stopped:
            ret, frame = self.stream.read()
            frame_number = frame_number + 1;
            if frame_number > sample_rate:
                output = frame.copy()
                self.processInAzure(output, self.collectedData)
                # cv2.imwrite(os.path.join(path, 'frame{:d}.jpg'.format(count)), frame)
                print("Picture saved")
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

    def processInAzure(image, collectedData):
        img = cv2.imencode('.jpg', image)[1].tostring()
        # set to your own subscription key value
        subscription_key = "5ed36051fd474aed83e7c35c15cd17c3"
        assert subscription_key

        # replace <My Endpoint String> with the string from your endpoint URL
        face_api_url = 'https://australiaeast.api.cognitive.microsoft.com/face/v1.0/detect?recognitionModel=recognition_01&returnRecognitionModel=false&detectionModel=detection_01'
        headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}

        params = {
            'returnFaceId': 'false',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion',
        }

        response = requests.post(face_api_url, params=params,
                                 headers=headers, data=img)
        gotBack = (json.dumps(response.json()))
        print(gotBack)
        collectedData.append(gotBack)


ed = CaptureRecognize.mainProcess()