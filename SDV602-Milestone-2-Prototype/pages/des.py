"""
Pipeline for running the DES

DES controller have access to the des model and des view
View have access to the model
Model just holds some data
"""

from pages.DES.des_controller import DESController
from pages.DES.des_model import DESModel
from pages.DES.des_view import DESView


def run(event):
    """
    Run a DES.
    Calling the "run" multiple times will create many DESes.

    Arg:
        event - the des key. Eg. des1, des2, des3
    """
    des_model = DESModel(event)
    des = DESController(DESView(des_model), des_model)
    des.load()
