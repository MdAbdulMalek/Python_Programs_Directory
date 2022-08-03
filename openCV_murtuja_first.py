import cv2

'''Image Read and Show Section'''

# img = cv2.imread("morata2.jpg")  ## image input

# cv2.imshow("Frame", img)   ## image show
# cv2.waitKey(0)

'''Video Read and Show Section'''

# cap = cv2.VideoCapture("cricket.mp4")  ## For reading video file

cap = cv2.VideoCapture(0)
cap.set(3,640)     #width code
cap.set(4,440)     # Height code
cap.set(10, 100)   ## brightness code

while True:
    success, img =  cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):   ## To break the loop press "q"
        break
