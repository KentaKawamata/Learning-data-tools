#!/usr/bin/env python
# -*- coding: utf-8 -*-
import path as PATH
import glob, os, shutil, random, re
import subprocess

class Add_label(image_p, label_p):
    def __init__(self):
        self.image_path = image_p
        self.label_path = label_p

    def labels(self, signal):
        
        for PF in glob.glob(os.path.join(self.image_path, "*.jpg")):  

            #画像fileの名前のみ取り出し
            image, ext = os.path.splitext(os.path.basename(PF))

            #画像の名前と一致する名前のラベルを探す
            if os.path.isfile(label_path + image + ".txt") is False:
                image_base = image.replace(signal, '') 
                label_base, ext = os.path.splitext(os.path.basename(self.label_path + image_base + ".txt"))
                shutil.copyfile(self.label_path + label_base + '.txt', self.label_path + image + ".txt")
            
def add_label(image_path, label_path):

    for path_file in glob.glob(os.path.join(image_path, "*.jpg")):  

        #画像fileの名前のみ取り出し
        image, ext = os.path.splitext(os.path.basename(path_file))

        #画像の名前と一致する名前のラベルを探す
        if os.path.isfile(label_path + image + ".txt") is False:
        
            print(image)
            #水増し前の大本の画像のラベル取り出し
            image_base = image.replace('_X', '') 
            image_base = image_base.replace('_V', '')
            image_base = image_base.replace('_Ge', '')
            image_base = image_base.replace('_G', '')
            print(image_base)
            label_base, ext = os.path.splitext(os.path.basename(label_path + image_base + ".txt"))

            shutil.copyfile(label_path + label_base + '.txt', label_path + image + ".txt")

if __name__ == '__main__':

    paths = PATH.file_path()

    add_label(paths[0], paths[1])
