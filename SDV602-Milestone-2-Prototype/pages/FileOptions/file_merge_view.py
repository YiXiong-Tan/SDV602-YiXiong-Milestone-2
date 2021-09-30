import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Column


class FileMergeView:
    def __init__(self):
        self.layout = [
            [sg.Text('Merge CSV:', font=('18'))],
            [sg.Text('Merge Target:', size=(12, 1)),
             sg.Input(key="target"), sg.FileBrowse(file_types=(("Comma separated value", "*.csv"),))],
            [sg.Text('File to Merge:', size=(12, 1)),
             sg.Input(key="source"), sg.FileBrowse(file_types=(("Comma separated value", "*.csv"),))],
            [sg.B("Merge CSV", key="Merge", size=(14, 1)),
             sg.B("Exit", size=(14, 1))]
        ]

        self.window = sg.Window("Merge CSV", self.layout, finalize=True, modal=True)
