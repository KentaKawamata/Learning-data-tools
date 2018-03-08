#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob, os, shutil, random, re
import subprocess

def add_label(image_path, label_path):

    image_data = os.listdir(image_path)

    for path_file in glob.glob(os.path.join(image_path, "*.jpg")):  

        #画像fileの名前のみ取り出し
        image, ext = os.path.splitext(os.path.basename(path_file))

        #画像の名前と一致する名前のラベルを探す
        if os.path.isfile(label_path + image + ".txt") is False:
        
            print(image)
            #水増し前の大本の画像のラベル取り出し
            image_base = image.replace('_A', '') 
            image_base = image_base.replace('_B', '')
            print(image_base)
            label_base, ext = os.path.splitext(os.path.basename(label_path + image_base + ".txt"))
            #print(label_base + "           label_base")

            shutil.copyfile(label_path + label_base + '.txt', label_path + image + ".txt")

if __name__ == '__main__':

    #画像保存先とラベル保存先指定
    image_path = "//"
    label_path = "//"

    add_label(image_path, label_path)
