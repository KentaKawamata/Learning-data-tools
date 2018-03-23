#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob, os, shutil, random, re
import path as PATH

def extract(image_path, label_path, image_tmp, label_tmp, sheets):

    image_data = []
    #ディレクトリ中からランダムにsheets枚取り出し
    for PF in glob.glob(os.path.join(image_path, "*.jpg")):  

        image, ext = os.path.splitext(os.path.basename(PF))
        image_data.append(str(image + ext))
    
    images = random.sample(image_data, sheets)

    for image in images:
        image = str(image)
        label = re.sub(re.compile(".jpg"), ".txt", image)

        shutil.copy(image_path + image, image_tmp)
        shutil.copy(label_path + label, label_tmp)

if __name__ == '__main__':

    #取り出す枚数
    number = 100
    paths = PATH.file_path()
    extract(paths[0], paths[1], paths[2], paths[3], number)
