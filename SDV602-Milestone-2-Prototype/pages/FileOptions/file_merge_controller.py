from pages.FileOptions.file_model import FileModel
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from pages.FileOptions.file_merge_view import FileMergeView
import PySimpleGUI as sg


class FileMergeController:

    def __init__(self, view: FileMergeView, model: FileModel):
        self.view = view
        self.model = model

    def load(self):

        while True:
            event, values = self.view.window.read()
            
            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break

            if event == "Merge":
                choice = sg.PopupOKCancel("Confirm merge?")
                if choice == "OK":
                    # TODO merge the files
                    self.model.source = values["source"]
                    self.model.target = values["target"]

                    self.model.merge()

                    if self.model.dest != "":
                        sg.Popup("Merge Successful")
                        break

        self.view.window.close()
        return self.model.dest
