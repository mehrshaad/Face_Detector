"""
Hi,
This is a simple code that uses your camera to detect faces.
I tried to explain every line by adding comments.
If you want the program to detect faces only (not eyes),
comment lines: 45~52.

Aug 2021 © Mehrshad Dadashzadeh
https://github.com/mehrshaad
"""
try:
    import cv2 as cv  #opencv-python used for detecting face, eyes, ...
    import numpy as np  #numpy used for managing xml data
except ImportError:  # if you don't have the packages just run the code and it'll take care
    import subprocess
    subprocess.call(
        ['pip3', 'install', '--upgrade', '--user', 'opencv-python'])
    subprocess.call(['pip3', 'install', '--upgrade', '--user', 'numpy'])
    import cv2 as cv
    import numpy as np

faceData = cv.CascadeClassifier(
    'haarcascade_frontalface_default.xml')  #opening face-detector xml data
eyesData = cv.CascadeClassifier('haarcascade_eye.xml')
windowX, windowY = 0, 0  #window size (written here to prevent crashes)
camera = cv.VideoCapture(
    0,
    cv.CAP_MSMF  #using cap_msmf.cpp source
)  #detecting your camera(s) and selecting first one in the list (if you have more than one)
faceColor, eyeColor, nameColor = (114, 28, 28), (0, 255, 0), (
    150, 200, 150)  #shapes and texts colors
while 1:
    _, win = camera.read()  #creating a window that show your camera picture
    gray = cv.cvtColor(
        win, cv.COLOR_BGR2GRAY
    )  #converting image to gray (doesn't impact the shown image)
    faces = faceData.detectMultiScale(
        gray, 1.1, 4
    )  #detects faces in the input image (detected objects are returned as a list of rectangles)

    for x, y, w, h in faces:  #passing trough the rectriangles of detected faces
        cv.rectangle(win, (x, y), (x + w, y + h), faceColor,
                     2)  #drawing rectriangle around each face

        inFaceGray = gray[y:y + h, x:x + w]  #limiting image to detected face
        inFaceWin = win[y:y + h, x:x + w]  #limiting windows to detected face
        eyes = eyesData.detectMultiScale(
            inFaceGray)  #detecting eyes in the drawn rectriangles
        for x2, y2, w2, h2 in eyes:  #passing trough the rectriangles of detected eyes
            cv.circle(inFaceWin, (x2 + w2 // 2, y2 + h2 // 2),
                      max(w2, h2) // 2, eyeColor,
                      2)  #drawing circle around eyes

    cv.putText(win,
               f'{len(faces)} Face(s)', (10, 40),
               cv.FONT_HERSHEY_DUPLEX,
               fontScale=0.8,
               color=faceColor,
               thickness=2)  #showing num of detected faces on the screen
    cv.putText(win,
               f'Mehrshad Dadashzadeh', (windowX // 2 - 90, windowY - 20),
               cv.FONT_HERSHEY_DUPLEX,
               fontScale=0.5,
               color=nameColor,
               thickness=1)  #credits :)

    cv.imshow('win', win)  #showing the whole window
    cv.setWindowTitle(
        "win",
        'Face Detector (by Mehrshad Dadashzadeh)')  #setting window title
    _, _, windowX, windowY = cv.getWindowImageRect('win')  #getting window size
    if cv.waitKey(30) == 27 or cv.getWindowProperty(
            'win', cv.WND_PROP_VISIBLE
    ) < 1:  #window goes on until user presses the esc button or closes window
        break

camera.release()  #releasing used camera
cv.destroyAllWindows()  #closing all windows
