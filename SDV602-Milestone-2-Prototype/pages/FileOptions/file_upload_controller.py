from pages.FileOptions.file_model import FileModel
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from pages.FileOptions.file_upload_view import FileUploadView
import utils.fileOps as fileOps
import PySimpleGUI as sg


class FileUploadController:

    def __init__(self, view: FileUploadView, model: FileModel()):
        self.view = view
        self.model = model

    def load(self):

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
