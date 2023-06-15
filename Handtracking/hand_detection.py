from collections import defaultdict
from hand import Hand

import mediapipe as mp

class HandDetector:

    # Hand detection
    RIGHT_HAND : int
    LEFT_HAND : int

    handList : list

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    def __init__(self):
        self.handList = []
        self.RIGHT_HAND = -1
        self.LEFT_HAND = -1

    def detectHands(self, image, imageRGB):
        self.handList = [] # Reassign list to flush old data

        results = self.getResults(imageRGB)

        if results.multi_hand_landmarks:
    
            self.getHandIndexes(results)
        
            self.getHandLandmarks(results, image)

            self.setHandAttributes()

            return self.handList

    def getResults(self, imageRGB):   
        return self.hands.process(imageRGB)

    ### Find out which hand is which
    def getHandIndexes(self, results):
        handIndexIterator = 0

	    # checking whether a hand is detected
        if results.multi_hand_landmarks:
            for hand in results.multi_handedness:
                # If the label is Right, it is actually the left hand because the image is being flipped.
                if hand.classification[0].label == "Right":
                    self.LEFT_HAND = handIndexIterator
                else:
                    self.RIGHT_HAND = handIndexIterator
                handIndexIterator += 1

    def getHandLandmarks(self, results, image):
            handLandmarks = []

            for handLms in results.multi_hand_landmarks: # working with each hand
                handObject = Hand()
                hand = []

                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    hand.append([id, cx, cy])

                handLandmarks.append(hand)
                self.handList.append(handObject)

            self.setHandLandmarks(handLandmarks, results.multi_hand_landmarks)

    def setHandLandmarks(self, handLandmarks, normalizedHandLandmarks):
        if self.LEFT_HAND < len(normalizedHandLandmarks) and self.LEFT_HAND < len(handLandmarks):
            self.handList[self.LEFT_HAND].setNormalizedHandLandmarks(normalizedHandLandmarks[self.LEFT_HAND])
            self.handList[self.LEFT_HAND].setHandLandmarks(handLandmarks[self.LEFT_HAND])
        
        if self.RIGHT_HAND < len(normalizedHandLandmarks) and self.RIGHT_HAND < len(handLandmarks):
            self.handList[self.RIGHT_HAND].setNormalizedHandLandmarks(normalizedHandLandmarks[self.RIGHT_HAND])
            self.handList[self.RIGHT_HAND].setHandLandmarks(handLandmarks[self.RIGHT_HAND])

    def setHandAttributes(self):
        if self.LEFT_HAND < len(self.handList):
            self.handList[self.LEFT_HAND].setHandedness("Left")

        if self.RIGHT_HAND < len(self.handList):
            self.handList[self.RIGHT_HAND].setHandedness("Right")

    def getRightGesture(self):
        if self.RIGHT_HAND >= 0 and self.RIGHT_HAND < len(self.handList):
            return self.handList[self.RIGHT_HAND].getGesture()
        return "none"

    def getLeftGesture(self):
        if self.LEFT_HAND >= 0 and self.LEFT_HAND < len(self.handList):
            return self.handList[self.LEFT_HAND].getGesture()
        return "none"