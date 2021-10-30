import hashlib
import os
import numpy as np
import numexpr as ne
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from ast import literal_eval
from matplotlib.patches import Arc, Wedge
from matplotlib.transforms import IdentityTransform, TransformedBbox, Bbox
from matplotlib.lines import Line2D


def generate_table_cell_colors(nrows, ncols, cells_filled):
    nrows, ncols, cells_filled = int(nrows), int(ncols), int(cells_filled)
    cells = list()
    for i in range(nrows):
        row_cells_filled = min(cells_filled, ncols)
        row_cells = ['tab:blue'] * row_cells_filled + ['lightgrey'] * (ncols - row_cells_filled)
        cells_filled -= row_cells_filled
        cells.append(row_cells)
    return cells


class Angle(Arc):
    """
    A composite object that combines Arc, Wedge and Text to draw an annotated angle between two vectors.

    Based on AngleAnnotation from
    https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html
    """

    def __init__(self, xy, p1=None, p2=None, theta1=None, theta2=None, size=2,
                 ax=None, text="", textposition="inside", text_kw=None, **kwargs):
        """
        Parameters
        ----------
        xy, p1, p2 : tuple or array of two floats
            Center position and two points. Angle annotation is drawn between
            the two vectors connecting *p1* and *p2* with *xy*, respectively.
            Units are data coordinates.

        theta1, theta2 : Alternative way of defining the Angle,
            directly providing the angles instead of calculating them from p1 and p2.

        size : float
            Diameter of the angle annotation.

        ax : `matplotlib.axes.Axes`
            The Axes to add the angle annotation to.

        text : str
            The text to mark the angle with.

        textposition : {"inside", "outside", "edge"}
            Whether to show the text in- or outside the arc. "edge" can be used
            for custom positions anchored at the arc's edge.

        text_kw : dict
            Dictionary of arguments passed to the Annotation.

        **kwargs
            Further parameters are passed to `matplotlib.patches.Arc`. Use this
            to specify, color, linewidth etc. of the arc.
        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # in data coordinates
        self.vec1 = p1
        self.vec2 = p2
        self._theta1 = theta1
        self._theta2 = theta2
        self.size = size
        self.textposition = textposition

        # add a separate Wedge to act like an arc filler (since the Arc itself cannot be filled)
        if 'facecolor' in kwargs:
            zorder = None
            if 'zorder' in kwargs:
                zorder = int(kwargs.get('zorder'))-1
            angle_wedge = Wedge(self._xydata, size/2, theta1=self.theta1, theta2=self.theta2,
                                color=kwargs['facecolor'], zorder=zorder)
            self.ax.add_patch(angle_wedge)
            kwargs.pop('facecolor')

        # create and add main arc
        super().__init__(self._xydata, size, size, angle=0.0,
                         theta1=self.theta1, theta2=self.theta2, **kwargs)
        self.ax.add_patch(self)

        self.kw = dict(ha="center", va="center",
                       xytext=(0, 0), textcoords="offset points",
                       annotation_clip=True, zorder=kwargs.get('zorder'))
        self.kw.update(text_kw or {})
        if text == 'auto':
            angle_span = int(self.theta2 - self.theta1) % 360
            text = str(angle_span) + '°'
        self.text = ax.annotate(text, xy=self._center, **self.kw)

    def get_center(self):
        return self._xydata

    def set_center(self, xy):
        self._xydata = xy

    def get_theta(self, vec):
        return np.rad2deg(np.arctan2(vec[1]-self._xydata[1], vec[0]-self._xydata[0]))

    def get_theta1(self):
        if self._theta1 is not None:
            return self._theta1
        else:
            return self.get_theta(self.vec1)

    def get_theta2(self):
        if self._theta2 is not None:
            return self._theta2
        else:
            return self.get_theta(self.vec2)

    def set_theta(self, angle):
        pass

    _center = property(get_center, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)

    # The following two methods are needed to update the text position.
    def draw(self, renderer):
        self.update_text()
        super().draw(renderer)

    def update_text(self):
        c = self._center
        s = self.size
        angle_span = (self.theta2 - self.theta1) % 360
        angle = np.deg2rad(self.theta1 + angle_span / 2)
        r = s / 2
        if self.textposition == "inside":
            r = s / np.interp(angle_span, [60, 90, 135, 180],
                              [3.3, 3.5, 3.8, 4])
        self.text.xy = c + r * np.array([np.cos(angle), np.sin(angle)])
        if self.textposition == "outside":
            def R90(a, r, w, h):
                if a < np.arctan(h / 2 / (r + w / 2)):
                    return np.sqrt((r + w / 2) ** 2 + (np.tan(a) * (r + w / 2)) ** 2)
                else:
                    c = np.sqrt((w / 2) ** 2 + (h / 2) ** 2)
                    T = np.arcsin(c * np.cos(np.pi / 2 - a + np.arcsin(h / 2 / c)) / r)
                    xy = r * np.array([np.cos(a + T), np.sin(a + T)])
                    xy += np.array([w / 2, h / 2])
                    return np.sqrt(np.sum(xy ** 2))

            def R(a, r, w, h):
                aa = (a % (np.pi / 4)) * ((a % (np.pi / 2)) <= np.pi / 4) + \
                     (np.pi / 4 - (a % (np.pi / 4))) * ((a % (np.pi / 2)) >= np.pi / 4)
                return R90(aa, r, *[w, h][::int(np.sign(np.cos(2 * a)))])

            bbox = self.text.get_window_extent()
            X = R(angle, r, bbox.width, bbox.height)
            trans = self.ax.figure.dpi_scale_trans.inverted()
            offs = trans.transform(((X - s / 2), 0))[0] * 72
            self.text.set_position([offs * np.cos(angle), offs * np.sin(angle)])


class Image:
    def __init__(self, axis_limits=None, dots=None, texts=None, charts=None, arrows=None, polygons=None, angles=None,
                 lines=None, ellipses=None, arcs=None, wedges=None, table=None, pie_chart=None,
                 y_scale=1, draw_grid=True, draw_axes=True, output_directory=''):
        self.dots = dots
        self.texts = texts
        self.charts = charts
        self.arrows = arrows
        self.polygons = polygons
        self.angles = angles
        self.lines = lines
        self.ellipses = ellipses
        self.arcs = arcs
        self.wedges = wedges
        self.table = table
        self.pie_chart = pie_chart
        self.y_scale = y_scale
        self.draw_grid = draw_grid
        self.draw_axes = draw_axes
        self.output_directory = output_directory

        if not axis_limits:
            self._xmin = -4
            self._xmax = 4
            self._ymin = -4
            self._ymax = 4
        else:
            self._xmin = round(float(axis_limits['xmin']))
            self._xmax = round(float(axis_limits['xmax']))
            self._ymin = round(float(axis_limits['ymin']))
            self._ymax = round(float(axis_limits['ymax']))

    def _draw_grid(self, ax):
        ticks_frequency = 1
        ax.set(xlim=(self._xmin - 1, self._xmax + 1), ylim=(self._ymin - 1, self._ymax + 1), aspect='equal')
        # Set bottom and left spines as x and y axes of coordinate system
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # Create custom major ticks to determine position of tick labels
        x_ticks = np.arange(self._xmin, self._xmax + 1, ticks_frequency)
        y_ticks = np.arange(self._ymin, (self._ymax + 1), ticks_frequency)
        if self.draw_axes:
            ax.set_xticks(x_ticks[x_ticks != 0])
            ax.set_yticks(y_ticks[y_ticks != 0])
            if self.y_scale != 1:
                ax.set_yticklabels([str(y_tick * self.y_scale) for y_tick in y_ticks[y_ticks != 0]])
            # Create 'x' and 'y' labels placed at the end of the axes
            ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
            ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
            arrow_fmt = dict(markersize=4, color='black', clip_on=False)
            ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
            ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        else:
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.set_xticks(x_ticks)
            ax.set_yticks(y_ticks)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.tick_params(axis='both', which='both', length=0)
        # Draw grid lines
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    def _draw_texts(self, ax):
        for text_dict in self.texts:
            if isinstance(text_dict['x'], str):
                text_dict['x'] = float(text_dict['x'])
            if isinstance(text_dict['y'], str):
                text_dict['y'] = float(text_dict['y'])
            ax.text(**text_dict)

    def _draw_dots(self, ax):
        dot_xs = list()
        dot_ys = list()
        dot_colors = list()
        for dot in self.dots:
            dot_xs.append(float(dot['x']))
            dot_ys.append(float(dot['y']))
            dot_colors.append(dot.get('color', 'orange'))
            if dot.get('text'):
                ax.text(float(dot['x']), float(dot['y']), '  ' + dot['text'], color=dot.get('color', 'orange'),
                        ha='left', va='center', fontweight='bold', fontsize='large', zorder=100)
        ax.scatter(dot_xs, dot_ys, c=dot_colors, zorder=10)

    def _draw_charts(self, ax):
        for chart in self.charts:
            xmin = float(chart['xmin']) if chart.get('xmin') else self._xmin - 1
            xmax = float(chart['xmax']) if chart.get('xmax') else self._xmax + 1
            chart_xs = np.linspace(xmin, xmax, 200)
            if chart.get('chart_xs') and chart.get('chart_ys'):
                chart_xs = literal_eval(str(chart.get('chart_xs')))
                chart_ys = literal_eval(str(chart.get('chart_ys')))
            else:
                chart_expression = chart['chart'].replace('x', 'chart_xs')
                chart_ys = ne.evaluate(chart_expression)
            chart_color = chart.get('color') or None
            ax.plot(chart_xs, chart_ys, c=chart_color)

    def _draw_arrows(self, ax):
        for arrow in self.arrows:
            arrow = arrow.split(';')
            x_start, y_start, dx, dy = (int(value) for value in arrow[:4])
            text = arrow[4] if len(arrow) > 4 else ''
            ax.arrow(x_start, y_start, dx, dy, head_width=0.07, color='purple', length_includes_head=True, zorder=5)
            horizontal_align = 'left' if dx == 0 else 'center'
            vertical_align = 'bottom' if dy == 0 else 'center'
            ax.text(x_start + dx / 2, y_start + dy / 2, text, color='purple', zorder=100,
                    ha=horizontal_align, va=vertical_align)

    def _draw_polygons(self, ax):
        for polygon_dict in self.polygons:
            for i, (x, y) in enumerate(polygon_dict['xy']):
                if isinstance(x, str) or isinstance(y, str):
                    polygon_dict['xy'][i] = (float(x), float(y))
            polygon = patches.Polygon(**polygon_dict)
            ax.add_patch(polygon)

    def _draw_angles(self, ax):
        for angle_dict in self.angles:
            for point in ['xy', 'p1', 'p2']:
                x, y = angle_dict.get(point, (None, None))
                if isinstance(x, str) or isinstance(y, str):
                    angle_dict[point] = (float(x), float(y))
            for key in ['theta1', 'theta2']:
                if isinstance(angle_dict.get(key), str):
                    angle_dict[key] = float(angle_dict[key])
            angle_dict['ax'] = ax
            Angle(**angle_dict)

    def _draw_lines(self, ax):
        for line_dict in self.lines:
            # form xdata and ydata lists from points
            if line_dict.get('p1') and line_dict.get('p2'):
                line_dict['xdata'] = (line_dict['p1'][0], line_dict['p2'][0])
                line_dict['ydata'] = (line_dict['p1'][1], line_dict['p2'][1])
                line_dict.pop('p1')
                line_dict.pop('p2')
            line_dict['xdata'] = [float(x) for x in line_dict['xdata']]
            line_dict['ydata'] = [float(y) for y in line_dict['ydata']]

            # draw text on the line with the correct rotation
            if line_dict.get('text'):
                text_kwargs = dict(ha='center', va='bottom', annotation_clip=True)
                text_x = (line_dict['xdata'][0] + line_dict['xdata'][1]) / 2
                text_y = (line_dict['ydata'][0] + line_dict['ydata'][1]) / 2
                text_xy = (text_x, text_y)
                dx = line_dict['xdata'][1] - line_dict['xdata'][0]
                dy = line_dict['ydata'][1] - line_dict['ydata'][0]
                text_kwargs['rotation'] = np.degrees(np.arctan2(dy, dx))
                text_kwargs.update(line_dict.get('text_kw') or {})
                ax.annotate(line_dict['text'], xy=text_xy, **text_kwargs)
                line_dict.pop('text')
                if 'text_kw' in line_dict:
                    line_dict.pop('text_kw')
            line = Line2D(**line_dict)
            ax.add_line(line)

    def _draw_ellipses(self, ax):
        for ellipse_dict in self.ellipses:
            x, y = ellipse_dict['xy']
            if isinstance(x, str) or isinstance(y, str):
                ellipse_dict['xy'] = (float(x), float(y))
            ellipse = patches.Ellipse(**ellipse_dict)
            ax.add_patch(ellipse)

    def _draw_arcs(self, ax):
        for arc_dict in self.arcs:
            x, y = arc_dict['xy']
            if isinstance(x, str) or isinstance(y, str):
                arc_dict['xy'] = (float(x), float(y))
            for key in ['angle', 'theta1', 'theta2', 'width', 'height']:
                if isinstance(arc_dict.get(key), str):
                    arc_dict[key] = float(arc_dict[key])
            arc = patches.Arc(**arc_dict)
            ax.add_patch(arc)

    def _draw_wedges(self, ax):
        for wedge_dict in self.wedges:
            x, y = wedge_dict['center']
            if isinstance(x, str) or isinstance(y, str):
                wedge_dict['center'] = (float(x), float(y))
            for key in ['theta1', 'theta2', 'width']:
                if isinstance(wedge_dict.get(key), str):
                    wedge_dict[key] = float(wedge_dict[key])
            wedge = patches.Wedge(**wedge_dict)
            ax.add_patch(wedge)

    def _draw_table(self, ax, fig):
        if self.table.get('cells_filled'):
            nrows = int(self.table['nrows'])
            ncols = int(self.table['ncols'])
            cells_filled = int(self.table['cells_filled'])
            cell_colors = generate_table_cell_colors(nrows=nrows, ncols=ncols, cells_filled=cells_filled)
            table = ax.table(cellColours=cell_colors, colWidths=[0.05] * ncols, bbox=[0, 0, 1, 1])
            for pos, cell in table._cells.items():
                cell._height = cell._width
                cell.set_edgecolor('grey')
            fig.set_size_inches(ncols, nrows, forward=True)

    def _draw_pie_chart(self, ax, fig):
        if self.pie_chart.get('segments_filled'):
            total_segments = int(self.pie_chart['nsegments'])
            filled_segments = int(self.pie_chart['segments_filled'])
            segments = [1] * total_segments
            colors = ['lightgrey'] * (total_segments - filled_segments) + ['tab:blue'] * filled_segments
            ax.pie(segments, colors=colors, startangle=90)
            fig.set_size_inches(5, 5, forward=True)

    def save_to_file(self) -> str:
        """ Save current image to png file and return its path """
        canvas = plt.gcf().canvas
        canvas.draw()
        image_hash = hashlib.sha1(np.array(canvas.buffer_rgba())).hexdigest()
        filepath = os.path.join(self.output_directory, 'images', image_hash + '.png')
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        plt.savefig(filepath, bbox_inches='tight')
        return filepath

    def draw_image(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        if not self.draw_grid:
            ax.set(xlim=(self._xmin - 1, self._xmax + 1), ylim=(self._ymin - 1, self._ymax + 1), aspect='equal')
            ax.set_axis_off()
        else:
            self._draw_grid(ax)
        if self.dots:
            self._draw_dots(ax)
        if self.texts:
            self._draw_texts(ax)
        if self.charts:
            self._draw_charts(ax)
        if self.arrows:
            self._draw_arrows(ax)
        if self.polygons:
            self._draw_polygons(ax)
        if self.angles:
            self._draw_angles(ax)
        if self.lines:
            self._draw_lines(ax)
        if self.ellipses:
            self._draw_ellipses(ax)
        if self.arcs:
            self._draw_arcs(ax)
        if self.wedges:
            self._draw_wedges(ax)
        if self.table:
            self._draw_table(ax, fig)
        if self.pie_chart:
            self._draw_pie_chart(ax, fig)

        filepath = self.save_to_file()
        fig.clear()
        plt.close('all')
        return os.path.relpath(filepath, self.output_directory)
