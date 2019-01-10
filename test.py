import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
while True:
    ret, frame = cam.read()

    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        face_frame = frame[y:y + h, x:x + w]
    cv2.imshow("Face test", face_frame)

cam.release()

cv2.destroyAllWindows()