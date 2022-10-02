import cv2 as cv
import numpy as np
import os
import random
import sys

NOICE_KERNEL_SIZE = (9, 9)
ADAPTIVE_THRESHOLD_KERNEL_SIZE = 21
ADAPTIVE_THRESHOLD_CONSTANT = 3
CONTOUR_AREA_THRESHOLD = 150
CONTOUR_AREA_COUNTING_THRESHOLD = 250
CONTOURS_DELTA = 150
EROSION_KERNEL = np.full((15,15), -5, np.uint8)
EROSION_KERNEL_SMALL_PIECES = np.full((3,3), -5, np.uint8)

def load(path):
    testset_filenames = os.listdir(path)
    images = []
    names = []
    for name in testset_filenames:
        img = cv.imread(path + '/' + name)
        images.append(img)
        names.append(name)
    return (images, names)

def find_filtered_contours(image, limitation_type):
        contours,_ = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours_filtered = []
        for contour in contours:
            if limitation_type == 1:
                if cv.contourArea(contour) < CONTOUR_AREA_THRESHOLD: 
                    contours_filtered.append(contour)
            if limitation_type == 2: 
                if cv.contourArea(contour) > CONTOUR_AREA_COUNTING_THRESHOLD: 
                    hull = cv.convexHull(contour)
                    contours_filtered.append(hull)
        return contours_filtered

if __name__ == "__main__":
    images, names = load('./images')
    images_amount = len(images)

    for index in range(images_amount):
        image = images[index]
        name = names[index]
        blurred = cv.GaussianBlur(image, (NOICE_KERNEL_SIZE), 0)
        grayscaled = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
        thresh = cv.adaptiveThreshold(grayscaled,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,ADAPTIVE_THRESHOLD_KERNEL_SIZE,ADAPTIVE_THRESHOLD_CONSTANT)
        thresh_inversed = cv.bitwise_not(thresh)
        contours = find_filtered_contours(thresh, 1)
        for contour in contours:
            hull = cv.convexHull(contour)
            cv.drawContours(thresh, [hull], 0, 255, -1)
        contours = find_filtered_contours(thresh, 2)
        contours_amount = len(contours)
        eroded = cv.erode(thresh, EROSION_KERNEL)
        contours = find_filtered_contours(eroded, 2)

        if (abs(len(contours) - contours_amount) > CONTOURS_DELTA): #TODO
            eroded = cv.erode(thresh, EROSION_KERNEL_SMALL_PIECES)
            contours = find_filtered_contours(eroded, 2)

        result = image.copy()
        print(len(contours))
        for i in contours:
            M = cv.moments(i)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                image_width = np.shape(image)[0]
                image_height = np.shape(image)[1]
                cv.circle(result, (cx, cy), 3, (0, 0, 255), -1) #TODO


        cv.putText(result, str(len(contours)), (50,50), cv.FONT_HERSHEY_SIMPLEX, 1, (240, 255, 255), 2, cv.LINE_AA)
        cv.imwrite('./res/'+name, result)

    cv.waitKey(0)
    cv.destroyAllWindows()


