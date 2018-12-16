import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage
from PIL import Image, ImageDraw
import cv2 as cv

cancer = cv2.imread("Cancer1.jpeg")
mask = np.zeros(cancer.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#rect = (150,100,450,290)
rect = (1,3,900,600)
cv2.grabCut(cancer,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
cancer = cancer*mask2[:,:,np.newaxis]
#plt.imshow(cancer),plt.colorbar(),plt.show()
cv2.imwrite("HalfCancer3.png",cancer)
img3 = cv2.imread("HalfCancer3.png")
rotated = ndimage.rotate(img3, 180)
cv2.imwrite("AusCancer3.png",rotated)

cancer2 = cv2.imread("AusCancer3.png")
mask = np.zeros(cancer2.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (1,3,530,700)
cv2.grabCut(cancer2,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
cancer2 = cancer2*mask2[:,:,np.newaxis]
#plt.imshow(cancer2),plt.colorbar(),plt.show()
cv2.imwrite("FullStomack3.png",cancer2)
#Rotation
img4 = cv2.imread("FullStomack3.png")
rotated = ndimage.rotate(img4, -180)
cv2.imwrite("NormStomack3.png",rotated)

image1 = cv2.imread("NormStomack3.png")
gray= cv2.bilateralFilter(image1,10,90,90)
cv2.imwrite("blur3.png",gray)
image = Image.open("blur3.png")
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
image.save("ans3.jpg", "JPEG")
del draw
image= cv2.imread("ans3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

# распознавание контуров
cv2.imwrite("edged3.jpg", edged)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
cv.drawContours(image, cnts, -1, (0, 255, 0),4)
cv2.imwrite("contours3.jpg",image)
solid=cv2.imread("Cancer1.jpeg")
cv.drawContours(solid, cnts, -1, (0, 0, 255),2)
cv2.imwrite("CancerDetected3.png",solid)
