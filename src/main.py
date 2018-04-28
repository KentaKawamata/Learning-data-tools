#!/usr/bin/env python
# -*- coding: utf-8 -*-
import reformat
import invert
import lumine
import label as LA
import path as PATH
import process
import change_color as BGR

def main():

    paths = PATH.file_path()
    if paths[0] in None:
        print("-------No path of images-------")
        return -1
    elif paths[1] in None:
        print("-------No path of labels-------")
        return -1

    print("-------Start reformat and rename-------")
    rename = reformat.Reformat(paths[0], paths[1])
    rename.reformat()
    print("-------End reformat and rename-------")

    print("-------Start reverse images-------")
    hanten = invert.Reverse(paths[0], paths[1])
    hanten.reverse()
    print("-------End reverse images-------")

    print("-------Start increase images other color images-------")
    chenge_color = BGR.COLOR(paths[0], paths[1])
    change_color.rgb()
    print("-------End increase images other color images-------")

    
    mizumashi = lumine.Lumine(paths[0])
    mizumashi.mashi()
    process.process(paths[0])

if __name__ == "__main__":

    main()
