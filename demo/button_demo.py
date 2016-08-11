from MComponents.MButton import MButton

__author__ = "Samvid Mistry"

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from MUtilities import MColors
from MComponents.MCheckbox import MCheckBox


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Button test")
        self.setGeometry(100, 100, 500, 500)
        p = self.palette()
        p.setColor(self.backgroundRole(), MColors.BACKGROUND_LIGHT)
        self.setPalette(p)

    def addComponents(self):
        layout = QGridLayout()
        self.button = MButton()
        layout.addWidget(self.button)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
