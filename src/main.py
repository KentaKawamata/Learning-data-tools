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
    mizumashi = LU.Lumine(paths[0])
    mizumashi.mashi()
    process.process(paths[0])

if __name__ == "__main__":

    main()
