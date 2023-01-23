from abc import ABC, abstractmethod as virtual
from math import sin, cos

from MDgen.base import ReadMe
from MDgen.chart.chartinfo import ChartInfo
from MDgen.chart.colorinfo import ColorInfo

PI = 3.1415926

def get_angles(a: float) -> tuple[float, float]:
    return 50 + 50 * sin(a), 50 - 50 * cos(a)

class PieChart(ReadMe):
    def __init__(self, size: int, entries: list[ChartInfo]):
        self.chart_size = size
        self.entries = entries
    
    @property
    def content(self):
        sum_total: float = 0.
        
        # First loop to get the sum total
        for v in self.entries:
            sum_total += v.amount
        
        # Second loop to draw the chart and take note of the legend
        legends = []
        paths = []
        last_angle = 0.
        mid = self.chart_size // 2
        for v in self.entries:
            angle = 2 * PI * v.amount / sum_total
            new_x, new_y = get_angles(last_angle + angle)
            last_x, last_y = get_angles(last_angle)
            paths.append(
                f'\t\t<path d="M{mid},{mid} L{last_x},{last_y} A{mid},{mid},0,0,1,{new_x},{new_y} Z" fill="{v.color.color}"></path>\n'
            )

            legends.append(
                f'<p><span style="background-color: {v.color.color};">&nbsp; &nbsp;</span> {v.color.name}</p>'
            )
        
        # Use an HTML table to display the pie chart along with the legend
        chart = f'<div id="shape">\n\t<svg height="{self.chart_size}" width="{self.chart_size}">'
        for p in paths:
            chart += p
        chart += '\n\t</svg>\n</div>'
        
        # Make the legends
        legend = ""
        for l in legends:
            legend += f"\t{l}\n"
        
        # Finish the table
        height = 18
        chart_width = 30
        legend_width = 50
        
        table = f"""\

<table style="height: {height}px; width: {chart_width + legend_width}px; border-collapse: collapse; border-style: hidden;" border="1">
<tbody>
<tr style="height: {height}px;">
    <td style="width: {chart_width}px; height: {height}px;">
{chart}
    </td>
    
    <td style="width: {legend_width}px; height: {height}px;">
{legend}
    </td>
</tr>
</tbody>
</table>"""

        return table
