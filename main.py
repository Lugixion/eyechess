import cv2
import numpy as np
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

keys = {
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    97: "a",
    98: "b",
    99: "c",
    100: "d",
    101: "e",
    102: "f",
    103: "g",
    104: "h",
    110: "n",
    111: "o",
    113: "q"
}

cap = cv2.VideoCapture(0)

ftw = open("data","a")

while True:
    _, frame = cap.read()

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(framergb)
    
    className = ''

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

    k = cv2.waitKey(1)

    if k in keys.keys():
        if k == 113: break
        landmarks.append(list(keys.keys()).index(k))
        ftw.write(str(landmarks)+"\n")

    cv2.imshow("Output", frame) 
    
cap.release()

cv2.destroyAllWindows()

ftw.close()