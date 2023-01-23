from __future__ import annotations
import random

class ColorInfo:
    """Color is the hex code of the color, name is the entry in the chart with said color
    For example, ColorInfo("#FF0000", "Hiya!") will give you an entry in the chart, with red plots and name 'Hiya!'"""
    __slots__ = ("color", "name")
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
    
    @classmethod
    def random(self, name: str, *, lower_bound: int = 0, upper_bound: int = 255) -> ColorInfo:
        """Generate a random color for testing purposes
        lower bound and upper bound are bounds for the color values to prevent generating colors that are too bright or too dim"""
        r = str(hex(random.randint(lower_bound, upper_bound)))[2:]
        g = str(hex(random.randint(lower_bound, upper_bound)))[2:]
        b = str(hex(random.randint(lower_bound, upper_bound)))[2:]
        color = f"#{r}{g}{b}"
        return ColorInfo(color, name)

class GitColorInfo(ColorInfo):
    """GitColorInfo defines the color along with the language used by Github
    color is the hex code of the color,
    url is the URL to the documentation of the language,
    name is the name of the language"""
    __slots__ = ("color", "url", "name")
    def __init__(self, color: str, url: str, name: str):
        self.color = color
        self.url = url
        self.name = name
