import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import register, app, error
import hashlib

def window():
    """
    The login window.
    """

    result = ''
    messages = ()

    layout = [  [sg.Text('The World\'s Leading \n(actually not..) \nData Explorer Screen', size=(30, 3), justification='center', font=("Helvetica", 25))],
                [sg.Column([
                    [sg.Text('Username')],
                    [sg.Input(key='username')],
                    [sg.Text('Password')],
                    [sg.Input(key='password',password_char='*')],
                    [sg.Button('Register'), sg.Button('Login')],
                    [sg.Text(k='messages',size=(40,5))]
                    ],justification='c')
                ]
              ]

    window = sg.Window('World Leading.. DES', layout)
    credentials ={}

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Register':
            window.close()
            
            # Go to register window
            register.window()
        
        if event == 'Login':

            result = ''
            err_msgs = []
            username, password = values['username'], values['password']

            # if false, display the error message
            # ****for prototyping - if username = 'user2' display error message****
            # ****check for blank spaces****
            if username == 'user2' or username == '' or password == '':
                
                result = 'Failed'
                err_msgs = ['Login Failed','- Invalid Username/Password!', '- Duplicate login']

                error.displayMessages(window,err_msgs)

            else:
                result = ''
                err_msgs = []
                
                window.close()
                
                # if true, go to main app 

                credentials["username"], credentials["password"] = username, password

                app.main(credentials)

            
    window.close()


if __name__ == "__main__":
    window()