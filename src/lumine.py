import numpy as np
import glob, os, sys, re
import cv2
import path as PATH
from tqdm import tqdm

def mizumashi(Ipath):

    images = glob.iglob(os.path.join(Ipath, "*"))
    num = 0

    for i, P in enumerate(images):
        num = num + 1

    pbar = tqdm(total=int(num))
    images = glob.iglob(os.path.join(Ipath, "*"))

    for i, PF in enumerate(tqdm(images)):
        image, ext = os.path.splitext(os.path.basename(PF))

        if str(ext) == ".png":
            src = cv2.imread(os.path.join(Ipath, image+ext), 1)
        elif str(ext) == ".jpg":
            src = cv2.imread(os.path.join(Ipath, image+ext), 1)
        else:
            src = None

        if src is not None:
            #標準偏差32,平均120に変更
            img = (src-np.mean(src))/np.std(src)*32+120
            cv2.imwrite(os.path.join(Ipath, image+'_V.jpg'), img)

        if src is not None:
            #標準偏差16,平均120に変更
            img = (src-np.mean(src))/np.std(src)*16+120
            cv2.imwrite(os.path.join(Ipath, image+'_X.jpg'), img)

        if src is not None:
            average_square = (10, 10)
            img = cv2.blur(src, average_square)
            cv2.imwrite(os.path.join(Ipath, image+'_Ge.jpg'), img)
        
        if src is not None:
            row, col, ch = src.shape
            mean = 0
            sigma = 15
            gauss = np.random.normal(mean, sigma, (row, col, ch))
            gauss = gauss.reshape(row, col, ch)
            gauss_img = src + gauss
            cv2.imwrite(os.path.join(Ipath, image+'_G.jpg'), gauss_img)

        pbar.update(1)

if __name__ == "__main__":

    paths = PATH.file_path()

    mizumashi(paths[0])
