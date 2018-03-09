import glob, os, shutil, random, re
import subprocess

image_path = "/inflation/"
label_path = "/labels/"

image_data = os.listdir(image_path)

for path_file in glob.glob(os.path.join(image_path, "*")):  

    #画像fileの名前のみ取り出し
    image, ext = os.path.splitext(os.path.basename(path_file))

    #labelを探す
    #label = re.sub(re.compile(".jpg"), ".txt", image)
    #label = glob.glob(label_path + image + ".txt")
    #print(image)
    #if str(ext) == ".jpg" or str(ext) == ".png":
    if str(ext) == ".jpg":

        if os.path.isfile(label_path + image + ".txt") is False:
        
            #水増し前の大本の画像のラベル取り出し
            image_base = image.replace("_V", "") 
            image_base = image_base.replace("_X", "") 
            image_base = image_base.replace("_Ge", "") 
            image_base = image_base.replace("_G", "") 
            #print(image_base)
            #label_base = glob.glob(label_path + image_base + ".txt")
            label_base, ext = os.path.splitext(os.path.basename(label_path + image_base + ".txt"))
            print(label_base + "           label_base")

            #label = re.sub(re.compile(".jpg"), ".txt", image)
            shutil.copyfile(label_path + label_base + '.txt', label_path + image + ".txt")
