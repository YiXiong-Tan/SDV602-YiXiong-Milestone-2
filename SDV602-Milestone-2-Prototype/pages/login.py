import register
from utils.error import Error
import PySimpleGUI as sg



class LoginPage:

    def __init__(self):
        self.username = ""
        self.password = ""

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

        self.window = sg.Window("Login", self.layout)

    def load(self):
        while True:
            self.event, self.values = self.window.read()

            if self.event == sg.WIN_CLOSED:
                break

            if self.event == 'Register':
                self.window.close()

                # Go to register window
                register.window()

            if self.event == 'Login':

                result = ''
                err_msgs = []
                # map view values to the model
                self.username, self.password = self.values['username'], self.values['password']

                # if false, display the error message
                # ****for prototyping - if username = 'user2' display error message****
                # ****check for blank spaces****
                # TODO should move this to the controller
                if self.username == 'user2' or self.username == '' or self.password == '':

                    err_msgs = ['Login Failed',
                                '- Invalid Username/Password!', '- Duplicate login']

                    Error.displayMessages(self.window, err_msgs)

                else:
                    result = ''
                    err_msgs = []

                    self.window.close()

                    # if true, go to main app
                    from pages.home import HomePage
                    home = HomePage(self.username)
                    home.load()
