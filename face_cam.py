import cv2
import numpy as np
import mediapipe as mp

mp_faceM = mp.solutions.faceM

faceM = mp_faceM.FaceMesh(

    max_faces = 1,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5

)

mp_drawings = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Can't open webcam!")
    exit()

print("Webcam is up! Press q to quit")

happy_hubert = cv2.imread("hubert_happy.jpg")
concerned_hubert = cv2.imread("hubert_straight_face.jpg")

current_react = concerned_hubert


while cap.isOpened():

    success, image = cap.read()

    if not success:
        print("Show me your face twin")

        continue

    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    results = faceM.process(image_rgb)

    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0]

        mp_drawings.draw_landmarks(

            image,
            face_landmarks,
            mp_faceM
        )

        current_react = happy_hubert

    else:
        current_react = concerned_hubert
    
    cv2.imshow("User WebCam", image)

    if current_react is None:
        cv2.imshow("Hubert Window", concerned_hubert)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

faceM.close()
cap.release()
cv2.destroyAllWindows()