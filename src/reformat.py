import glob, os
import cv2

def reformat():

    # 画像データパス
    #current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = '/Your/directory/path/'

    # 出力先ディレクトリ
    path_data = '/Your/directory/path/'

    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):  

        #画像データの名前のみ取り込み
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        IMG = cv2.imread(title + '.png')
        cv2.imwrite(os.path.join(path_data, title + '.jpg'), IMG)

if __name__ == '__main__':

    reformat()
