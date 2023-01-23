from abc import ABC, abstractmethod as virtual
from math import sin, cos
import random

from MDgen.base import ReadMe
from MDgen.chart.chartinfo import ChartInfo
from MDgen.chart.colorinfo import ColorInfo

PI = 3.1415926

def get_angles(a: float, size: float) -> tuple[float, float]:
    return size + size * sin(a), size - size * cos(a)

class PieChart(ReadMe):
    def __init__(self, size: int, entries: list[ChartInfo], use_columns: bool = True):
        """Generates a pie chart in the markdown file. If use_columns is set to true, then legends are put in columns"""
        self.size = size
        self.entries = entries
        self.col = use_columns
    
    @property
    def content(self):
        sum_total: float = 0.
        
        # First loop to get the sum total
        for v in self.entries:
            sum_total += v.amount
        
        # Second loop to draw the chart
        paths = []
        
        last_angle = 0.
        mid = self.size / 2
        
        # Keep track of the longest length to calculate the legend width
        longest_word_len = 0
        
        self.entries.sort(key = lambda x: x.amount, reverse = True)
        
        for i, v in enumerate(self.entries):
            ratio = v.amount / sum_total
            angle = 2 * PI * ratio
            
            # Calculate the new angles
            if i == len(self.entries) - 1:
                new_x, new_y = get_angles(0, mid)
            else:
                new_x, new_y = get_angles(last_angle + angle, mid)
            
            last_x, last_y = get_angles(last_angle, mid)
            
            # There is a bug where if the ratio is larger than 0.5 in the pie chart
            # Then the path might be something unexpected.
            # To fix this we perform linear interpolation, to cover the distances:
            # 0 - 40%, 30 - 70%, 60 - 100%
            if ratio >= 0.49:
                f30_x, f30_y = get_angles(last_angle + 0.3 * angle, mid)
                f40_x, f40_y = get_angles(last_angle + 0.4 * angle, mid)
                f60_x, f60_y = get_angles(last_angle + 0.6 * angle, mid)
                f70_x, f70_y = get_angles(last_angle + 0.7 * angle, mid)
                paths += [
                    f'<path d="M{mid},{mid} L{last_x},{last_y} A{mid},{mid},0,0,1,{f40_x},{f40_y} Z" fill="{v.color.color}"></path>',
                    f'<path d="M{mid},{mid} L{f30_x},{f30_y} A{mid},{mid},0,0,1,{f70_x},{f70_y} Z" fill="{v.color.color}"></path>',
                    f'<path d="M{mid},{mid} L{f60_x},{f60_y} A{mid},{mid},0,0,1,{new_x},{new_y} Z" fill="{v.color.color}"></path>'
                ]
            else:
                paths.append(
                    f'<path d="M{mid},{mid} L{last_x},{last_y} A{mid},{mid},0,0,1,{new_x},{new_y} Z" fill="{v.color.color}"></path>'
                )
            
            # To minimize black borders for adjacent similar colors
            last_angle += angle - 0.005
            
            longest_word_len = max(longest_word_len, len(v.color.name))
        
        # Use an HTML table to display the pie chart along with the legend
        chart = f'<div id="shape">\n\t<svg height="{self.size}" width="{self.size}">\n'
        chart += "\n".join([f"\t\t{p}" for p in paths])
        chart += '\n\t</svg>\n</div>'
        
        if self.col:
            legends = []
            # A third loop to create the legends
            for v in self.entries:
                ratio = v.amount / sum_total
                legends.append(
                    f'<p><span style="background-color: {v.color.color};">&nbsp; &nbsp;</span> {v.color.name}: {round(ratio * 100, 2)}%</p>'
                )
            
            # Make the legends
            legend = "\n".join([f"\t{l}" for l in legends])
            
            # Finish the table
            height = 18
            chart_width = 100
            legend_width = 20 * longest_word_len + 100
            
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
        else:
            entries_per_row = 3
            legends = []
            currRow = ""
            padding = longest_word_len + 10
            for i, v in enumerate(self.entries):
                ratio = v.amount / sum_total
                mock_text = f"    {v.color.name}: {round(ratio * 100, 2)}%"
                currRow += f'<span style="background-color: {v.color.color};">&nbsp; &nbsp;</span> {v.color.name}: {round(ratio * 100, 2)}%'
                currRow += "&nbsp; " * ((padding - len(v.color.name) - len(mock_text)) // 2 + 6)
                if i % entries_per_row == entries_per_row - 1 or i == len(self.entries) - 1:
                    legends.append(f'<p>{currRow}</p>')
                    currRow = ""
            legend = "\n".join(legends)
            table = f"""\
{chart}
{legend}"""
            return table
        
# Debug
if __name__ == "__main__":
    entries = [
        ChartInfo(random.random(), ColorInfo.random(f"Entry {i}", lower_bound=70)) for i in range(random.randint(2, 10))
    ]

    pc = PieChart(200, entries, use_columns=False)

    with open('./test.md', 'w') as f:
        f.write(pc.content)