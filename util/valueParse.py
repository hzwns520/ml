#_*_coding:utf-8_*_
__author__="huangzhengwei"
CONFIGDIR = "../config/nametodir"

def getNameDict():
    lines = list()
    valueDict = dict()
    with open(CONFIGDIR) as f:
        lines = f.readlines()
    for line in lines:
        tmp_list = line.split("###")
        if len(tmp_list) == 2:
            print tmp_list
            valueDict[tmp_list[0]] = tmp_list[1].replace("\n", "")
    return valueDict

def writeNameConfig(name, dir):
    content = "%s###%s\n" % (dir, name)
    with open(CONFIGDIR, "a") as f:
        f.write(content)


