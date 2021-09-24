from model.appModel import *
from view.appView import *
from controller.appController import *


if __name__ == "__main__":
    c = appController(appModel(), appView())
    c.run()
 