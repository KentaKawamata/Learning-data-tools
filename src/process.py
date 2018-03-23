import glob, os
import path as PATH

def process(image_path):

    # Current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Percentage of images to be used for the test set
    percentage_test = 10;

    # Create and/or truncate train.txt and test.txt
    file_train = open(os.path.join(image_path, 'train.txt'), 'w')  
    file_test = open(os.path.join(image_path, 'test.txt'), 'w')

    # Populate train.txt and test.txt
    counter = 1  
    index_test = round(100 / percentage_test)  
    for PF in glob.iglob(os.path.join(image_path, "*.jpg")):  

        title, ext = os.path.splitext(os.path.basename(PF))

        if counter == index_test:
            counter = 1
            file_test.write(image_path + title + '.jpg' + "\n")
        else:
            file_train.write(image_path + title + '.jpg' + "\n")
            counter = counter + 1

if __name__ == "__main__":

    paths = PATH.file_path()

    process(paths[0])
