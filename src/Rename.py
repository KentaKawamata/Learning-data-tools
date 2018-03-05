import sys, os, re
import datetime

file_path = "/your/directory/path/"
files = os.listdir(file_path)
files.sort()

today = datetime.date.today()
#today = today - datetime.timedelta(days=1)

for i, image in enumerate(files):

    image = os.path.join(file_path, image)
    reimage = os.path.join(file_path, str(today) + '_' + str("{0:03d}".format(i)) + '.png')

    os.rename(image, reimage)
