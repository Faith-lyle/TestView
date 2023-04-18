#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: TestView>>mainWidget.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/3/16-10:55
@IDE: PyCharm 
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QMouseEvent
from GUI.UI.UI_mainWidget import Ui_Form
from GUI.tabWidget import TabWidget


class MainWidget(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choose_index = 1
        self.slot_list = []
        for i in range(4):
            t = TabWidget()
            t.setParent(self.frame_2)
            self.horizontalLayout_10.addWidget(t)
            self.slot_list.append(t)
        self.choose_slot(self.choose_index)

    def choose_slot(self, index):
        for i in self.frame.children():
            if type(i) == QtWidgets.QFrame:
                i.setStyleSheet('background-color:#F0FFFF')
        for slot in self.slot_list:
            slot.setVisible(False)
        if index == 1:
            self.frame_3.setStyleSheet('background-color:#FAF0E6')
            self.slot_list[0].setVisible(True)
        elif index == 2:
            self.frame_4.setStyleSheet('background-color:#FAF0E6')
            self.slot_list[1].setVisible(True)
        elif index == 3:
            self.frame_5.setStyleSheet('background-color:#FAF0E6')
            self.slot_list[2].setVisible(True)
        elif index == 4:
            self.frame_6.setStyleSheet('background-color:#FAF0E6')
            self.slot_list[3].setVisible(True)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == 1:
            if self.frame_3.x() < a0.x() < (self.frame_3.x() + self.frame_3.width()) and self.frame_3.y() < a0.y() < (
                    self.frame_3.y() + self.frame_3.height()):
                self.choose_index = 1
            elif self.frame_4.x() < a0.x() < (self.frame_4.x() + self.frame_4.width()) and self.frame_4.y() < a0.y() < (
                    self.frame_4.y() + self.frame_4.height()):
                self.choose_index = 2
            elif self.frame_5.x() < a0.x() < (self.frame_5.x() + self.frame_5.width()) and self.frame_5.y() < a0.y() < (
                    self.frame_5.y() + self.frame_5.height()):
                self.choose_index = 3
            elif self.frame_6.x() < a0.x() < (self.frame_6.x() + self.frame_6.width()) and self.frame_6.y() < a0.y() < (
                    self.frame_6.y() + self.frame_6.height()):
                self.choose_index = 4
            self.choose_slot(self.choose_index)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())
