import cv2
from convertor import toLAB
import cv2
import numpy as np
import glob

for idx, img in enumerate(glob.glob("/media/vahid/96CC807ACC805701/Agronomy/pythonTasselTraits/mpi/imageproperties/09082017/Agronomy/*.JPG")):
    cv_img = cv2.imread(img,cv2.IMREAD_COLOR)
    im_gray = cv2.cvtColor( cv_img, cv2.COLOR_RGB2GRAY )
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    output = cv2.connectedComponentsWithStats(im_bw, 8, cv2.CV_32S)
    print(output[0])
    #   list[idx,0]=img[96:121]
    #0list[idx,1]=output[0]
    cv2.imwrite("/media/vahid/96CC807ACC805701/Agronomy/pythonTasselTraits/mpi/imageproperties/bwResult/"+img[96:121]+".png", im_bw)