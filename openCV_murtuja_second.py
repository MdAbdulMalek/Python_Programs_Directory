import cv2

img = cv2.imread("morata2.jpg")

imgcanny = cv2.Canny(img, 150, 150)   ## canny edges


cv2.imshow("Canny Image", imgcanny)
cv2.waitKey(0)