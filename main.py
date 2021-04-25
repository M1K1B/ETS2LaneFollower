from cv2 import cv2
import pyautogui
import numpy as np
import time

from components import laneDetect

def main():
    cap = cv2.VideoCapture('tests/position_6_test_video_1.mp4')
    conf = laneDetect.LaneFinder()

    while(cap.isOpened()):
        ret, frame = cap.read()

        final = conf.find_lanes(frame)
        cv2.imshow('frame', final)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def test():
    conf = laneDetect.LaneFinder()

    cap = cv2.imread('tests/position_6_test_2.jpg')
    
    final = conf.find_lanes(cap)

    cv2.imshow('frame', final)
    cv2.waitKey()


if __name__ == '__main__':
    main()