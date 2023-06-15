import keyboard
import hand_detection
import renderer
from input_handler import InputHandler

def run():
    isRunning = True
    inputHandler = InputHandler()
    handDetector = hand_detection.HandDetector()

    rightGesture = ""
    leftGesture = ""

    previousRightGesture = ""
    previousLeftGesture = ""

    while isRunning:
        renderer.render(handDetector)
        inputHandler.handleInput()

        rightGesture = handDetector.getRightGesture()
        leftGesture = handDetector.getLeftGesture()

        if previousRightGesture != rightGesture:
            # Gesture handling
            handleGesture(rightGesture)

        previousRightGesture = rightGesture
        previousLeftGesture = leftGesture
        
        if inputHandler.pressedKey == ord('q'):
            print("Application stopped")
            isRunning = False;
            # Do cleanup
            break

def handleGesture(gesture):
    if gesture == "palm_up":
        # Simulate pressing 'p' on the keyboard
        keyboard.press('p')
        keyboard.release('p')
        print("Palm up")
    elif gesture == "pointing_left":
        # Simulate pressing 'b' on the keyboard
        keyboard.press('b')
        keyboard.release('b')
        print("Pointing left")
    elif gesture == "pointing_right":
        # Simulate pressing 'n' on the keyboard
        keyboard.press('n')
        keyboard.release('n')
        print("Pointing right")
    elif gesture == "hand_down":
        print("Hand down")
    elif gesture == "none":
        print("No gesture")