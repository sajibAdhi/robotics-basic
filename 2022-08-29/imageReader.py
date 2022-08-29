import cv2


def imageReader(filename="20220829\R.jpg"):
    img = cv2.imread(filename)
    cv2.imshow("sajib", img)
    img2 = cv2.rectangle(img, (20, 20), (40, 40), (255, 0, 0), 10)

    cv2.imshow("image2", img2)
    cv2.waitKey(2000)


imageReader("20220829\R.jpg")
