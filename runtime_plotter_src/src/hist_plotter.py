import numpy as np
import pandas as pd
from bokeh.io import show, curdoc
from bokeh.models import NumeralTickFormatter, HoverTool, ColumnDataSource
from bokeh.plotting import figure


class HistogramPlotter:

    """
        Plots a histogram using bokeh
    """

    def __init__(self, execution_times, colors=['#4682B4', '#D2B48C']):
        """
        Initialize plotter with the execution times of a notebook
        :param execution_times: How long each notebook code cell took
        :param colors: Colors in hexadecimal - Ascii colors don't work when running from command line
        """
        self.execution_times = execution_times
        self.colors = colors

    def plot(self, show_plot=True):
        """
        Plot a histogram using the data provided for the plotter
        :param show_plot: whether to display the plot or not
        :return: None
        """

        # Get all the execution times.
        data = list(self.execution_times.values())

        # Create dynamic bins based on the data.
        bins = np.arange(np.floor(min(data)), np.ceil(max(data)))

        # Create histogram using numpy
        hist, edges = np.histogram(data,
                                   weights=np.ones(len(data)) / len(data),
                                   density=1, bins=bins)

        # Create pandas from numpy histogram. This is used for hoverTool
        arr_df = pd.DataFrame({'count': hist, 'left': edges[:-1], 'right': edges[1:]})
        arr_df['f_count'] = [count for count in arr_df['count']]
        arr_df['f_interval'] = ['%d to %d ' % (left, right) for left, right in zip(arr_df['left'], arr_df['right'])]

        # User a dark theme for the histogram
        curdoc().theme = 'dark_minimal'
        arr_src = ColumnDataSource(arr_df)

        # Use Bokeh to plot the histogram using the numpy data provided
        p = figure(title="Histogram of {}".format("How Fast is my code?"),
                   x_axis_label="Runtime (ms)",
                   y_axis_label="Distribution (%)",
                   sizing_mode='stretch_both',
                   tools='pan')
        p.quad(top='count', source=arr_src, bottom=0, left='left', right='right',
               line_color=self.colors[0], fill_color=self.colors[1],
               fill_alpha=0.7)

        # Create a HoverTool to show the runtime and distribution
        hover = HoverTool(tooltips=[('Runtime (ms)', '@f_interval'),
                                    ('Distribution (%)', '@f_count{%0.2f}')])

        # Format the y axis with % and add hoverPlot
        p.yaxis.formatter = NumeralTickFormatter(format='0 %')
        p.add_tools(hover)

        # show plot if true
        if show_plot:
            show(p)
