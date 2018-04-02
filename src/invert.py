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

                x_beyond = []
                for x in x_point:
                    x = abs(x*640-640)/640
                    x_beyond.append(str(round(x, 7)))

                with open(newlabel, 'w') as fp:
                    for (n, x, y, w, h) in zip(num, x_beyond, y_point, width, height):
                        fp.write(n + ' ' + x + ' ' + y + ' ' + w + ' ' + h)
    

'''
def reverse(image_dir, label_dir):

  
        #cv2.flipで画像を左右反転
        if src is not None:
            img = cv2.flip(src, 1)
            cv2.imwrite(os.path.join(image_dir, image+'_in'+'.jpg'), img)

        #元画像のラベルファイルを取り出し
        labelfile = str(label_dir + image + '.txt')
        newlabel = str(label_dir + image + '_in.txt')

        num, x_point, y_point, width, height = [], [], [], [], []
        with open(labelfile, 'r') as fp:
            for line in fp: 
                data = re.split(" ", line)

                num.append(str(data[0])) 
                x_point.append(float(data[1]))
                y_point.append(str(data[2]))
                width.append(str(data[3]))
                height.append(str(data[4]))

        x_beyond = []
        for x in x_point:
            x = abs(x*640-640)/640
            x_beyond.append(str(round(x, 7)))

        with open(newlabel, 'w') as fp:
            for (n, x, y, w, h) in zip(num, x_beyond, y_point, width, height):
                fp.write(n + ' ' + x + ' ' + y + ' ' + w + ' ' + h)
'''

if __name__ == "__main__":

    paths = PATH.file_path()

    hanten = Reverse(paths[0], paths[1])
    hanten.reverse()
