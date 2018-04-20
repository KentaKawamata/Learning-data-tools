import os
import glob
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img
from PIL import Image
import cv2
import path as PA

def draw_images(generator, x, dir_name, index):
    # 出力ファイルの設定
    save_name = 'images-' + str(index)
    g = generator.flow(x, batch_size=1, save_to_dir=dir_name, save_prefix=save_name, save_format='jpg')

    # 1つの入力画像から何枚拡張するかを指定
    # g.next()の回数分拡張される
    for i in range(2):
        bach = g.next()

if __name__ == '__main__':

    paths = PA.file_path()

    images = glob.iglob(os.path.join(paths[0], "*.jpg"))   

    generator = ImageDataGenerator(rotation_range=0, # 90°まで回転
                      width_shift_range=0, # 水平方向に
                      height_shift_range=0, # 垂直方向にランダムでシフト
                      channel_shift_range=25.0, # 色調をランダム変更
                      shear_range=0, # 斜め方向(pi/8まで)に引っ張る
                      horizontal_flip=False, # 垂直方向にランダムで反転
                      vertical_flip=False # 水平方向にランダムで反転
                      )

    for i,image in enumerate(images):

        img = Image.open(image)
        print(img,image)
        #img = load_img(img)
        # 画像を配列化して転置a
        x = np.asarray(img)
        x = np.expand_dims(x, axis=0)
        print(x.shape)
        draw_images(generator, x, paths[0], i)


