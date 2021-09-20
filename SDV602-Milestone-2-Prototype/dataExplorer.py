import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Output
import home, matplotlibGraphsAndCharts
from icons import minus20x20, plus20x20

class Model:
    filepath = ""
    pass


def window(key='', home_window=sg.Window('')):
    """
    This function opens the window for the 3 DESes

    Args:
        key (str): specify the window selected. 'key1' = 1st DES, 'key2' = 2nd DES, 'key3' = 3rd DES
        home_window (obj): PySimpleGUI window
    """

    def make_layout():
        """
        This nested function makes the layout for the DESes. 
        """
      
        # -------------------------------layout-------------------------------
        layout = [
            [
                sg.Column([[sg.Button('Exit')]],
                          justification='l', expand_x=True),
                sg.Column([[sg.Button('Logout')]], justification='r')],
            [
                sg.Column([
                    [sg.InputText(key='-file1-'), sg.FileBrowse(),sg.Button('Upload')],
                    [sg.Canvas(key='-CANVAS-')],
                    [sg.Combo(default_value='Areas affected by the fire', values=['Areas affected by the fire','Types of fire occured', 'Fire occured in the year'], size=(30, 1)),
                     sg.B('', image_data=minus20x20, pad=(5, 0)), sg.B('', image_data=plus20x20, pad=(0, 0))],
                    [sg.Multiline(k='summary', size=(None, 10))]
                ], justification='l', expand_x=True),
                sg.Column([
                    [sg.Multiline(k='-mline-', size=(25, 30),
                                  autoscroll=True, auto_refresh=True)],
                    [sg.InputText(k='-chatTxt-', size=(20, 1)),
                     sg.Button('Send')]
                ], justification='r')
            ]
        ]

        # update title based on the key supplied
        title = ''
        if key == 'key1':
            title = '2015 Fire occurence'
        elif key == 'key2':
            title = '2016 Fire occurence'
        elif key == 'key3':
            title = 'Add New'

        return sg.Window(title, layout, finalize=True, modal=True)


    # initialize the windows
    window1, window2, window3 = None, None, None

    if key == 'key1':
        window1 = make_layout()
        matplotlibGraphsAndCharts.wave_graph(window1)
    elif key == 'key2':
        window2 = make_layout()
        matplotlibGraphsAndCharts.bar_graph(window2)
    elif key == 'key3':
        window3 = make_layout()
        matplotlibGraphsAndCharts.pie_chart(window3)

    while True:
        window, event, values = sg.read_all_windows()

        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Logout':
            window.close()
            
            # reset the window when closed
            if window == window1:
                window1 = None
            elif window == window2:
                window2 = None
            elif window == window3:
                window3 = None

            # when loging out, close the home window as well
            if event == 'Logout':
                home.window_close(home_window)

            break

    window.close()
