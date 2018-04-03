import glob, os, shutil
import cv2
import datetime
import path as PATH
from lumine import Lumine

class Reformat(Lumine):
    def __init__(self, image_path, label_path):
        super().__init__(image_path, label_path)
        self.new_image_name = None
        self.today = datetime.date.today()

    def reformat(self):
        #self.today = self.today - datetime.timedelta(days=1)
        PF = glob.iglob(os.path.join(self.image_path, "*"))

        i=0
        for img_origin in PF:  
            i+=1
            self.image_name, ext = os.path.splitext(os.path.basename(img_origin))
            self.read_image(ext)
            if self.src is not None:
                self.rewrite(i)
            else:
                i-=1


    def rewrite(self, i):
        self.new_image_name = str(self.today)+'_'+str("{0:04d}".format(i))
        if self.new_image_name != self.image_name:
            cv2.imwrite(os.path.join(self.image_path, self.new_image_name+'.jpg'), self.src)
            self.add_label(self.new_image_name)
        else:
            print("A same name file is existence in" + str(self.image_path))
            pass 
    
if __name__ == '__main__':

    paths = PATH.file_path()

    re_name_format = Reformat(paths[0], paths[1])

    re_name_format.reformat()
