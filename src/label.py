import glob, os, shutil, random, re
import subprocess

<<<<<<< HEAD
image_path = "/path/"
label_path = "/path/"

image_data = os.listdir(image_path)

for path_file in glob.glob(os.path.join(image_path, "*.png")):  

    #画像fileの名前のみ取り出し
    image, ext = os.path.splitext(os.path.basename(path_file))

    #labelを探す
    #label = re.sub(re.compile(".jpg"), ".txt", image)
    #label = glob.glob(label_path + image + ".txt")
    #print(image)

    if os.path.isfile(label_path + image + ".txt") is False:
        
        #水増し前の大本の画像のラベル取り出し
        image_base = image.replace("_X", "") 
        #print(image_base)
        #label_base = glob.glob(label_path + image_base + ".txt")
        label_base, ext = os.path.splitext(os.path.basename(label_path + image_base + ".txt"))
        print(label_base + "           label_base")

        #label = re.sub(re.compile(".jpg"), ".txt", image)
        shutil.copyfile(label_path + label_base + '.txt', label_path + image + ".txt")
=======
def add_label(image_path, label_path):

    image_data = os.listdir(image_path)

    for path_file in glob.glob(os.path.join(image_path, "*.png")):  

        #画像fileの名前のみ取り出し
        image, ext = os.path.splitext(os.path.basename(path_file))

        #画像の名前と一致する名前のラベルを探す
        if os.path.isfile(label_path + image + ".txt") is False:
        
            #水増し前の大本の画像のラベル取り出し
            image_base = image.replace("_X", "") 
            label_base, ext = os.path.splitext(os.path.basename(label_path + image_base + ".txt"))
            print(label_base + "           label_base")

            shutil.copyfile(label_path + label_base + '.txt', label_path + image + ".txt")

if __name__ == '__main__':

    #画像保存先とラベル保存先指定
    image_path = "/path/"
    label_path = "/path/"

    add_label(image_path, label_path)
>>>>>>> private
