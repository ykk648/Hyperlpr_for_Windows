#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import mainframe_ui

from batch import batch_main

from openpyxl import Workbook
# from openpyxl import load_workbook

class MainWindow(QtWidgets.QMainWindow, mainframe_ui.Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.init_directory = ''

        self.filename_list = []
        self.colors = []
        self.predict_list = []
        self.step = 0

        # self.Title.setText("hello Python")
        # self.World.clicked.connect(self.onWorldClicked)
        # self.China.clicked.connect(self.onChinaClicked)
        # self.lineEdit.textChanged.connect(self.onlineEditTextChanged)
        self.pushButton.clicked.connect(self.msg)
        self.pushButton_3.clicked.connect(self.my_platerecognize)
        self.pushButton_2.clicked.connect(self.savefile)

    # def timerEvent(self, event):
    #     if self.step >=100:
    #         self.timer.stop()
    #         return
    #     self.step = self.step + 1
    #     self.progressBar.setValue(self.step)

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')

    def savefile(self):
        filename2, ok2 = QFileDialog.getSaveFileName(self,
                                    "文件保存",
                                    "C:/",
                                    "Excel files(*.xlsx , *.xls)")
        print(filename2)

        wb = Workbook()
        sheet = wb.active
        for i in range(len(self.filename_list)):
            sheet["A{}".format(i+1)].value = self.predict_list[i]
            sheet["B{}".format(i+1)].value = self.colors[i]
            sheet["C{}".format(i+1)].value = self.filename_list[i]  # +'.jpg'

        wb.save(filename2)

    def msg(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "C:/")  # 起始路径
        print(directory1)
        self.init_directory = directory1


    def my_platerecognize(self):
        self.filename_list,self.colors,self.predict_list = batch_main(self.init_directory)
