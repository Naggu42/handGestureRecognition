import cv2
import numpy
from tensorflow.python.keras.models import load_model

# Used to test the model and see its output.

cap = cv2.VideoCapture(0)

model = load_model("my_model.h5")
model.summary()

str = "Blank"
counter = 0
while (cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img, (306, 306), (50, 50), (255, 0, 0), 0)
    crop_img = img[50:306, 50:306]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15, 15), 2)
    blur = cv2.GaussianBlur(gray, (15, 15), 2)
    ret, res = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
    cv2.putText(img, str, (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Gesture', img)
    cv2.imshow('Contours', res)
    counter += 1
    cv2.waitKey(10)
    if counter >= 20:
        prediction = model.predict(numpy.array([res]).reshape(1, 256, 256, 1))
        print(prediction)
        counter = 0
        max = numpy.argmax(prediction)
        if max == 0:
            str = "Blank"
        elif max == 1:
            str = "Fist"
        elif max == 2:
            str = "Open Hand"
        elif max == 3:
            str = "OK"
        elif max == 4:
            str = "Palm"
        elif max == 5:
            str = "Thumb"


