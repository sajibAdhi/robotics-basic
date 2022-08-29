import cv2


def captureImage():
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey()

    cap.release()
    cv2.destroyAllWindows()

print("Program Start....")
captureImage()
print("Program End")