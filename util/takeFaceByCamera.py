#-*-coding:utf-8-*-
__author__ = "huangzhengwei"
import sys
import os
import time
# import pickFace
try:
    import cv2
except BaseException:
    sys.path.append("/usr/local/lib/python2.7/site-packages/")
    import cv2

BASE_DIR = "../faceNetDatasource"

def takeFace(path, count):
    os.mkdir(path)
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    for i in range(count):
        # time.sleep(1)
        ret, frame = cap.read()
        cv2.imshow(path, frame)
        cv2.waitKey(1000)
        name = "%s/%d.jpeg" % (path, i)
        cv2.imwrite(name, frame)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)
    dir_rec = os.listdir(BASE_DIR)
    try:
        input_f = max(map(lambda x: int(x.replace("*_","")), dir_rec)) + 1
    except BaseException:
        input_f = 0
    try:
       input_s = raw_input("请输入用户名")
    except BaseException:
       input_s = input("请输入用户名")
    if not input_s:
        print ("请输入正确的用户名")
        exit(1)
    try:
       input_t = raw_input("请输入注册相片的张数")
    except BaseException:
       input_t = input("请输入注册相片的张数")
    try:
        if (int(input_t) < 0):
            print ("请输入正确的相片张数")
            exit(1)
    except BaseException:
        print ("请输入正确的张数")
        exit(1)
    # input_f = "s%s" % (input_f,)
    input_s = "%s_%s" % (input_s,input_f)
    takeFace(os.path.join(BASE_DIR, input_s), int(input_t))
    # pickFace.handleFace(input_s, int(input_t))
    # valueParse.writeNameConfig(input_s, input_f)
