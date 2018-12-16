from PIL import Image, ImageDraw
import cv2
import cv2 as cv

image1 = cv2.imread("NormStomack2.png")
gray= cv2.bilateralFilter(image1,10,90,90)
cv2.imwrite("blur.png",gray)
image = Image.open("blur.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
factor = int(input('factor:')) #its better to use min factor closer to white color
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
image.save("ans2.jpg", "JPEG")
del draw
image= cv2.imread("ans2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)
#gray = cv2.GaussianBlur(gray, (3, 3), 0)

# распознавание контуров
#edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("edged2.jpg", edged)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
#_, contours, hierarchy =  cv.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(image, cnts, -1, (0, 255, 0),4)
cv2.imwrite("contours222.jpg",image)
print("h")
