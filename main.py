import mss
import numpy as np
import cv2
import pyautogui
import keyboard
import torch
import time
from tkinter import *
from tkinter import ttk

def krunkerAimbot():
    model = torch.hub.load("ultralytics/yolov5", "custom", path="best.pt")

    with mss.mss() as sct:
        monitor = {'top': 175, 'left': 587, 'width': 750, 'height': 750}
    while True:
        img = np.array(sct.grab(monitor))
        results = model(img)

        rl = results.xyxy[0].tolist()

        if len(rl) > 0:
            if rl[0][4] > 0.65:
                x = int(rl[0][2])
                y = int(rl[0][3])
                width = int(rl[0][2] - rl[0][0])
                height = int(rl[0][3] - rl[0][1])
                xpos = int(0.37 * ((x - (width/2)) - pyautogui.position()[0]))
                ypos = int(0.30 * ((y - (height / 2)) - pyautogui.position()[1]))
                pyautogui.moveRel(xpos, ypos)
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()
                pyautogui.moveRel(-xpos, -ypos)

        cv2.imshow('Aimbot NN View', np.squeeze(results.render()))
        cv2.waitKey(1)
        if keyboard.is_pressed("q"):
            break

    cv2.destroyAllWindows()

root = Tk()
root.geometry("300x100")
root.title("Aimbot Interface")
ttk.Label(root, text="(quite a bad) Aimbot").pack()
ttk.Button(root, text="Krunker Aimbot", command=krunkerAimbot).pack()

root.mainloop()