import numpy as np
import cv2
# Capturing video through webcam
webcam = cv2.VideoCapture(0)
# Start a while loop
while(1):
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()
    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    # Set range for red color and
    # define mask
    red_lower = np.array([0,143, 64], np.uint8)
    red_upper = np.array([5, 245, 141], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    kernal = np.ones((5, 5), 'uint8')
    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
    mask = red_mask)
    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(0, 255, 0), 2)
            cv2.putText(imageFrame, 'RED POT', (x, y),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0 ,0, 255))
    # Program Termination
    cv2.imshow('Multiple Color Detection in Real-Time', imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        #cap.release()
        cv2.destroyAllWindows()
        break