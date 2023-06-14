import renderer
from input_handler import InputHandler

import cv2

def run():
    isRunning = True
    
    while isRunning:
        renderer.render()
        inputHandler = InputHandler()
        inputHandler.handleInput()

        if inputHandler.pressedKey == ord('q'):
            print("Application stopped")
            isRunning = False;
            # Do cleanup
            break;