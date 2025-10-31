import cv2
import numpy as np
import mediapipe as mp



mp_drawings = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Can't open webcam!")
    exit()

print("Webcam is up! Press q to quit")

happy_hubert = cv2.imread("hubert_happy.jpg")
concerned_hubert = cv2.imread("hubert_straight_face.jpg")



if happy_hubert is None or concerned_hubert is None:
    print("Nobody's there :( ")
    
current_react = concerned_hubert

while cap.isOpened():

    success, image = cap.read()

    if not success:
        print("Show me your face twin")

        continue

    cv2.imshow("User WebCam", image)

    if current_react is None:
        cv2.imshow("Hubert Window", concerned_hubert)