import glob, os
import cv2

# Current directory
#current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = '/Your/directory/path/'

# Directory where the data will reside, relative to 'darknet.exe'
path_data = '/Your/directory/path/'

for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    IMG = cv2.imread(title + '.png')
    cv2.imwrite(os.path.join(path_data, title + '.jpg'), IMG)
