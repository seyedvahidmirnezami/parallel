import cv2
from convertor import toLAB
import cv2
import glob

for img in glob.glob("/media/vahid/96CC807ACC805701/Agronomy/pythonTasselTraits/mpi/09082017/Agronomy/*.JPG"):
    cv_img = cv2.imread(img,cv2.IMREAD_COLOR)
    lab_he = toLAB(cv_img)
    print(img[80:105])
    cv2.imwrite("/media/vahid/96CC807ACC805701/Agronomy/pythonTasselTraits/mpi/labResult/"+img[80:105]+".png", lab_he)
#image = cv2.imread('C304B-4-07252017-2K7A2259.JPG',cv2.IMREAD_COLOR)


