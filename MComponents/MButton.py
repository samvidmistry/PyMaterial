__author__ = "Samvid Mistry"

from enum import IntEnum

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
        self.__blur = 2
        self.__color_anim = None
        self.__elev_anim = None
        self.__blur_anim = None
        self.__brush = QBrush(self.__color)
        self.__pen = QPen(self.__color)
        self.__shadow = QGraphicsDropShadowEffect()
        self.__shadow.setBlurRadius(self.blur)
        self.__animationSet = QParallelAnimationGroup()
        self.elevation = 1
        self.__shadow.setOffset(self.elevation)
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
            self.__shadow.setOffset(self.elevation)
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

        self.__animationSet.stop()
        self.__animationSet.clear()
        if self.__style == MButtonStyle.Flat or self.__style == MButtonStyle.Raised or \
                        self.__style == MButtonStyle.Toggles:
            self.__animationSet.addAnimation(self.get_color_animation(QColor("#CCC")))

        if self.__style == MButtonStyle.Raised or self.__style == MButtonStyle.Toggles:
            self.__animationSet.addAnimation(self.get_elev_animation(3))
            self.__animationSet.addAnimation(self.get_blur_animation(6))

        if self.__style == MButtonStyle.Toggles:
            self.__should_stick = not self.__should_stick

        self.__animationSet.start()

    def get_elev_animation(self, end_val: float) -> QAbstractAnimation:
        self.__elev_anim = QPropertyAnimation(self, "a_elevation", self)
        self.__elev_anim.setStartValue(self.elevation)
        self.__elev_anim.setEndValue(end_val)
        self.__elev_anim.setDuration(150)
        self.__elev_anim.setEasingCurve(QEasingCurve.InOutQuad)
        return self.__elev_anim

    def get_color_animation(self, end_val: QColor) -> QAbstractAnimation:
        self.__color_anim = QPropertyAnimation(self, "acolor", self)
        self.__color_anim.setStartValue(self.color)
        self.__color_anim.setEndValue(end_val)
        self.__color_anim.setDuration(150)
        return self.__color_anim

    def get_blur_animation(self, end_val: float) -> QAbstractAnimation:
        self.__blur_anim = QPropertyAnimation(self, "a_blur", self)
        self.__blur_anim.setStartValue(self.blur)
        self.__blur_anim.setEndValue(end_val)
        self.__blur_anim.setDuration(150)
        return self.__blur_anim

    def mouseReleaseEvent(self, event):
        if self.__style == MButtonStyle.Disabled:
            return

        self.__animationSet.stop()
        self.__animationSet.clear()
        self.__animationSet.addAnimation(self.get_color_animation(QColor("#EEE")))

        if not self.__should_stick:
            self.__animationSet.addAnimation(self.get_elev_animation(1))
            self.__animationSet.addAnimation(self.get_blur_animation(2))

        self.__animationSet.start()

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

    @property
    def color(self) -> QColor:
        return self.__color

    @color.setter
    def color(self, value: QColor):
        self.__color = value
        self.repaint()

    @property
    def blur(self) -> float:
        return self.__blur

    @blur.setter
    def blur(self, value: float):
        self.__blur = value

    def getcolor(self) -> QColor:
        return self.color

    def setcolor(self, value: QColor):
        self.color = value

    def setElevation(self, value: int):
        self.elevation = value

    def getElevation(self) -> int:
        return self.elevation

    def getBlur(self) -> float:
        return self.blur

    def setBlur(self, val: float):
        self.blur = val

    acolor = Property(QColor, getcolor, setcolor)
    a_elevation = Property(float, getElevation, setElevation)
    a_blur = Property(float, getBlur, setBlur)


class MButtonStyle(IntEnum):
    Flat = 0
    Raised = 1
    Toggles = 2
    Disabled = 3
