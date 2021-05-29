import cv2

cap = cv2.VideoCapture(0)
str = 0
n = 0

# Takes 300 pictures from your video feed to create training data.
# press the following keys to save data in different folders-
# 1. Blank Picture, 2. Full Hand, 3. Fist, 4.OK gesture, 5.Palm, 6.Thumbs up

#   Change below variable to your project directory.
project_dir = "F:\Projects\handGestureRecognition\Training_data"

# Program will close after one directory is created.

while (cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img, (350, 350), (50, 50), (255, 0, 0), 0)
    crop_img = img[50:350, 50:350]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15, 15), 2)
    ret, res = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('Gesture', img)
    cv2.imshow('Contours', res)

    k = cv2.waitKey(10)
    if k == 49:
        n = 1
    if k == 50:
        n = 2
    if k == 51:
        n = 3
    if k == 52:
        n = 4
    if k == 53:
        n = 5
    if k == 54:
        n = 6

    if n == 1:
        cv2.imwrite( project_dir  + '\Blank\img_%s.jpg' % str, res,
                    [cv2.IMWRITE_JPEG_QUALITY, 100])
        str += 1
    if n == 1:
        cv2.imwrite('F:\Projects\openCVTests\Training_data\Full_hand\img_%s.jpg' % str, res,
                    [cv2.IMWRITE_JPEG_QUALITY, 100])
        str += 1
    if n == 1:
        cv2.imwrite('F:\Projects\openCVTests\Training_data\Fist\img_%s.jpg' % str, res,
                    [cv2.IMWRITE_JPEG_QUALITY, 100])
        str += 1
    if n == 1:
        cv2.imwrite('F:\Projects\openCVTests\Training_data\OK\img_%s.jpg' % str, res,
                    [cv2.IMWRITE_JPEG_QUALITY, 100])
        str += 1
    if n == 1:
        cv2.imwrite('F:\Projects\openCVTests\Training_data\Palm\img_%s.jpg' % str, res,
                    [cv2.IMWRITE_JPEG_QUALITY, 100])
        str += 1
    if n == 1:
        cv2.imwrite('F:\Projects\openCVTests\Training_data\Thumbs_up\img_%s.jpg' % str, res,
                    [cv2.IMWRITE_JPEG_QUALITY, 100])
        str += 1
    if str >= 300:
        break
