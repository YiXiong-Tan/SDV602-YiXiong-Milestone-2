"""
Graphs and charts functions for the matplotlib are stored here.

When a function is called depending on the chart/graph, 
configure the data and then call draw_figure function to generate 
the figure and plot the figure on the canvas
"""

from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib
matplotlib.use('TkAgg')


def draw_figure(canvas, figure, canvas_toolbar):
    """
    Plot the chart/graph figure to the chart

    Args:
        canvas (class): the graph placeholder
        figure (variable): the figure of the graph

    Returns:
        figure_canvas_agg (variable): the canvas where the graph was plotted
    """
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


class Toolbar(NavigationToolbar2Tk):
    """Generate the toolbar for the matplotlib chart"""

    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


def bar_graph(window, bar_chart_dict: dict):
    """
    Plots a simple bar graph on the window provided.

    Args:
        window (module): window where the graph is to be plotted
        bar_chart_dict: a dictionary that stores all the data for the bar chart
    """
    
    labels = bar_chart_dict.keys()
    men_means = bar_chart_dict.values()
    # women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Fire Count')
    # rects2 = ax.bar(x + width/2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Fire Count by Month/Year')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    # add the plot to the window
    return draw_figure(window['-CANVAS-'].TKCanvas, fig, window['-CONTROLS-'].TKCanvas)


def pie_chart(window, pie_chart_dict: dict):
    """
    Plots a simple pie chart on the window provided.

    Args:
        window (module): window where the graph is to be plotted
        pie_chart_dict: a dictionary that stores all the data for the pie chart
    """
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = list(pie_chart_dict.keys())
    sizes = [count/sum(pie_chart_dict.values()) *
             100 for count in pie_chart_dict.values()]
    # explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')

    # add the plot to the window
    return draw_figure(window['-CANVAS-'].TKCanvas, fig1, window['-CONTROLS-'].TKCanvas)


def discrete_plot(window, acres_dict: dict):
    """
    Plot format, sets marker in place of a continuous line. 

    Args 
          window: the window to be plotted in.
          acres_dict: the data that consist the acres data.
    """
    fig, ax = plt.subplots()
    plt.plot(acres_dict.values(), 'ro')

    return draw_figure(window['-CANVAS-'].TKCanvas, fig, window['-CONTROLS-'].TKCanvas)
