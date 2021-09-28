from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from pages.FileOptions.file_merge_view import FileMergeView
import utils.fileOps as fileOps
import PySimpleGUI as sg


class FileMergeController:

    def __init__(self, view: FileMergeView):
        self.view = view

    def load(self):

        while True:
            event, values = self.view.window.read()
            # pop when merge complete
            print(event)

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break

            if event == "Merge":
                choice = sg.PopupOKCancel("Confirm merge?")
                if choice == "OK":
                    # TODO merge the files
                    source = values["source"]
                    target = values["target"]
                    fileOps.merge(source, target)
                    
                    # TODO store to data
                    

                    sg.Popup("Merge Successful")

        self.view.window.close()
