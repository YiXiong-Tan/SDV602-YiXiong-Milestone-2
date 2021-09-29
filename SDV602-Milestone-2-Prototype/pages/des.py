from pages.DES.des_controller import DESController
from pages.DES.des_model import DESModel
from pages.DES.des_view import DESView


def run(event):
    des_model = DESModel(event)
    des = DESController(DESView(des_model), des_model)
    des.load()
