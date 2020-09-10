#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 19:15
# @Author  : wfo-12
# @FileName: Play.py
# @Software: PyCharm
# @Blog    : https://www.cnblogs.com/jvav/
# @Github  : https://github.com/Wfo-12

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtGui import QIcon
from Calculate import *

class Play:

    array = []
    string = ''
    flag = 0
    len = 0

    def __init__(self):
        # 从文件中加载ui文件
        qfile_play = QFile("ui/main.ui")
        qfile_play.open(QFile.ReadOnly)
        qfile_play.close()

        # 从ui文件动态创建窗口对象
        self.ui = QUiLoader().load(qfile_play)
        self.ui.listWidget.clicked.connect(self.setArray)
        self.ui.pushButton.clicked.connect(self.popArray)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.pushButton_3.clicked.connect(self.run)

    def setArray(self):
        if self.flag:
            self.array = []
            self.flag = 0
            for i in range(self.len):
                self.ui.tableWidget.removeRow(0)
        self.array.append(self.ui.listWidget.currentItem().text())
        self.refresh()

    def popArray(self):
        try:
            self.array.pop()
            self.refresh()
        except:
            pass

    def refresh(self):
        self.string = ' '.join(self.array)
        self.ui.lineEdit.setText(self.string)

    def clear(self):
        self.array = []
        self.refresh()
        for i in range(self.len):
            self.ui.tableWidget.removeRow(0)
        self.flag = 0

    def run(self):
        self.flag = 1
        Cal = Calculate(self.array)
        Cal.run()
        Cal.resultList.reverse()
        self.len = len(Cal.resultList)
        for i in range(self.len):
            self.ui.tableWidget.insertRow(i)
            item = QTableWidgetItem()
            item.setText('     ' + Cal.resultList[i][0])
            self.ui.tableWidget.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setText('     ' + Cal.resultList[i][1])
            self.ui.tableWidget.setItem(i, 1, item)


app = QApplication()
app.setWindowIcon(QIcon('img/logo.png'))
window = Play()
window.ui.show()
app.exec_()