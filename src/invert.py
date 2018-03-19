import glob, os, shutil, random, re
import cv2

image_dir = "/home/image/testimage/"
label_dir = "/home/image/testlabel/"

for pathAndFile in glob.iglob(os.path.join(image_dir, "*")):
    image, ext = os.path.splitext(os.path.basename(pathAndFile))

    print(ext)
    if str(ext) == ".png":
        src = cv2.imread(image_dir + image + '.png')
    elif str(ext) == ".jpg":
        src = cv2.imread(image_dir + image + '.jpg')
    else:
        src = None
  
    if src is not None:
        inverse = cv2.flip(src, 1)
        cv2.imwrite(image_dir + image + '_in' + '.jpg', inverse)

    labelfile = str(label_dir + image + '.txt')

    n, x, y, w, h = [], [], [], [], []
    with open(labelfile, 'r') as fp:
        for line in fp: 
            data = re.split(" ", line)

            n.append(str(data[0])) 
            x.append(float(data[1]))
            y.append(str(data[2]))
            w.append(str(data[3]))
            h.append(str(data[4]))

    print(x)
    x_beyond = []

    for xl in x:
        xl = abs(xl*640-640)/640
        x_beyond.append(str(round(xl, 7)))

    newlabel = str(label_dir + image + '_in.txt')

    with open(newlabel, 'w') as fp:
        for i, nu in enumerate(n):
            fp.write(nu + ' ' + x_beyond[i] + ' ' + y[i] + ' ' + w[i] + ' ' + h[i])
    
                    
