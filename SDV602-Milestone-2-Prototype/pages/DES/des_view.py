import PySimpleGUI as sg

class DESView:
    def __init__(self, title) :
        self.title = title

        """
        This nested function makes the layout for the DESes. 
        """
        self.layout = [
            [
                sg.Column([[sg.Button('Exit')]],
                          justification='l', expand_x=True)],
            [
                sg.Column([
                    [sg.Button('Upload CSV'), sg.Button('Merge CSV')],
                    [sg.Canvas(key='-CANVAS-', size=(300,300))],
                    [sg.Combo(default_value='Areas affected by the fire', values=['Areas affected by the fire', 'Types of fire occured', 'Fire occured in the year'], size=(30, 1))],
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

        self.window = sg.Window(self.title, self.layout, finalize=True)