import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt
import hashlib
import os


class Image:
    def __init__(self, axis_limits=None, dots=None, charts=None, arrows=None, output_directory=''):
        self.axis_limits = axis_limits
        self.dots = dots
        self.charts = charts
        self.arrows = arrows
        self.output_directory = output_directory

    def draw_image(self):
        if not self.axis_limits:
            xmin, xmax, ymin, ymax = -4, 4, -4, 4
        else:
            xmin = round(float(self.axis_limits['xmin']))
            xmax = round(float(self.axis_limits['xmax']))
            ymin = round(float(self.axis_limits['ymin']))
            ymax = round(float(self.axis_limits['ymax']))
        ticks_frequency = 1

        fig, ax = plt.subplots(figsize=(10, 10))

        # Draw axes and coordinate grid
        # Set identical scales for both axes
        ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')
        # Set bottom and left spines as x and y axes of coordinate system
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # Create 'x' and 'y' labels placed at the end of the axes
        ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
        ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
        # Create custom major ticks to determine position of tick labels
        x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
        y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])
        # Create minor ticks placed at each integer to enable drawing of minor grid
        # lines: note that this has no effect in this example with ticks_frequency=1
        ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
        ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)
        # Draw major and minor grid lines
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

        # draw dots
        if self.dots:
            dot_xs = list()
            dot_ys = list()
            dot_colors = list()
            for dot in self.dots:
                dot_xs.append(float(dot['x']))
                dot_ys.append(float(dot['y']))
                dot_colors.append(dot.get('color', 'orange'))
                if dot.get('text'):
                    ax.text(float(dot['x']), float(dot['y']), '  '+dot['text'], color=dot.get('color', 'orange'),
                            ha='left', va='center', fontweight='bold', fontsize='large', zorder=100)
            ax.scatter(dot_xs, dot_ys, c=dot_colors, zorder=10)

        # draw charts
        if self.charts:
            chart_xs = np.linspace(xmin-1, xmax+1, 200)
            for chart in self.charts:
                chart_expression = chart['chart'].replace('x', 'chart_xs')
                chart_ys = ne.evaluate(chart_expression)
                chart_color = chart.get('color') or None
                ax.plot(chart_xs, chart_ys, c=chart_color)

        # draw arrows
        if self.arrows:
            for arrow in self.arrows:
                arrow = arrow.split(';')
                x_start, y_start, dx, dy = (int(value) for value in arrow[:4])
                text = arrow[4] if len(arrow) > 4 else ''
                ax.arrow(x_start, y_start, dx, dy, head_width=0.07, color='purple', length_includes_head=True, zorder=5)
                horizontal_align = 'left' if dx == 0 else 'center'
                vertical_align = 'bottom' if dy == 0 else 'center'
                ax.text(x_start+dx/2, y_start+dy/2, text, color='purple', zorder=100,
                        ha=horizontal_align, va=vertical_align)

        canvas = plt.gcf().canvas
        canvas.draw()

        image_hash = hashlib.sha1(np.array(canvas.buffer_rgba())).hexdigest()
        filepath = os.path.join(self.output_directory, 'images', image_hash + '.png')
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        plt.savefig(filepath, bbox_inches='tight')
        plt.close('all')
        return os.path.relpath(filepath, self.output_directory)
