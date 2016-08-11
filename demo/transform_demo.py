from MAnimations.MTransform import MTransform
from MBase import MAnimationThread
from MComponents.MShape import MShape

__author__ = "Samvid Mistry"

from MComponents.MButton import MButton

import sys
from PySide.QtGui import *
from MUtilities import MColors
from MComponents.MCheckbox import MCheckBox


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Reveal test")
        self.setGeometry(100, 100, 500, 500)
        p = self.palette()
        p.setColor(self.backgroundRole(), MColors.BACKGROUND_LIGHT)
        self.setPalette(p)

    def addComponents(self):
        layout = QGridLayout()
        button = MButton()
        transform = MTransform(apply_transform, 100, 500, 10000)
        transform.start_delay = 1000
        transform.add_target(button)
        layout.addWidget(button, 0, 0)
        self.setLayout(layout)


def apply_transform(val: float, shape: MShape) -> None:
    shape.x = val
    shape.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
