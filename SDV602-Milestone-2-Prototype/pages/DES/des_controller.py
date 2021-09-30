from pages.DES.des_model import DESModel
from pages.DES.des_view import DESView
import PySimpleGUI as sg
import utils.data_visuals as plotter
import pages.file_operations as file
import pages.des as des


class DESController:

    def __init__(self, view: DESView, model: DESModel):
        self.view = view
        self.model = model

    def load(self):
        current_des = self.model.selected_DES   
        
        def updateFileHistory():
            data_path = self.model.data_path

            # old filenames
            old_filenames = sg.user_settings_get_entry(current_des+"-filenames",[])
            
            
            # save filenames
            sg.user_settings_set_entry(current_des+"-filenames", list(set(old_filenames+[data_path])))
            sg.user_settings_set_entry(current_des+"-last-filename", data_path)


        def updateCanvas(graph_type="Pie Chart"):

            if graph_type == "Pie Chart":

                # dict for pie chart
                self.model.pie_chart_dict = file.getPieChartDataFromFile(self.model.data_path)

                # update canvas
                self.view.figure_agg = plotter.pie_chart(self.view.window, self.model.pie_chart_dict)

            if graph_type == "Bar Graph":
                # dict for bar chart
                self.model.bar_chart_dict = file.getBarChartDataFromFile(self.model.data_path)
                
                # update canvas
                self.view.figure_agg = plotter.bar_graph(self.view.window, self.model.bar_chart_dict)

            if graph_type == "Highest Threshold":
                 # dict for thresholds
                self.model.bar_chart_dict = file.getHighestLowModerateHighThresholdData(self.model.data_path)

        # get last file
        lastfile = sg.user_settings_get_entry(current_des+"-last-filename", "")    

        # if last file exist, display data visual
        if lastfile != "":
            self.model.data_path = lastfile
            updateCanvas()
            

        while True:
            # when file history is not blank, update canvas

            event, values = self.view.window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == "combo":
                combo_value = values['combo']

                updateCanvas(combo_value)

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

            if event == 'des1' or event == 'des2' or event == 'des3':
                self.view.window.close()
                des.run(event)                    

        self.view.window.close()
