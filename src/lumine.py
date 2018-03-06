import numpy as np
import glob, os, sys, re
import cv2
<<<<<<< HEAD
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


=======

def lumine(file_path):

    for pathAndFilename in glob.iglob(os.path.join(file_path, "*.png")):

        image, ext = os.path.splitext(os.path.basename(pathAndFilename))
        src = cv2.imread(image + '.png')

        #標準偏差32,平均120に変更
        #if src is not None:
        #    img = (src-np.mean(src))/np.std(src)*32+120
        #    cv2.imwrite(image + '_1.png', img)

        #標準偏差16,平均120に変更
        if src is not None:
            img = (src-np.mean(src))/np.std(src)*16+120
            cv2.imwrite(image + '_X.png', img)

if __name__ == '__main__':

    #現在スクリプトが存在するディレクトリのパスを取り出し
    file_path = os.path.dirname(os.path.abspath(__file__))

    lumine(file_path)
>>>>>>> private
