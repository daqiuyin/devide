# -*- coding: utf-8 -*-
import os
import time
import sys


def mkSubFile(lines,head,srcName,sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str(sub) + extname
    print( 'make file: %s' %filename)
    fout = open(filename,'w')
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()


def splitByLineCount(filename, count):
    filepath = os.path.join(sys.path[0],filename)
    with open(filepath) as fin:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == int(count):
                sub = mkSubFile(buf, head, filepath, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filepath, sub)


if __name__ == '__main__':
    begin = time.time()
    InputContent=input('文件名：每个文件数据量\n').split(',')
    splitByLineCount(*InputContent)
    end = time.time()
    print('time is %d seconds ' % (end - begin))



    # @Time    : 2018/3/30 13:49
# @Auth    : DAQIUYIN
# @File    : devide.py.py
# @SoftWare: PyCharm Community Edition