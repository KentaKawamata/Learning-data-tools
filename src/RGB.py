#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import glob, os, sys, re, shutil
import cv2
import path as PATH
from tqdm import tqdm
from lumine import Lumine

class RGB(Lumine):

    def rgb(self):

        print("------start RGB images------")
        
        self.images = glob.iglob(os.path.join(self.image_path, "*"))
        self.count(self.images)
        self.images = glob.iglob(os.path.join(self.image_path, "*"))
        
        for i, PF in enumerate(tqdm(self.images)):
            self.image_name, ext = os.path.splitext(os.path.basename(PF))
            self.read_image(ext)

            if self.src is not None:
                self.Blue(0.9, 0.625, 0.8)
                self.Green(0.625, 0.9, 0.8)

            self.pbar.update(1)

        print("\n------end RGB images------")

    def Blue(self, b_param, g_param, r_param):
        b,g,r = cv2.split(self.src)
       
        b = np.float64(b)
        g = np.float64(g)
        r = np.float64(r)

        blue = b*b_param
        green = g*g_param
        red = r*r_param

        self.img = cv2.merge((blue, green, red))
        self.write_image('_blue')

    def Green(self, b_param, g_param, r_param):
        b,g,r = cv2.split(self.src)
       
        b = np.float64(b)
        g = np.float64(g)
        r = np.float64(r)

        blue = b*b_param
        green = g*g_param
        red = r*r_param

        self.img = cv2.merge((blue, green, red))
        self.write_image('_green')

if __name__ == "__main__":

    paths = PATH.file_path()

    color = RGB(paths[0], paths[1])
    color.rgb()
