# import sys
# sys.path.insert(0,'..')

import home
import PySimpleGUI as sg
import register
from model.appModel import *
from utils.error import *
from view.appView import *


class appController():
    def __init__(self, model: appModel, view: appView):
        self.model = model
        self.view = view
    
    def hi(self):
        print("hi")

    def run(self):
        self.view.setup()

        while True:
            self.view.event, self.view.values = self.view.window.read()

            if self.view.event == sg.WIN_CLOSED:
                break

            if self.view.event == 'Register':
                self.stop()

                # Go to register window
                register.window()

            if self.view.event == 'Login':

                result = ''
                err_msgs = []
                # map view values to the model
                self.model.username, self.model.password = self.view.values[
                    'username'], self.view.values['password']

                # if false, display the error message
                # ****for prototyping - if username = 'user2' display error message****
                # ****check for blank spaces****
                # TODO should move this to the controller
                if self.model.username == 'user2' or self.model.username == '' or self.model.password == '':

                    result = 'Failed'
                    err_msgs = ['Login Failed',
                                '- Invalid Username/Password!', '- Duplicate login']

                    displayMessages(self.view.window, err_msgs)

                else:
                    result = ''
                    err_msgs = []

                    self.stop()

                    # if true, go to main app
                    home.window(self.model)

        self.stop()

    def stop(self):
        self.view.window.close()
