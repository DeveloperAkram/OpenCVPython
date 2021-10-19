import cv2
print("package Imported")

# <--- Image Show --->

# img = cv2.imread("Resources/lena.png")

# cv2.imshow("Output", img)
# cv2.waitKey(0)

# <--- Video Show --->

#frameWidth = 640
#frameHeight = 480
#cap = cv2.VideoCapture("Resources/test_ video.mp4")
#while True:
#    success, img = cap.read()
#    img = cv2.resize(img, (frameWidth, frameHeight))
#    cv2.imshow("Result", img)
#    if cv2.waitKey(1) and 0xFF == ord('q'):
#        break

# <--- Webcam Show --->

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
