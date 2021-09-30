from typing import Text
from PySimpleGUI.PySimpleGUI import Button
from pages.DES.des_model import DESModel
import PySimpleGUI as sg


class DESView:
    def __init__(self, model: DESModel):
        # self.title = title
        self.figure_agg = None
        self.model = model
        sorted_file_history_list = sorted(sg.user_settings_get_entry(
            self.model.selected_DES+'-filenames', []))
        last_selected_file = sg.user_settings_get_entry(
            self.model.selected_DES+"-last-filename")

        # ------------------------------ SETUP Nav buttons (start) ------------------------------
        des_dict = sg.user_settings_get_entry("DESes", {})
        des_nav = []

        # check if previous des exists
        if "previous" in des_dict[self.model.selected_DES].keys():
            previous_key = des_dict[self.model.selected_DES]["previous"]
            previous_button_name = "Previous Des\n(" + \
                des_dict[previous_key]["name"]+")"
            previous_button = sg.Column([[sg.Button(
                previous_button_name, key=previous_key, size=(15, 2))]], justification='l', expand_x=True)
            des_nav.append(previous_button)

        # check if next button des exists
        if "next" in des_dict[self.model.selected_DES].keys():
            next_key = des_dict[self.model.selected_DES]["next"]
            next_button_name = "Next DES\n("+des_dict[next_key]["name"]+")"
            next_button = sg.Column(
                [[sg.Button(next_button_name, key=next_key, size=(15, 2))]], justification='r')
            des_nav.append(next_button)
        # ------------------------------ SETUP Nav buttons (end) ------------------------------

        """
        This nested function makes the layout for the DESes. 
        """
        self.layout = [

            [

                sg.Text("File History:"),
                sg.Combo(sorted_file_history_list, key="file-history",
                         size=(50, 1), enable_events=True, default_value=last_selected_file),
                sg.Button('Upload CSV'), sg.Button('Merge CSV'),
                sg.Button('Exit')
            ],
            [
                sg.Column([
                    [sg.Combo(default_value='Pie Chart', key="combo", values=[
                              'Pie Chart', 'Bar Graph', 'Highest Threshold'], enable_events=True, size=(30, 1)), sg.Canvas(key='-CONTROLS-', size=(400, 40))],
                    [sg.Canvas(key='-CANVAS-', size=(300, 300))],
                    [sg.Multiline(k='summary', size=(None, 5), expand_x=True)]

                ], justification='l'),
                sg.Column([
                    [sg.Multiline(k='-mline-', size=(25, 30),
                                  autoscroll=True, auto_refresh=True, expand_y=True)],
                    [sg.InputText(k='-chatTxt-', size=(20, 1)),
                     sg.Button('Send')]
                ])
            ],
            des_nav

        ]

        self.window = sg.Window(self.model.selected_DES,
                                self.layout, location=(0, 0), finalize=True, modal=True).Finalize()
