import PySimpleGUI as sg


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
