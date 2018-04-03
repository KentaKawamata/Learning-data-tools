#!/usr/bin/env python
# -*- coding: utf-8 -*-
import reformat as RF
import invert as IN
import lumine as LU
import label as LA
import path as PATH
import process

def main():

    paths = PATH.file_path()

    rename = RF.Reformat(paths[0], paths[1])
    rename.reformat()
    hanten = IN.Reverse(paths[0], paths[1])
    hanten.reverse()
    mizumashi = LU.Lumine(paths[0])
    mizumashi.mashi()
    process.process(paths[0])

if __name__ == "__main__":

    main()
