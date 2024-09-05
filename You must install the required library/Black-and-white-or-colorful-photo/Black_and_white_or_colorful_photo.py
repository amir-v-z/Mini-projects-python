# pip install opencv-python
import cv2
img=cv2.imread("logo.png")

def function(x):
    print(x)

cv2.namedWindow("Black and white or colorful photo")
cv2.createTrackbar("change", "Black and white or colorful photo", 0,1,function)

while 1:
    if cv2.getTrackbarPos("change", "Black and white or colorful photo") == 0:
        cv2.imshow("Black and white or colorful photo", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

    else:
        cv2.imshow("Black and white or colorful photo", img)

    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()