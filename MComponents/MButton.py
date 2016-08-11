from enum import IntEnum

__author__ = "Samvid Mistry"

from PySide.QtGui import *
from PySide.QtCore import *

from MComponents.MShape import MShape


class MButton(MShape):
    def __init__(self):
        MShape.__init__(self)

        self.__text = QLabel()
        self.__text.setText("Button")
        self.__text.setAlignment(Qt.AlignCenter)
        self.__style = MButtonStyle.Raised
        self.__color = QColor("#EEE")
        self.__should_stick = False
        self.__brush = QBrush(self.__color)
        self.__pen = QPen(self.__color)
        self.__shadow = QGraphicsDropShadowEffect()
        self.__shadow.setBlurRadius(2)
        self.__shadow.setOffset(1)
        self.add_layout_item(self.__text, 0, 0)
        self.setLayout(self.layout)
        self.max_width = self.__text.fontMetrics().width(self.__text.text())
        self.max_height = self.__text.fontMetrics().height()
        self.width = self.max_width
        self.height = self.max_height
        self.margin_left = 5
        self.margin_top = 5
        self.setFixedSize(self.width + self.margin_left * 2, self.height + self.margin_top * 2)
        self.__painter = QPainter()
        self.__bounding_rect = QRect(self.x, self.y,
                                     self.width + self.margin_left * 2, self.height + self.margin_top * 2)

    def paintEvent(self, event):
        painter = self.__painter
        painter.begin(self)
        painter.save()
        self.__brush.setColor(self.__color)
        self.__pen.setColor(self.__color)
        if self.__style == MButtonStyle.Raised or self.__style == MButtonStyle.Toggles:
            self.setGraphicsEffect(self.__shadow)
        painter.setBrush(self.__brush)
        painter.setPen(self.__pen)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRoundedRect(self.__bounding_rect, 2, 2)
        painter.restore()
        painter.end()

    def mousePressEvent(self, event):
        if self.__style == MButtonStyle.Disabled:
            return

        if self.__style == MButtonStyle.Flat or self.__style == MButtonStyle.Raised or self.__style == MButtonStyle.Toggles:
            self.__color.setNamedColor("#CCC")

        if self.__style == MButtonStyle.Raised or self.__style == MButtonStyle.Toggles:
            self.__shadow.setOffset(3)
            self.__shadow.setBlurRadius(4)

        if self.__style == MButtonStyle.Toggles:
            self.__should_stick = not self.__should_stick

        self.repaint()

    def mouseReleaseEvent(self, event):
        if self.__style == MButtonStyle.Disabled:
            return

        self.__color.setNamedColor("#EEE")
        if not self.__should_stick:
            self.__shadow.setOffset(1)
            self.__shadow.setBlurRadius(2)

        self.repaint()

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, value):
        self.__style = value
        self.repaint()


class MButtonStyle(IntEnum):
    Flat = 0
    Raised = 1
    Toggles = 2
    Disabled = 3
