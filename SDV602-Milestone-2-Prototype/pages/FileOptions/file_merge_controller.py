from pages.FileOptions.file_model import FileModel
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from pages.FileOptions.file_merge_view import FileMergeView
import PySimpleGUI as sg


class FileMergeController:
    """Controller for merging files"""

    def __init__(self, view: FileMergeView, model: FileModel):
        """
        Initializes the controller
        Args:
            FileMergeView - consists of the layout and window
            FileModel - consists of data from the view needed in the controller
        """
        self.view = view
        self.model = model

    def load(self):
        """
        Load the controller and handle events from the FileMergeView

        Return:
            path to uploaded file
        """
        while True:
            event, values = self.view.window.read()
            
            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break

            if event == "Merge":
                choice = sg.PopupOKCancel("Confirm merge?")
                if choice == "OK":
                    
                    self.model.source = values["source"]
                    self.model.target = values["target"]

                    self.model.merge()

                    if self.model.dest != "":
                        sg.Popup("Merge Successful")
                        break

        self.view.window.close()
        return self.model.dest
