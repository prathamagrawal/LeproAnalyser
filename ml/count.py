import matplotlib.pyplot as plt
import cv2
import numpy
path='../data/train/image0.tif'
kernel = numpy.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

def process(path):
    frame = cv2.imread(path)
    image_sharp = cv2.filter2D(src=frame, ddepth=-1, kernel=kernel)
    gray = cv2.cvtColor(image_sharp, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray,threshold1=100, threshold2=200)
    dilated = cv2.dilate(canny, (1,1), iterations = 1)
    (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(dilated, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)

    return len(cnt)
