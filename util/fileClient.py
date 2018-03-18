# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 下午2:02
# @Author  : huangzhengwei
# @Site    : 
# @File    : fileClient.py
# @Software: PyCharm

import socket, json, os
import traceback
import sys
import time

#reload(sys)

#sys.setdefaultencoding('utf8')
# reload(sys)

# sys.setdefaultencoding('utf8')


def sendData(filename, ip="127.0.0.1", port="9999"):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((ip, int(port)))
	basefilename = os.path.basename(filename)
	myfile = open(filename, 'rb')
	myfile_size = os.path.getsize(filename)
	data = {'filename': basefilename, 'filesize': myfile_size}
	json_obj = json.dumps(data)
	client.send(json_obj)
	time.sleep(0.2)
	for readline in myfile:
		client.send(readline)
	else:
		# client.send(b'finish')
		print("file send is finish")

# if __name__ == '__main__':
# 	sendData("/Users/huangzhengwei/newWorkCode/yzt/newomni/faceRecognition_v1/faceNetDatasource/hhuangzhengwei_0/3.jpeg")
