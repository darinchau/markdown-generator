### This module contains helpful methods that generates pie charts for us
from typing import Optional

from MDgen.base import ReadMe
from MDgen.profile.gituser import GitUser
from MDgen.chart.piechart import PieChart
from MDgen.chart.colorinfo import ColorInfo
from MDgen.chart.chartinfo import ChartInfo
from MDgen.profile.git_colors import COLORS

class GitPieChart(PieChart):
    def __init__(self, user: GitUser, chart_size: int = 150, use_columns: bool = False, skip_entries: Optional[list[str]] = None):
        """Process all the repo information and creates the language pie chart for you"""
        if skip_entries is None:
            skip_entries = []
        entries: list[ChartInfo] = []
        other_bytes = 0
        for language, num_bytes in user.total_languages.items():
            if language in skip_entries:
                other_bytes += num_bytes
                continue
            color = COLORS.get(language)
            if color:
                entries.append(ChartInfo(num_bytes, color))
            else: 
                other_bytes += num_bytes
        other_info = ChartInfo(other_bytes, ColorInfo("#DEDEDE", "Others"))
        entries.append(other_info)
        return super().__init__(chart_size, entries, use_columns)
