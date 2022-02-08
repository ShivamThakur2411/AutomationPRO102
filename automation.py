import numpy as np
import cv2
import pyautogui as pt
import random
import time

startTime = time.time()

def take_screenshot():
    number = random.randrange(0, 1000)
    result = True

    while(result):
        image_name = "img"+str(number)+".png"
        image = pt.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        cv2.imwrite(image_name, image)
        result = False
    return image_name
    print("Screenshot taken")
    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time() - startTime)>=300):
            take_screenshot()

main()