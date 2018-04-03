import glob, os, shutil, random, re
import cv2
import path as PATH
from lumine import Lumine

class Reverse(Lumine):

    def reverse(self):

        for PF in glob.iglob(os.path.join(self.image_path, "*")):
            self.image_name, ext = os.path.splitext(os.path.basename(PF))
            self.read_image(ext)

            if self.src is not None:
                self.img = cv2.flip(self.src, 1)
                cv2.imwrite(os.path.join(self.image_path, self.image_name+'_in'+'.jpg'), self.img)
                self.add_label('_in')

    def x_reverse(self, x):
        x = abs(x*640-640)/640
        return str(round(x, 7))


    def add_label(self, signal):

        #元画像のラベルファイルを取り出し
        labelfile = str(self.label_path + self.image_name + '.txt')
        newlabel = str(self.label_path + self.image_name + '_in.txt')

        num, x_point, y_point, width, height = [], [], [], [], []
        with open(labelfile, 'r') as fp:
            for line in fp: 
                data = re.split(" ", line)

                num.append(str(data[0])) 
                x_point.append(float(data[1]))
                y_point.append(str(data[2]))
                width.append(str(data[3]))
                height.append(str(data[4]))

            x_point = map(self.x_reverse, x_point)

        with open(newlabel, 'w') as fp:
            for (n, x, y, w, h) in zip(num, x_point, y_point, width, height):
                fp.write(n + ' ' + x + ' ' + y + ' ' + w + ' ' + h)
    
if __name__ == "__main__":

    paths = PATH.file_path()

    hanten = Reverse(paths[0], paths[1])
    hanten.reverse()
