### This module contains helpful methods that generates pie charts for us
from typing import Optional, Callable

from MDgen.base import ReadMe
from MDgen.profile.gituser import GitUser
from MDgen.chart.piechart import PieChart
from MDgen.chart.colorinfo import ColorInfo
from MDgen.chart.chartinfo import ChartInfo
from MDgen.profile.git_colors import COLORS

class GitPieChart(PieChart):
    def __init__(self, user: GitUser, chart_size: int = 150, use_columns: bool = False, ignore_key: Callable[[ChartInfo, float], bool] | None = None):
        """Process all the repo information and creates the language pie chart for you"""
        entries: list[ChartInfo] = []
        for language, num_bytes in user.total_languages.items():
            color = COLORS.get(language)
            if color:
                entries.append(ChartInfo(num_bytes, color))
        return super().__init__(chart_size, entries, use_columns, ignore_key)
