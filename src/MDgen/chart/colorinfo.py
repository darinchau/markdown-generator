class ColorInfo:
    """Color is the hex code of the color, name is the entry in the chart with said color
    For example, ColorInfo("#FF0000", "Hiya!") will give you an entry in the chart, with red plots and name 'Hiya!'"""
    __slots__ = ("color", "name")
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name

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
        