"""
DES Model class store the data for the DES feature.
The Des controller and View access the data in this class
"""
class DESModel:
    def __init__(self,selected_DES):
        self.selected_DES = selected_DES

    data_path = ""
    pie_chart_dict = {}
    bar_chart_dict = {}
    horizontal_bar_chart_dict = {}