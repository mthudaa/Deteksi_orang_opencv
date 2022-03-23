import cv2
cam = cv2.VideoCapture(0)
tubuh = cv2.CascadeClassifier('tubuh.xml')
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = tubuh.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 2)
    cv2.imshow("Tubuh", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cam.release()
cv2.destroyWindow()
