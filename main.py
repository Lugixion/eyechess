import cv2
import numpy as np
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

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


    cv2.imshow("Output", frame) 

    k = cv2.waitKey(1)

    if k in ['q','1','2','']:
        break

    if cv2.waitKey(1)  == ord('1'):
        landmarks.append(1)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('2'):
        landmarks.append(2)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('3'):
        landmarks.append(3)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('4'):
        landmarks.append(4)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('5'):
        landmarks.append(5)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('a'):
        landmarks.append(6)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('b'):
        landmarks.append(7)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('c'):
        landmarks.append(8)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('d'):
        landmarks.append(9)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('e'):
        landmarks.append(10)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('f'):
        landmarks.append(11)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('g'):
        landmarks.append(12)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('h'):
        landmarks.append(13)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('o'):
        landmarks.append(14)
        ftw.write(str(landmarks)+"\n")
    elif cv2.waitKey(1)  == ord('n'):
        landmarks.append(15)
        ftw.write(str(landmarks)+"\n")

    
cap.release()

cv2.destroyAllWindows()

ftw.close()