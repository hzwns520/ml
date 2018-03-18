# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 下午1:59
# @Author  : huangzhengwei
# @Site    : 
# @File    : fileServer.py
# @Software: PyCharm

import sys
import os
import socket, json
import traceback
#reload(sys)

#sys.setdefaultencoding('utf8')
# reload(sys)

# sys.setdefaultencoding('utf8')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('', 9999))

server.listen(5)

i = 0
filename = "test"
while True:
	conn, addr = server.accept()
	print('conn is addr :', addr)
	while True:
		json_obj = conn.recv(1024)
		try:
			file_info = json.loads(json_obj)
			filesize = file_info['filesize']
			filename = file_info['filename']
			filesize = file_info['filesize']
			print('filename=', filename, 'filesize=', filesize)
			filename = os.path.join("../faceNet/unknowDatasource", filename)
			filesize = file_info['filesize']
			recevie_size = 0
			myfile = open(filename, 'wb')
			while recevie_size < filesize:

				filedata = conn.recv(1024)
				myfile.write(filedata)
				recevie_size += len(filedata)
			else:
				myfile.close()
				print('receive file finished!')
				break
		except BaseException:
			traceback.print_exc()
			print ("%s is error" % filename)
			break
	conn.close()
