# -*- coding=utf-8 -*-

import os
import sys
import time
from faceValidate1 import MtcnnDetector
import mxnet as mx
try:
    import cv2
except BaseException:
    sys.path.append("/usr/local/lib/python2.7/site-packages/")
    import cv2
# import dlib
# catPath = "../casade/haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(catPath)
# d_path = "../casade/shape_predictor_68_face_landmarks.dat"
detector = MtcnnDetector(model_folder='./model', ctx=mx.cpu(0), num_worker = 4 , accurate_landmark = False)

# 1. 可以同dlib检测人脸，准确率更高，但是速度更慢
# detector = dlib.get_frontal_face_detector()
def handleFace(name, count):
    srcNmae = "../faceNetDatasource/%s" % (name)
    destName = "../secondDatasource/%s" % (name)
    if not os.path.exists(destName):
        os.mkdir(destName)
    j = 1
    for i in range(1):
        destPath = "%s/%d.jpeg" % (destName, j)
        srcPath = "/Users/huangzhengwei/newWorkCode/yzt/newomni/faceRecognition_v1/faceNet/testDatasource/test1521134304.38.jpeg"
        # 读取图片并灰度化
        print(srcPath)
        img = cv2.imread(srcPath)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        results = detector.detect_face(img)
        print ("-=-=-=-------------")
        print (results)
        if results is None:
            continue
        total_boxes = results[0]
        # draw = gray.copy()
        # 取最大的脸部,排除在录脸的时候录取了其他人的脸
        keyList = list()
        valueList = list()
        for b in total_boxes:
            x1 = int(b[0])
            x2 = int(b[1])
            y1 = int(b[2])
            y2 = int(b[3])
            keyList.append(x2-x1)
            ROI = img[x2:y2,x1:y1]
            ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
            valueList.append(ROI)
        if keyList:
            index =  keyList.index(max(keyList)) # 返回最大值
            ROI = valueList[index]
            try:
                ROI = cv2.resize(ROI, (128, 128))
                cv2.imshow("test", ROI)
                cv2.waitKey(1)
                cv2.imwrite(destPath, ROI)
                j = j+1
            except BaseException:
                pass
        # rects = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        # if len(rects) != 0:
        #     for (x, y, w, h) in rects:
        #         cv2.imshow("test", gray[y:(y + h), x:(x + w)])
        #         cv2.waitKey(1)
        #         f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
        #         cv2.imwrite(destPath, f)
        #     j = j+1

if __name__ == '__main__':
    handleFace("yihaitao",
               10)