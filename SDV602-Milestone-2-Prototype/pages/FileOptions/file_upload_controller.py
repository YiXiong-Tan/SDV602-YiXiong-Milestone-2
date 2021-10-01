"""
Controller that controls the view and model of file upload feature.
Read the view and handle any events
"""
from pages.FileOptions.file_model import FileModel
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from pages.FileOptions.file_upload_view import FileUploadView
import PySimpleGUI as sg


class FileUploadController:
    """A FileUploadController class to handle uploading of files to the DESes"""

    def __init__(self, view: FileUploadView, model: FileModel):
        """
        FileUploadView and FileModel is required to initialize the 
        FileUploadcontroller
        """
        self.view = view
        self.model = model

    def load(self):
        """Load the window and handle the window events"""
        
        while True:
            event, values = self.view.window.read()
            # pop when merge complete

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break

            if event == "Upload":
                choice = sg.PopupOKCancel("Upload?")

                if choice == "OK":

                    self.model.source = values["source"]

                    self.model.upload()

                    if self.model.dest != "":

                        sg.Popup("Upload Successful")
                        break

        self.view.window.close()
        return self.model.dest
