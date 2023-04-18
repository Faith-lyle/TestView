#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: TestView>>tabWidget.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/3/16-15:33
@IDE: PyCharm 
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QMouseEvent
from GUI.UI.UI_tabWidget import Ui_Form


class TabWidget(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)