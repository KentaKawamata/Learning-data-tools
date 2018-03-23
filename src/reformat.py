import glob, os
import cv2
import path as PATH

def reformat(image_path):

    for PF in glob.iglob(os.path.join(image_path, "*.png")):  

        #画像データの名前のみ取り込み
        title, ext = os.path.splitext(os.path.basename(PF))

        IMG = cv2.imread(title + '.png')
        cv2.imwrite(os.path.join(image_path, title + '.jpg'), IMG)

if __name__ == '__main__':

    paths = PATH.file_path()

    reformat(paths[0])
