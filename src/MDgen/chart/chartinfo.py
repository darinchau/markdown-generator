from collections import namedtuple
from MDgen.chart.colorinfo import ColorInfo

class ChartInfo:
    __slots__ = ("amount", "color")
    def __init__(self, amount: float, color: ColorInfo) -> None:
        self.amount = amount
        self.color = color
