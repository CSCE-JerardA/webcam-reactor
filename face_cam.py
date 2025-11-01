import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(

    max_num_faces = 1,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5

)

mp_drawings = mp.solutions.drawing_utils
drawing_spec = mp_drawings.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Can't open webcam!")
    exit()

print("Webcam is up! Press q to quit")

happy_hubert = cv2.imread("hubert_happy.jpg")
concerned_hubert = cv2.imread("hubert_straight_face.jpg")

current_react = concerned_hubert

if happy_hubert is None:
    print("Couldn't find Happy Hubert")
    exit()
    
if concerned_hubert is None :
    print("Couldn't find Concerned Hubert")
    exit()
    

SMILE_THRESHOLD = 0.12


while cap.isOpened():

    success, image = cap.read()

    if not success:
        print("Show me your face twin")

        continue

    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    results = face_mesh.process(image_rgb)

    current_react = concerned_hubert

    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0]

        p1 = face_landmarks.landmark[61]
        p2 = face_landmarks.landmark[291]

        mouth_width = np.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 )

        if mouth_width > SMILE_THRESHOLD :
            current_react = happy_hubert
        else:
            current_react = concerned_hubert



        mp_drawings.draw_landmarks(

            image = image,
            landmark_list =face_landmarks,
            connections = mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec = drawing_spec,
            connection_drawing_spec = drawing_spec
        )

       
    
    cv2.imshow("User WebCam", image)

    if current_react is None:
        cv2.imshow("Hubert Window", concerned_hubert)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

face_mesh.close()
cap.release()
cv2.destroyAllWindows()