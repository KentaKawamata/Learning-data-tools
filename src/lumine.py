import numpy as np
import glob, os, sys, re
import cv2

file_path = os.path.dirname(os.path.abspath(__file__))

for pathAndFilename in glob.iglob(os.path.join(file_path, "*.png")):
    image, ext = os.path.splitext(os.path.basename(pathAndFilename))

    src = cv2.imread(image + '.png')

    #if src is not None:
    #    img = (src-np.mean(src))/np.std(src)*32+120 #標準偏差32,平均120に変更
    #    cv2.imwrite(image + '_1.png', img)

    if src is not None:
        img = (src-np.mean(src))/np.std(src)*16+120 #標準偏差16,平均120に変更
        cv2.imwrite(image + '_X.png', img)


