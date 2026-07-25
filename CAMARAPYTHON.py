# Open webcam
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    # Show webcam
    cv2.imshow("Web Camera", frame)

    # Press Q to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Close everything
camera.release()
cv2.destroyAllWindows()