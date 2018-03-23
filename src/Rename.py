import sys, os, re
import datetime
import path as PATH

def rename(image_path):

    files = os.listdir(image_path)
    files.sort()

    today = datetime.date.today()
    #today = today - datetime.timedelta(days=1)

    for i, image in enumerate(files):

        image = os.path.join(image_path, image)
        reimage = os.path.join(image, str(today) + '_' + str("{0:03d}".format(i)) + '.jpg')

    os.rename(image, reimage)

if __name__ == "__main__":

    paths = PATH.file_path()
    rename(paths[0])
