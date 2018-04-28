#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QDockWidget, QMenuBar, QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit, QAction, QFileDialog, QGridLayout, QApplication, QPushButton, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import xml.etree.ElementTree as et

class FilePath(QWidget):

    def __init__(self, parent=None):
        super(FilePath, self).__init__(parent)
        self.initUI()

    def image_path_dir(self):
        self.image_label = QLabel("image path", self)
        self.image_path = QPushButton("Choose", self)
        self.image_path.clicked.connect(self.show_image_path)
        self.image_edit = QLineEdit(self)

        self.paths = QGridLayout()
        self.paths.setSpacing(10)
 
        self.paths.addWidget(self.image_label, 0, 0)
        self.paths.addWidget(self.image_edit, 0, 1)
        self.paths.addWidget(self.image_path, 0, 2)

    def label_path_dir(self):
        self.label_label = QLabel("label path", self)
        self.label_path = QPushButton("Choose", self)
        self.label_path.clicked.connect(self.show_label_path)
        self.label_edit = QLineEdit(self)

        self.paths.addWidget(self.label_label, 1, 0)
        self.paths.addWidget(self.label_edit, 1, 1)
        self.paths.addWidget(self.label_path, 1, 2)

    def OK_or_Cancel(self):
        self.Write = QPushButton("OK", self)
        self.Write.clicked.connect(self.write_path)
        self.Cancel = QPushButton("Cancel", self)
        self.Cancel.clicked.connect(QCoreApplication.instance().quit)


    def initUI(self):

        self.image_path_dir()
        self.label_path_dir()
        self.OK_or_Cancel()

        YN = QHBoxLayout()
        YN.addStretch(1)
        YN.addWidget(self.Write)
        YN.addWidget(self.Cancel)

        allwid = QVBoxLayout()
        allwid.addStretch(1)
        allwid.addLayout(self.paths)
        allwid.addLayout(YN)

        self.setLayout(allwid)

    def write_path(self, pressed):

        try:
            tree = et.ElementTree()
            tree.parse("path.xml")
        except:
            print("xml file error!!!  check path.xml!!!")
            return -1

        path = self.image_edit.text()
        if path:
            new_image = tree.find('image_path')
            new_image.text = path
            tree.write('path.xml', 'utf-8', True)
            path = None

        path = self.label_edit.text()
        if path:
            new_image = tree.find('image_path')
            new_label = tree.find('label_path')
            new_label.text = path
            tree.write('path.xml', 'utf-8', True)
        
        QApplication.quit()

    def show_image_path(self, pressed):
        dir_path = QFileDialog.getExistingDirectory(self, 'find directory', '/home', QFileDialog.ShowDirsOnly)

        if dir_path:
            self.image_edit.setText(dir_path + "/")

    def show_label_path(self, pressed):
        dir_path = QFileDialog.getExistingDirectory(self, 'find directory', '/home', QFileDialog.ShowDirsOnly)

        if dir_path:
            self.label_edit.setText(dir_path + "/")

class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.mainUI()

    def mainUI(self):

        openFile = QAction(QIcon('Multi.jpg'), 'Exit', self)
        openFile.setShortcut('Ctrl+Q')
        openFile.setStatusTip('Close the Window')
        openFile.triggered.connect(QCoreApplication.instance().quit)

        menu = self.menuBar()
        filemenu = menu.addMenu('&close')
        filemenu.addAction(openFile)

        self.setCentralWidget(FilePath(self))

        self.setGeometry(300, 300, 650, 150)
        self.setWindowTitle('File dialog')
        self.setWindowIcon(QIcon('Multi.jpg'))
        self.show()

if __name__ == "__main__":

        app = QApplication(sys.argv)
        ex = MyMainWindow()
        sys.exit(app.exec_())
