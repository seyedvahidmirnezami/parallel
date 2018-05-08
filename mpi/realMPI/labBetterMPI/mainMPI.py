import cv2
import math
#from convertor import toLAB
import glob
from mpi4py import MPI
import os
import numpy as np
cwd = os.getcwd()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

dataAll = glob.glob(cwd+"/09082017/Agronomy/*.JPG")
n = len(dataAll)
m = math.floor(n / size)
print('m')
print(m)
def toLAB(image):
    lab_he = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv_image = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    hue, sat, val = hsv_image[:,:,0], hsv_image[:,:,1], hsv_image[:,:,2]
    im_bw = cv2.threshold(hue, 0, 1, cv2.THRESH_BINARY)[1]
    mask = cv2.inRange(hsv, 0, 0.5)
    return mask


if rank == 0:
    data = glob.glob(cwd+"/09082017/Agronomy/*.JPG")
else:
    data = None

data = comm.bcast(data, root=0)
print ('rank',rank,data)
for i in data:
    cv_img = cv2.imread(i,cv2.IMREAD_COLOR)
    lab_he = toLAB(cv_img)
    cv2.imwrite(cwd+"/labResult/"+i[101:126]+"_"+str(rank)+".png", lab_he)


'''


if (rank < n-m*size):
    m = m + 1
   
    print ('rank')
    print (rank)
    print('n-m*size')
    print(n-m*size)
    print ('n')
    print (n)
    print ('m')
    print (m)

for i in range(0,m):
    print(dataAll[i])
    print(dataAll[i][101:126])
    cv_img = cv2.imread(dataAll[i],cv2.IMREAD_COLOR)
    lab_he = toLAB(cv_img)
    cv2.imwrite(cwd+"/labResult/"+dataAll[i][101:126]+"_"+str(rank)+".png", lab_he)


if rank == 0:
    print("I am : ",rank)
    data = glob.glob(cwd+"/09082017/Agronomy/*.JPG")
    #data = [(x+1)**x for x in range(size)]
    #print (data)
    #print (type(data) )
      
else:
    print(rank)
    data = None
    #print (Data)
    #print(img[92:117])
    #cv_img = cv2.imread(Data[rank],cv2.IMREAD_COLOR)
    #lab_he = toLAB(cv_img)
    #cv2.imwrite(cwd+"/labResult/"+img[93:118]+".png", lab_he)

    #iter =(size_data/size)*rank;
    #data = None
    #for img in Data:
    #    print(img[92:117])
    #    cv_img = cv2.imread(img,cv2.IMREAD_COLOR)
    #    lab_he = toLAB(cv_img)
    #    cv2.imwrite(cwd+"/labResult/"+img[93:118]+".png", lab_he)

data = comm.scatter(data, root=0)

print ('rank', rank,'has data',data)

#for img in data:
print(data[92:117])
cv_img = cv2.imread(data,cv2.IMREAD_COLOR)
lab_he = toLAB(cv_img)
cv2.imwrite(cwd+"/labResult/"+data[93:118]+".png", lab_he)
 
for img in glob.glob(cwd+"/09082017/Agronomy/*.JPG"):
    cv_img = cv2.imread(img,cv2.IMREAD_COLOR)
    lab_he = toLAB(cv_img)
    print(img[93:118])
    cv2.imwrite(cwd+"/labResult/"+img[93:118]+".png", lab_he)
#image = cv2.imread('C304B-4-07252017-2K7A2259.JPG',cv2.IMREAD_COLOR)

'''
