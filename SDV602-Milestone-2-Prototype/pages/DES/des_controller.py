from pages.DES.des_model import DESModel
from pages.DES.des_view import DESView
import PySimpleGUI as sg
import utils.matplotlibGraphsAndCharts as plotter


class DESController:

    def __init__(self, view: DESView, model: DESModel):
        self.view = view
        self.model = model

    def load(self):
        import pages.file_operations as file

        def updateCanvas():

            if self.model.data_path == "":
                return
                
            # TODO show file name

            # check drop down

            # dict for pie chart
            self.model.pieDataDict = file.getPieChartDataFromFile(
                self.model.data_path)

            # update canvas
            plotter.drawPieChart(
                self.view.window, self.model.pieDataDict)

        while True:
            event, values = self.view.window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == 'Merge CSV':
                # open file upload popup
                self.model.data_path = file.mergePopUp()

                # update infograph
                updateCanvas()

            if event == 'Upload CSV':
                # open file upload popup
                self.model.data_path = file.uploadPopUp()

                # update infograph 
                updateCanvas()

        self.view.window.close()
