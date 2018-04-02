#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import glob, os, sys, re, shutil
import cv2
import path as PATH
from tqdm import tqdm

class Lumine():
    def __init__(self, Ipath, Lpath):
        self.num = 0
        self.src = None
        self.image_path = Ipath
        self.label_path = Lpath
        self.images = []
        self.pbar = None
        self.img = None
        self.image_name = None
        self.img = None

    def mashi(self):

        print("------start multiply images------")
        self.images = glob.iglob(os.path.join(self.image_path, "*"))
        self.count(self.images)
        self.images = glob.iglob(os.path.join(self.image_path, "*"))

        for i, PF in enumerate(tqdm(self.images)):
            self.image_name, ext = os.path.splitext(os.path.basename(PF))

            self.search_format(ext)

            if self.src is not None:
                self.normalization(32, 120, '_N32')       
                self.normalization(16, 120, '_N16')       
                self.median()
                self.gauss()

            self.pbar.update(1)

        print("\n------end multiply images------")

    def search_format(self, f):
        if str(f) == ".png" or str(f) == ".jpg":
            self.src = cv2.imread(os.path.join(self.image_path, self.image_name+f), 1)
        else:
            self.src = None

    def count(self, files):
        for i, P in enumerate(files):
            self.num = self.num + 1
        self.pbar = tqdm(total=int(self.num))

    def write_image(self, signal):
        new_name = self.image_name + signal
        cv2.imwrite(os.path.join(self.image_path, new_name + '.jpg'), self.img)
        self.add_label(new_name)

    def add_label(self, new_filename):
        shutil.copyfile(self.label_path + self.image_name + '.txt', self.label_path + new_filename + ".txt")

    def normalization(self, hensa, avrage, signal):
        self.img = (self.src-np.mean(self.src))/np.std(self.src)*hensa+avrage
        self.write_image(signal)

    def median(self):
        average_square = (10, 10)
        self.img = cv2.blur(self.src, average_square)
        self.write_image('_M')

    def gauss(self):
        row, col, ch = self.src.shape
        mean = 0
        sigma = 15
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        self.img = self.src + gauss
        self.write_image('_G')

if __name__ == "__main__":

    paths = PATH.file_path()

    mizumashi = Lumine(paths[0], paths[1])
    mizumashi.mashi()
