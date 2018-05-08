import cv2
from convertor import toLAB
import cv2
import glob
from mpi4py import MPI
import os
cwd = os.getcwd()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


#Data = glob.glob(cwd+"/09082017/Agronomy/*.JPG")   
#ize_data = len(Data);
#print (Data)
#comm.scatter(size_data,root=0)
#comm.scatter(Data, root=0)
#Data = [];

def toLAB(image):
    lab_he = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    return lab_he   

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





 
'''
for img in glob.glob(cwd+"/09082017/Agronomy/*.JPG"):
    cv_img = cv2.imread(img,cv2.IMREAD_COLOR)
    lab_he = toLAB(cv_img)
    print(img[93:118])
    cv2.imwrite(cwd+"/labResult/"+img[93:118]+".png", lab_he)
#image = cv2.imread('C304B-4-07252017-2K7A2259.JPG',cv2.IMREAD_COLOR)

'''