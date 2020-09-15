# This is the source code collection of Emotion light of INFO90003
# Video of the project is https://www.youtube.com/watch?v=KIMvJKLBZRc&feature=youtu.be

## Team members:
Chaoran Jin
chaoran@student.unimelb.edu.au

Eldar Kurmakaev
ekurmakaev@student.unimelb.edu.au

Tianqi Zhou
tiazhou@student.unimelb.edu.au


## The introduction of contents:
| file          | location
| ------------- |-------
| Interface     | ```/interface/Main.py```
| Arduino code  | ```/sketch_may06a/sketch_may06a.ino```

### Interfaces have three sections:

form  is mainWindow for welcome and sample hits
dashboard is colorDashboard for users decide the relation between colors and emotions
camera is cameraWindow for displaying the camera capture and light project at backend

### Changes for switching environment
Remember fix details in recognition/noStreamCapture.py for hardware connection

1.  change Url in blink() and final_output() when network environment changed
2.  Check if requests lines are commented or not , they are commented sometime because saving testing time
3.  make sure default model.txt and saturate.txt exist in root lib before run.
    If they are not here, commenting those two method in class VideoGet and run once to generate
4.  change the API key in processInAzure() into yours if exist one down
