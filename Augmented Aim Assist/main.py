import cv2
from roboflow import Roboflow
import mss
import numpy as np
import pyautogui
import time
from config import ROBOFLOW_API_KEY

rf = Roboflow(api_key=ROBOFLOW_API_KEY)
project = rf.workspace("dylan-lewis-cfzob").project("krunker1")
model = project.version(3, local="http://localhost:9001/").model

with mss.mss() as sct:
    monitor = {'top': 0, 'left': 0, 'width': 1397, 'height': 786}
while True:
    prediction = model.predict(np.array(sct.grab(monitor)), overlap=30) # Makes a prediction of where it detects enemies based off the screen capture
    output = prediction.json()
    try:
        if output['predictions'][0]['confidence'] > 0.65: # If a detection is made that has over a 65% confidence level
            print("Detection")
            width = int(output['predictions'][0]['width']) # Extract the width and height values from the predicted JSON
            height = int(output['predictions'][0]['height'])
            x = int(output['predictions'][0]['x'] - width//2) # Get the Top X and Top Y co-ordinates of the bounding box
            y = int(output['predictions'][0]['y'] - height//2)
            xpos = int(0.37 * ((x - (width/2)) - pyautogui.position()[0])) # X and Y position to move the mouse to
            ypos = int(0.30 * ((y - (height / 2)) - pyautogui.position()[1]))
            pyautogui.moveRel(xpos, ypos)
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()
    except Exception:
        print("No Detection")
