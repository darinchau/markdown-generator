import re

from MDgen.chart.colorinfo import ColorInfo
from MDgen.util import copy

class GitLanguageInfo(ColorInfo):
    def __init__(self, color: str, name: str, extension: list[str], language_type: str, language_id: int):
        self.color = color
        self.name = name
        self.lang_type = language_type
        self.id = language_id
        self.ext = copy(extension)

def variablize(k: str):
    """Makes the string a valid variable name in lowercase by replacing all non-alphabetic characters with underscores"""
    return "_".join([st.lower() for st in re.sub('[^a-zA-Z]+', '_', k).split(" ")])
