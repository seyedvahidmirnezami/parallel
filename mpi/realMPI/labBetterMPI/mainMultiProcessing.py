'''
import cv2
import math
from multiprocessing import Pool
from multiprocessing import Process, current_process
import glob
import os
cwd = os.getcwd()

def toLAB(data):
    print (data)
    cv_img = cv2.imread(data,cv2.IMREAD_COLOR)
    lab_he = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imwrite(cwd+"/labResult/"+data[101:126]+".png", lab_he)


dataAll = glob.glob(cwd+"/09082017/Agronomy/*.JPG")
n = len(dataAll)
numbers = list(range(0,n))
procs = []

for index, number in enumerate(numbers):
    proc = Process(target=toLAB, args=(dataAll,))
    procs.append(proc)
    proc.start()

for proc in procs:
    proc.join()


    '''
import multiprocessing.Manager as Manager
import multiprocessing.Pool as Pool

m = Manager()
p = Pool(processes=5)

state_info = m.dict()
state_info['image_found'] = False

def processImage(img):

    # ... Process Image ...
    if imageIsBlack(img):
        state_info['image_found'] = True
        p.terminate()

p.apply(processImage, imageList)

if state_info['image_found']:
    print ('There was a black image!!')
else: