import reformat as RF
import invert as IN
import lumine as LU
import label as LA
import path as PATH
import process

def main():

    paths = PATH.file_path()

    RF.reformat(paths[0], paths[1])
    IN.reverse(paths[0], paths[1])
    LU.mizumashi(paths[0])
    LA.add_label(paths[0], paths[1])
    process.process(paths[0])

if __name__ == "__main__":

    main()
