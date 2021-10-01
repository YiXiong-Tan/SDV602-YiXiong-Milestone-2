"""
File upload layout
"""
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Column


class FileUploadView:
    """
    FileUploadView class
    Create an FileUploadView object to get a FileUploadView layout.
    """
    
    def __init__(self):
        """
        Initializes the class
        Sets layout and window to self.
        """    
        self.layout = [
            [sg.Text('File Upload:', font=('18'))],
            [sg.Text('Upload file path:', size=(12, 1)),
             sg.Input(key="source"), sg.FileBrowse(file_types=(("Comma separated value", "*.csv"),))],
            [sg.B("Upload CSV", key="Upload", size=(14, 1)),
             sg.B("Exit", size=(14, 1))]
        ]

        self.window = sg.Window("File Upload", self.layout, finalize=True, modal=True)
