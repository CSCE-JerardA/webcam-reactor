import cv2
import numpy as np
import mediapipe as mp
import dlib 

mp_drawings = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Can't open webcam!")
    exit()

print("Webcam is up! Press q to quit")

while cap.isOpened():
    success, image = cap.read()

    if not success:
        print("Show your face twin")

        continue

happy_hubert = cv2.imread('hubert_happy.jpg')
concerned_hubert = cv2.imread('straight')

