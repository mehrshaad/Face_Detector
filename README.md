# Face Detector
A simple **Python** script implemented with **OpenCV**.\
I used [XML](https://en.wikipedia.org/wiki/XML) face and eyes datas from [opencv repository](https://github.com/opencv/opencv) and cv2 Python package to use them in my script.\
Used packages are [opencv-python](https://pypi.org/project/opencv-python) and [numpy](https://pypi.org/project/numpy).

## How it works
This script detects all of your cameras (if there's none it'll crash) before opening any windows, then a window opens and it'll start detecting faces and eyes.\
I tried to explain every line plainly, but if you didn't get any part of it try to search it, it'll help you massively!\
Try connecting your phone's camera to your PC for better quality and more detection accuracy of course. Just don't forget to change the index of `VideoCapture` (line **26**) to change the camera in use (try changing indexes until you find the suitable camera).

## How to run
First you need to download and install [Python3](https://www.python.org). After that you have to run the file which named `faceDetector.py`.\
After that download files from [releases section](https://github.com/mehrshaad/Face_Detector/releases) and extract them.\
Then open `CMD`, `Terminal` or `shell` (whatever you call it! 🙂) in that folder, and enter:
```sh
python faceDetector.py
```
**NOTE**: use `python3` instead of `python` if you're running on*Linux* or *MacOS*.\
This command should start the script. After that it may take a while till a window appears, because at the first run it'll start to download and install opencv and numpy python packages (if you didn't have them already) which need to download about *60mb* of files, then you good to go!

**Hope you enjoy it, find it usefull and learn something from it!** 👍🏼
