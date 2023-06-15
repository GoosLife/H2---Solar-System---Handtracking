import gesture_detection

class Hand:
    gesture : str
    handLandmarks : list
    normalizedHandLandmarks : list
    handedness : str

    def __init__(self) :
        self.gesture = ""
        self.handLandmarks = []
        self.normalizedHandLandmarks = []

    def getGesture(self):
        if (self.handLandmarks is not None):
            self.gesture = gesture_detection.detectGesture(self.handLandmarks)
            return self.gesture
        else:
            return "none"

    def setHandLandmarks(self, handLandmarks):
        self.handLandmarks = handLandmarks

    def setNormalizedHandLandmarks(self, normalizedHandLandmarks):
        self.normalizedHandLandmarks = normalizedHandLandmarks

    def setHandedness(self, handedness):
        self.handedness = handedness