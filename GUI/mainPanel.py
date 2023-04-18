#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: TestView>>mainPanel.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/3/16-11:43
@IDE: PyCharm 
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI.UI.UI_mainPanel import Ui_MainWindow
from GUI.mainWidget import MainWidget


class MainPanel(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        m = MainWidget()
        m.setParent(self.centralwidget)
        self.verticalLayout.addWidget(m)
        self.verticalLayout.setStretch(1, 10)


if __name__ == "__main__":
    # from qt_material import apply_stylesheet
    app = QApplication(sys.argv)
    main = MainPanel()
    # apply_stylesheet(app, theme='light_pink.xml')
    main.show()
    sys.exit(app.exec_())
