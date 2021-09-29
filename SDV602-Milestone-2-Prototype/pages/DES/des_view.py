from pages.DES.des_model import DESModel
import PySimpleGUI as sg

class DESView:
    def __init__(self, model:DESModel) :
        # self.title = title
        self.figure_agg = None
        self.model = model
        sorted_file_history_list = sorted( sg.user_settings_get_entry(self.model.selected_DES+'-filenames', []) )
        last_selected_file = sg.user_settings_get_entry(self.model.selected_DES+"-last-filename")

        """
        This nested function makes the layout for the DESes. 
        """
        self.layout = [
            
            [
                sg.Column([[sg.Button('Exit')]],
                          justification='l', expand_x=True)
            ],
            [   
                sg.Combo(sorted_file_history_list,key="file-history",size=(100,1),default_value=last_selected_file)
            ],
            [
                sg.Column([
                    [sg.Button('Upload CSV'), sg.Button('Merge CSV')],
                    [sg.Canvas(key='-CANVAS-', size=(300,300))],
                    [sg.Combo(default_value='Pie Chart',key="combo", values=['Pie Chart', 'Bar Graph', 'Maps'], enable_events=True, size=(30, 1))],
                    [sg.Multiline(k='summary', size=(None, 10))]
                ], justification='l', expand_x=True),
                sg.Column([
                    [sg.Multiline(k='-mline-', size=(25, 30),
                                  autoscroll=True, auto_refresh=True)],
                    [sg.InputText(k='-chatTxt-', size=(20, 1)),
                     sg.Button('Send')]
                ], justification='r')
            ],
            [
                sg.Column([[sg.Button("Previous DES", size=(15,2))]], justification='l', expand_x=True),
                sg.Column([[sg.Button("Next DES", size=(15,2))]], justification='r')
            ]

        ]

        self.window = sg.Window(self.model.selected_DES, self.layout, finalize=True)