import cv2 as cv
import numpy as np
import os
import random
import sys


WIDTH = 800
HEIGHT = 800

NOICE_KERNEL_SIZE = (9, 9)
ADAPTIVE_THRESHHOLD_KERNEL_SIZE = 21
ADAPTIVE_THRESHHOLD_CONSTANT = 3
CONTOUR_AREA_THRESHHOLD = 250
CONTOUR_AREA_COUNTING_THRESHHOLD = 50
CONTOURS_DELTA = 150
EROSION_KERNEL = (15,15)
EROSION_KERNEL_SMALL_PIECES = (3,3)

def load(path):
    testsetFilenames = os.listdir(path)
    images = []
    for name in testsetFilenames:
        img = cv.imread(path + '/' + name)
        images.append((img, name))

    return images

def find_filtered_contours(image, limitationType):
        contours,_ = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contoursFiltered = []
        for contour in contours:
            if limitationType == 1:
                if cv.contourArea(contour) < CONTOUR_AREA_THRESHHOLD: 
                    contoursFiltered.append(contour)
            if limitationType == 2:
                if cv.contourArea(contour) > CONTOUR_AREA_COUNTING_THRESHHOLD: 
                    hull = cv.convexHull(contour)
                    contoursFiltered.append(hull)
        return contoursFiltered

def show(images):
    i = 0
    for img in images:
        cv.imshow(str(i), img)
        i += 1

    cv.waitKey(0)
    cv.destroyAllWindows()

def randColour():
    return (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))


if __name__ == "__main__":
    #if (len(sys.argv) != 0):
        #    EROSION_KERNEL = (int(sys.argv[0]), int(sys.argv[0]))
    #EROSION_KERNEL = (args[0], args[0])
    

    images = load('./images')

    edgedImgs = []
    blurredImgs = []


    i = 0
    for obj in images:
        img = obj[0]
        name = obj[1]
        shrinked = cv.resize(img, (WIDTH, HEIGHT))
        blurred = cv.GaussianBlur(shrinked, (NOICE_KERNEL_SIZE), 0)
        grayscaled = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
        thresh = cv.adaptiveThreshold(grayscaled,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,ADAPTIVE_THRESHHOLD_KERNEL_SIZE,ADAPTIVE_THRESHHOLD_CONSTANT)
   
        threshInversed = imagem = cv.bitwise_not(thresh)
        contours = find_filtered_contours(thresh, 1)
        for contour in contours:
            hull = cv.convexHull(contour)
            cv.drawContours(thresh, [hull], 0, 255, -1)

        
        contours = find_filtered_contours(thresh, 2)
        contoursAmount = len(contours)

        kernelErode = np.full(EROSION_KERNEL, -5, np.uint8)
        eroded = cv.erode(thresh, kernelErode)
        contours = find_filtered_contours(eroded, 2)

        if (abs(len(contours) - contoursAmount) > CONTOURS_DELTA):
            kernelErode = np.full(EROSION_KERNEL_SMALL_PIECES, -5, np.uint8)
            eroded = cv.erode(thresh, kernelErode)
            contours = find_filtered_contours(eroded, 2)


        result = img.copy()
        print(len(contours))


        for i in contours:
            M = cv.moments(i)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                imgWidth = np.shape(img)[0]
                imgHeight = np.shape(img)[1]
                cv.circle(result, (int(cx * imgHeight / HEIGHT), int(cy * imgWidth / WIDTH)), 3, (0, 0, 255), -1)

        cv.putText(result, str(len(contours)), (50,50), cv.FONT_HERSHEY_SIMPLEX, 1, (240, 255, 255), 2, cv.LINE_AA)
        cv.imwrite('./res/'+name, result)
        i += 1

    cv.waitKey(0)
    cv.destroyAllWindows()


