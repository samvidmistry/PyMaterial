from enum import IntEnum

from MComponents.MShape import MShape

__author__ = "Samvid Mistry"

import time
from typing import List, Callable

from PySide.QtGui import QApplication

from MAnimations.MAnimate import MAnimate
from MBase import *


class MTransform(MAnimate):
    def __init__(self, method: Callable[[float, MShape], None], start_val: float, end_value: float, duration: int, fps=60):
        MAnimate.__init__(self)
        self.can_run_reversed = True
        self.__remaining_delay = -1
        self.__method = method
        self.__completed = False
        self.__animator = MValueAnimator(start_val, end_value, duration, fps)

    def animate(self, shapes: List[MShape]):
        if self.start_delay != 0 and self.__remaining_delay == -1:
            self.__remaining_delay = self.start_delay

        if self.__remaining_delay > 0:
            self.__remaining_delay -= 1 / 60
            print(str(self.__remaining_delay))
            return True

        if self.started and not self.paused and not self.__completed:
            for i, s in enumerate(shapes):
                try:
                    self.__method(self.__animator.step(), s)
                except MFinalValueReachedException:
                    self.__completed = True

            if self.__completed:
                return False
