import numpy as np
import glob, os, sys, re
import cv2

file_path = os.path.dirname(os.path.abspath(__file__))

for pathAndFilename in glob.iglob(os.path.join(file_path, "*")):
    image, ext = os.path.splitext(os.path.basename(pathAndFilename))

    print(ext)
    if str(ext) == ".png":
        src = cv2.imread(image + '.png')
    elif str(ext) == ".jpg":
        src = cv2.imread(image + '.jpg')
    else:
        src = None
    print(src)

    if src is not None:
        img = (src-np.mean(src))/np.std(src)*32+120 #標準偏差32,平均120に変更
        cv2.imwrite(image + '_V.png', img)

    if src is not None:
        img = (src-np.mean(src))/np.std(src)*16+120 #標準偏差16,平均120に変更
        cv2.imwrite(image + '_X.jpg', img)

    if src is not None:
        average_square = (10, 10)
        noize = cv2.blur(src, average_square)
        cv2.imwrite(image + '_G.jpg', img)
        
    if src is not None:
        row, col, ch = src.shape
        mean = 0
        sigma = 15
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        gauss_img = src + gauss
        cv2.imwrite(image + '_Ge.jpg', gauss_img)
