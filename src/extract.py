import glob, os, shutil, random, re
import subprocess

image_path = "/image/data/directory/path/"
label_path = "/label/data/directory/path/"

image_tmp = "/image/data/temp/directory/path/"
label_tmp = "/label/data/temp/directory/path/"

image_data = os.listdir(image_path)
sheets = 100

images = random.sample(image_data, sheets)


for image in images:
    image = str(image)
    label = re.sub(re.compile(".jpg"), ".txt", image)

    shutil.copy(image_path + image, image_tmp)
    shutil.copy(label_path + label, label_tmp)
