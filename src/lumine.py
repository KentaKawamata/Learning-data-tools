import numpy as np
import glob, os, sys, re
import cv2
import datatime

file_path = "/your/directory/path/"
files = os.listdir(file_path)
files.sort()


for i, src in enumerate(files):

    img = src*1.2 #輝度値が2倍になる
    reimage = os.path.join(file_path, str(today) + '_' + str("{0:03d}".format(i)) + 1 + '.img')
    cv2.imwrite(reimage, img)

    img = src + 40 #輝度値のベースが40上がる
    reimage = os.path.join(file_path, str(today) + '_' + str("{0:03d}".format(i)) + 2 + '.img')
    cv2.imwrite(reimage, img)

    img = (img-np.mean(src))/np.std(src)*32+120 #標準偏差32,平均120に変更
    reimage = os.path.join(file_path, str(today) + '_' + str("{0:03d}".format(i)) + 3 + '.img')
    cv2.imwrite(reimage, img)

    img = (img-np.mean(src))/np.std(src)*16+120 #標準偏差16,平均120に変更
    reimage = os.path.join(file_path, str(today) + '_' + str("{0:03d}".format(i)) + 4 + '.img')
    cv2.imwrite(reimage, img)


