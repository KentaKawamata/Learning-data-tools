import glob, os, shutil, random, re
import subprocess

def extract(image_path, label_path, image_tmp, label_tmp, sheets):

    

    #ディレクトリ中からランダムにsheets枚取り出し
    image_data = os.listdir(image_path)
    images = random.sample(image_data, sheets)


for image in images:
    image = str(image)
    label = re.sub(re.compile(".jpg"), ".txt", image)

    shutil.copy(image_path + image, image_tmp)
    shutil.copy(label_path + label, label_tmp)

if __name__ == '__main__':

    #画像とラベルのパス
    image_path = "/image/data/directory/path/"
    label_path = "/label/data/directory/path/"

    #画像トラベルのコピー先パス
    image_tmp = "/image/data/temp/directory/path/"
    label_tmp = "/label/data/temp/directory/path/"

    #取り出す枚数
    random = 100

    extract(image_path, label_path, image_tmp, label_tmp, random)
