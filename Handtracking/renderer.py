from capture import cap
import hand_detection
import gesture_detection
import hand

import cv2
import mediapipe as mp

# Drawing utilities
mpDraw = mp.solutions.drawing_utils
mpDrawingStyles = mp.solutions.drawing_styles

def render(handDetector):
    # Reset gesture strings
    leftGesture = rightGesture = ""
    
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
    hands = handDetector.detectHands(image, imageRGB)

    if hands is not None:
        for hand in hands:
            if (hand.normalizedHandLandmarks != [] and hand.handLandmarks != []):
                mpDraw.draw_landmarks(image, hand.normalizedHandLandmarks, mp.solutions.hands.HAND_CONNECTIONS)

                if (hand.handedness == "Left"):
                    leftGesture = hand.getGesture()
                elif (hand.handedness == "Right"):
                    rightGesture = hand.getGesture()


    # Flip image to avoid mirroring before applying text
    image = cv2.flip(image, 1)

    cv2.putText(image, leftGesture, (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 5)
    cv2.putText(image, rightGesture, (225,  50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 5)
            
    cv2.imshow("Output", image)