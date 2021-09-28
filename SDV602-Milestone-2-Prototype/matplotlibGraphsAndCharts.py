from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')


def draw_figure(canvas, figure):
    """
    Plot the chart/graph figure to the chart
    
    Args:
        canvas (class): the graph placeholder
        figure (variable): the figure of the graph

    Returns:
        figure_canvas_agg (variable): the canvas where the graph was plotted
    """

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def wave_graph(window):
    """
    Plots a simple wave graph on the window provided.
    
    Args:
        window (module): window where the graph is to be plotted
    """

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)


def bar_graph(window):
    """
    Plots a simple bar graph on the window provided.
    
    Args:
        window (module): window where the graph is to be plotted
    """
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Men')
    rects2 = ax.bar(x + width/2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

def drawPieChart(window, pieDataDict:dict):
    """
    Plots a simple pie chart on the window provided.
    
    Args:
        window (module): window where the graph is to be plotted
    """
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = list(pieDataDict.keys())
    sizes = [count/sum(pieDataDict.values())*100 for count in pieDataDict.values()]
    #explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    print(labels)
    print(sizes)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig1)
