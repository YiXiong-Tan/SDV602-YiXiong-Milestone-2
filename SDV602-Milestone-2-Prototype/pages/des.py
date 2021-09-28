from pages.DES.des_controller import DESController
from pages.DES.des_model import DESModel
from pages.DES.des_view import DESView


def run(event):

    des = DESController(DESView(event), DESModel())
    des.load()
