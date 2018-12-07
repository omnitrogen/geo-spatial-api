import math
import numpy as np
import cv2
from PIL import Image


def white_percentage(liste):

    lower_white = np.array([180, 180, 180], dtype=np.uint8)
    upper_white = np.array([255, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(liste, lower_white, upper_white)
    maskPixels = cv2.countNonZero(mask)

    return math.ceil((100 * maskPixels) / mask.size)


def cap(n):
    if n + 100 > 255:
        return 255
    return n + 100


def divide_pic(img):
    liste = [((0, 1), (0, 1)), ((1, 1), (1, 2)), ((0, 2), (1, 3)), ((0, 3), (1, 4)),
             ((0, 4), (1, 5)), ((0, 5), (1, 6)), ((0, 6), (1, 7)), ((0, 7), (1, 8))]
    # 512 / 64 = 8
    # 900 / 45 = 20
    for elt in liste:
        if white_percentage(img[elt[0][0] * 64:elt[0][1] * 45, elt[1][0] * 64:elt[1][1] * 45]) > 40:
            img[elt[0][0] * 64:elt[0][1] * 45, elt[1][0] * 64:elt[1][1] * 45][..., 2] += 10

    return img


if __name__ == '__main__':
    pass
