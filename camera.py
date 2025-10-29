import cv2
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Could not open webcam.")
    exit()

print("Webcam Reactor is running. Press 'q' to quit.")

while cap.isOpened():
    
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        
        continue

    
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    
    results = hands.process(image_rgb)

    
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    
    hand_count = 0

    
    if results.multi_hand_landmarks:
        hand_count = len(results.multi_hand_landmarks)

        for hand_landmarks in results.multi_hand_landmarks:
            
            mp_drawing.draw_landmarks(
                image_bgr,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
            )

    
    
    reaction_text = ""
    text_color = (255, 255, 255) # White

    if hand_count == 0:
        reaction_text = "Reactor Waiting... Show your hands!"
        text_color = (0, 0, 255)  # Red
    elif hand_count == 1:
        reaction_text = "ONE HAND: Single Focus Activated."
        text_color = (0, 255, 255) # Yellow
    elif hand_count == 2:
        reaction_text = "TWO HANDS: Dual-Wield Power!"
        text_color = (0, 255, 0)  # Green

    
    H, W, _ = image_bgr.shape

    
    cv2.putText(
        img=image_bgr,
        text=f"{hand_count} Hands Detected. {reaction_text}",
        org=(10, 30),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=text_color,
        thickness=2,
        lineType=cv2.LINE_AA
    )

    cv2.imshow('Webcam Reactor (Press Q to quit)', image_bgr)

    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break



cap.release()

cv2.destroyAllWindows()