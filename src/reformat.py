import glob, os, shutil
import cv2
import datetime
import path as PATH

def reformat(image_path, label_path):

    PathAndFile = glob.iglob(os.path.join(image_path, "*.png"))

    for i, PF in enumerate(PathAndFile, 1):  

        today = datetime.date.today()
        #today = today - datetime.timedelta(days=1)

        #画像データの名前のみ取り込み
        title, ext = os.path.splitext(os.path.basename(PF))

        IMG = cv2.imread(title + '.png')
        newname = str(today) + '_' + str("{0:04d}".format(i))
        cv2.imwrite(image_path + newname + '.jpg', IMG)

        shutil.copyfile(label_path + title + '.txt', label_path + newname + ".txt")

if __name__ == '__main__':

    paths = PATH.file_path()

    reformat(paths[0], paths[1])
