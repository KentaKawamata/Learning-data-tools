import glob, os, shutil, random, re
import cv2

def reverse():

    image_dir = "/home/image/testimage/"
    label_dir = "/home/image/testlabel/"

    for pathAndFile in glob.iglob(os.path.join(image_dir, "*")):
        image, ext = os.path.splitext(os.path.basename(pathAndFile))

        if str(ext) == ".png":
            src = cv2.imread(image_dir + image + '.png')
        elif str(ext) == ".jpg":
            src = cv2.imread(image_dir + image + '.jpg')
        else:
            src = None
  
        #cv2.flipで画像を左右反転
        if src is not None:
            img = cv2.flip(src, 1)
            cv2.imwrite(image_dir + image + '_in' + '.jpg', img)

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
    
if __name__ == "__main__":

    reverse()
