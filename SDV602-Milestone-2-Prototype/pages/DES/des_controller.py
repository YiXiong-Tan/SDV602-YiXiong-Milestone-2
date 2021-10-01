"""
Des controller that handles the events from the view
Here are some functions of the DES:
- updates the file history
- update the canvas
- acccess merge and update file from here
"""

from pages.DES.des_model import DESModel
from pages.DES.des_view import DESView
import PySimpleGUI as sg
import utils.data_visuals as plotter
import pages.file_operations as file
import pages.des as des


class DESController:
    """
    To initialize the controller, create a new object of the class and
    pass in DESView and DESModel
    """

    def __init__(self, view: DESView, model: DESModel):
        """
        Initializes the DES Controller and assign the view and model to self.

        Args:
            view: only the DES view can be used
            model: only the DES model can be used
        """
        self.view = view
        self.model = model
        self.current_des = self.model.selected_DES

    def load(self):
        """
        Runs the DES Controller
        """

        # get file history from user settings
        file_hist = sg.user_settings_get_entry(
            self.current_des+"-filenames", [])

        # get list of DESes
        list_of_DESes = sg.user_settings_get_entry("DESes")

        def updateFileHistory():
            """
            Update the file history combo box
            Private function
            """

            data_path = self.model.data_path

            # save filenames in user settings
            sg.user_settings_set_entry(
                self.current_des+"-filenames", list(set(file_hist+[data_path])))
            sg.user_settings_set_entry(
                self.current_des+"-last-filename", data_path)

        def updateCanvas(graph_type="Pie Chart"):
            """
            Update the canvas based on the selected value from the combo box
            Private function

            Args:
                graph_type: defaulted to Pie Chart. Eg. Pie Chart, Bar Graph and Scatter plots
            """

            data_path = self.model.data_path

            # ---------------------------- check if file exists ----------------------------
            if not file.sourceExist(data_path):
                if data_path in list(file_hist):
                    # remove from file history
                    file_hist.remove(data_path)
                    sg.user_settings_set_entry(
                        self.current_des+"-filenames", list(set(file_hist)))

                    # update the combo box
                    self.view.window['file-history'].update(values=file_hist)
                    return

            # ---------------------------- determine Chart based on combo box ----------------------------
            if graph_type == "Pie Chart":

                # dict for pie chart
                self.model.pie_chart_dict = file.getPieChartDataFromFile(
                    self.model.data_path)

                # update canvas
                self.view.figure_agg = plotter.pie_chart(
                    self.view.window, self.model.pie_chart_dict)

            if graph_type == "Bar Graph":
                # dict for bar chart
                self.model.bar_chart_dict = file.getBarChartDataFromFile(
                    self.model.data_path)

                # update canvas
                self.view.figure_agg = plotter.bar_graph(
                    self.view.window, self.model.bar_chart_dict)

            if graph_type == "Scatter Plots":
                # dict for thresholds
                self.model.horizontal_bar_chart_dict = file.getAcresData(
                    self.model.data_path)

                # update canvas
                self.view.figure_agg = plotter.discrete_plot(
                    self.view.window, self.model.horizontal_bar_chart_dict)

        # ---------------------------- update the last selected file ----------------------------
        # get last file opened
        lastfile = sg.user_settings_get_entry(
            self.current_des+"-last-filename", "")

        # if last file exist, display data visual
        if lastfile != "":
            self.model.data_path = lastfile
            updateCanvas()

        # ---------------------------- DES window ----------------------------
        while True:

            event, values = self.view.window.read()

            # ---------------------------- window events ----------------------------
            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == "combo":
                # get the combo drop down value and update canvas
                combo_value = values['combo']
                updateCanvas(combo_value)

            if event == "Clear History":
                # empty the settings
                sg.user_settings_set_entry(self.current_des+"-filenames", [])
                sg.user_settings_set_entry(
                    self.current_des+'-last-filename', '')

                # update the combo box
                self.view.window['file-history'].update(values=[], value='')

            if event == "file-history":
                self.model.data_path = values["file-history"]
                updateCanvas()

            if event == 'Merge CSV' or event == 'Upload CSV':

                if event == 'Merge CSV':
                    # open merge file popup
                    self.model.data_path = file.mergePopUp()

                if event == 'Upload CSV':
                    # open upload file popup
                    self.model.data_path = file.uploadPopUp()

                if self.model.data_path != "":
                    # update file history and canvas
                    updateFileHistory()
                    updateCanvas()

            if event in list_of_DESes.keys():
                self.view.window.close()
                des.run(event)

        self.view.window.close()
