import os
import glob
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img
from PIL import Image
import cv2 
def draw_images(generator, x, dir_name, index):
    # 出力ファイルの設定
    save_name = 'images-' + str(index)
    g = generator.flow(x, batch_size=1, save_to_dir=output_dir, save_prefix=save_name, save_format='jpg')

    # 1つの入力画像から何枚拡張するかを指定
    # g.next()の回数分拡張される
    for i in range(10):
        bach = g.next()
if __name__ == '__main__':
    # 出力先ディレクトリの設定
    output_dir = "extended"
    if not(os.path.exists(output_dir)):
         os.mkdir(output_dir)
    images = glob.glob('*.jpg')
        
    print(images)
    generator = ImageDataGenerator(rotation_range=90, # 90°まで回転
                      width_shift_range=0.1, # 水平方向に
                      height_shift_range=0.1, # 垂直方向にランダムでシフト
                      channel_shift_range=50.0, # 色調をランダム変更
                      shear_range=0.39, # 斜め方向(pi/8まで)に引っ張る
                      horizontal_flip=True, # 垂直方向にランダムで反転
                      vertical_flip=True # 水平方向にランダムで反転
                      )
    for i,image in enumerate(images):
        img = Image.open(image)
        print(img,image)
        #img = load_img(img)
        # 画像を配列化して転置a
        x = np.asarray(img)
        x = np.expand_dims(x, axis=0)
        print(x.shape)
        draw_images(generator, x, output_dir, i)
