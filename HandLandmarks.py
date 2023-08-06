import cv2
import numpy as np
import mediapipe as mp
mp_drawings=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands
cam = cv2.VideoCapture(0)
with mp.solutions.hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
    while cam.isOpened():
        ret,frame=cam.read()
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #results = hands.process(cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB))

        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        print(results)
        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawings.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS,mp_drawings.DrawingSpec(color=(255,0,0),thickness=4,circle_radius=4),mp_drawings.DrawingSpec(color=(0,255,0),thickness=6,circle_radius=2))
        image = cv2.flip(image,1)
        cv2.imshow("handTracking",image)
        if cv2.waitKey(1)==ord('q'):
            break
cam.release()
cv2.destroyAllWindows()
