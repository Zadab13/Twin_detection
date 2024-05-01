import cv2 as cv
import sys


# cv.samples.addSamplesDataSearchPath("C:\\Users\\ElsaVanMuysewinkel\\Downloads\\opencv opencv 4.x samples-data")
# img = cv.imread(cv.samples.findFile("starry_night.jpg"))
img = cv.imread("images/blad 1.png")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("blad 1",img)
