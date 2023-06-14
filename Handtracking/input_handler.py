import cv2

class InputHandler:
    pressedKey : int

    def handleInput(self):
        self.pressedKey = cv2.waitKey(1) & 0xFF