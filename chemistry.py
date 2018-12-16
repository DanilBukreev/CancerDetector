# coding: utf8
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image, ImageDraw
import cv2
import cv2 as cv
import os


def get_count_contours(counters):
    counter = [c for c in counters if len(c) > 5]
    return len(counter)

def get_cnts():
    image = Image.open("3.jpg")
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    factor = 10
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    image.save("ansCH2.jpg", "JPEG")
    del draw

    hsv_min = np.array((0, 0, 240), np.uint8)
    hsv_max = np.array((255, 15, 255), np.uint8)

    Image.open('ansCH2.jpg').save('ansCH2.png')
    image = cv.imread("ansCH2.png")

    hsv = cv.cvtColor(image,
                      cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр

    _, cnts, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
                                         cv.CHAIN_APPROX_SIMPLE)

    return cnts


if __name__ == '__main__':
    image = Image.open("3.jpg")
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    factor = int(input('factor:'))  # its better to use min factor closer to white color
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    image.save("ansCH2.jpg", "JPEG")
    del draw

    hsv_min = np.array((0, 0, 240), np.uint8)
    hsv_max = np.array((255, 15, 255), np.uint8)

    Image.open('ansCH2.jpg').save('ansCH2.png')
    image = cv2.imread("ansCH2.png")

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр

    _, cnts, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    count_contours = get_count_contours(cnts)
    print(count_contours)

    # отображаем контуры поверх изображения
    cv.drawContours(image, cnts, -1, (0, 0, 255), 3, cv.LINE_AA, hierarchy, 1)
    cv2.imwrite("contoursCH2.jpg", image)
