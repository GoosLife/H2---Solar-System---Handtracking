import gesture

def detectGesture(points):
    for func in gesture.gestures():
        if (func(points)):
            return func.__name__
    return "none"