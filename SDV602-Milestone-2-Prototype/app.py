import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import register
import error
import home


class appModel:
    username = ""
    password = ""


class appView:

    def __init__(self):
        self.event = []
        self.values = {}
        self.window = None

    def setup(self):
        title = 'World Leading.. DES'

        self.layout = [[sg.Text('The World\'s Leading \n(actually not..) \nData Explorer Screen', size=(30, 3), justification='center', font=("Helvetica", 25))],
                       [sg.Column([
                           [sg.Text('Username')],
                           [sg.Input(key='username')],
                           [sg.Text('Password')],
                           [sg.Input(key='password', password_char='*')],
                           [sg.Button('Register'), sg.Button('Login')],
                           [sg.Text(k='messages', size=(40, 5))]
                       ], justification='c')
        ]
        ]

        self.window = sg.Window(title, self.layout)


class Controller:
    def __init__(self, model: appModel, view: appView):
        self.model = model
        self.view = view

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

                    error.displayMessages(self.view.window, err_msgs)

                else:
                    result = ''
                    err_msgs = []

                    self.stop()

                    # if true, go to main app
                    home.window(self.model)

        self.stop()

    def stop(self):
        self.view.window.close()


if __name__ == "__main__":
    c = Controller(appModel(), appView())
    c.run()


# def mainloop():
#     """
#     The login window.
#     """

#     layout = [[sg.Text('The World\'s Leading \n(actually not..) \nData Explorer Screen', size=(30, 3), justification='center', font=("Helvetica", 25))],
#               [sg.Column([
#                   [sg.Text('Username')],
#                   [sg.Input(key='username')],
#                   [sg.Text('Password')],
#                   [sg.Input(key='password', password_char='*')],
#                   [sg.Button('Register'), sg.Button('Login')],
#                   [sg.Text(k='messages', size=(40, 5))]
#               ], justification='c')
#     ]
#     ]

#     window = sg.Window('World Leading.. DES', layout)
#     credentials = {}

#     while True:
#         event, values = window.read()

#         if event == sg.WIN_CLOSED:
#             break

#         if event == 'Register':
#             window.close()

#             # Go to register window
#             register.window()

#         if event == 'Login':

#             result = ''
#             err_msgs = []
#             username, password = values['username'], values['password']

#             # if false, display the error message
#             # ****for prototyping - if username = 'user2' display error message****
#             # ****check for blank spaces****
#             # TODO should move this to the controller
#             if username == 'user2' or username == '' or password == '':

#                 result = 'Failed'
#                 err_msgs = ['Login Failed',
#                             '- Invalid Username/Password!', '- Duplicate login']

#                 error.displayMessages(window, err_msgs)

#             else:
#                 result = ''
#                 err_msgs = []

#                 window.close()

#                 # if true, go to main app

#                 credentials["username"], credentials["password"] = username, password

#                 home.window(credentials)

#     window.close()


# if __name__ == "__main__":
#     mainloop()
