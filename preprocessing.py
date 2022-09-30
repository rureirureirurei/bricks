import cv2
import numpy as np
import os

WIDTH = 600
HEIGHT = 600

def load(path):
    testsetFilenames = os.listdir(path)
    images = []
    for name in testsetFilenames:
        img = cv2.imread(path + '/' + name)
        images.append(img)

    return images


def show(images):
    i = 0
    for img in images:
        cv2.imshow(str(i), img)
        i += 1

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    images = load('./images')

    edges = []
    blurs = []


    i = 1
    for img in images:
        shrinked = cv2.resize(img, (WIDTH, HEIGHT))
        blurred = cv2.GaussianBlur(shrinked, (3,3), 0)
        grayscaled = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

        edges.append(cv2.Canny(image=grayscaled, threshold1=50, threshold2=150))


    show(edges)
