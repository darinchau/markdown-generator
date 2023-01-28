from collections import namedtuple
from MDgen.chart.colorinfo import ColorInfo
from MDgen.util import copy

class ChartInfo:
    __slots__ = ("amount", "color")
    def __init__(self, amount: float, color: ColorInfo) -> None:
        self.amount = amount
        self.color = color
        
    def __copy__(self):
        return ChartInfo(self.amount, copy(self.color))
