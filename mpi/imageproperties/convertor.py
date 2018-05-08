import cv2
def toLAB(image):
    lab_he = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    return lab_he
