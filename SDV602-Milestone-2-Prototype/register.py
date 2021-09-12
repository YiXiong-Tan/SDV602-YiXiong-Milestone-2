import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import login, error
def validate(window, values):
    """
    Validates the username and password during registration
    
    Args:
        window (module): window where the graph is to be plotted
        values (list): contains the input params:
                        - username
                        - password
                        - fruit

    Returns:
        result (str): returns the 'Failed' string for a failed status.
    """
    username = values['username']
    password = values['password']
    fruit = values['fruit']
    result = ''

    # reset message
    error.displayMessages(window)

    # -------------------------------- validate username, password and favourite fruit-------------------------------------
    if username == 'user2':
        result = 'Failed'
        err_msg = ['Register Failed','-Duplicate Username']

    if username == '' or password == '' or fruit == '':
        result = 'Failed'
        err_msg = ['Register Failed','-Can\'t leave anything blank!']

    if fruit.lower() == 'apple' or fruit.lower() == 'apples':
        result = 'Failed'
        err_msg = ['Register Failed','-What apples?!']
    
    if result == 'Failed':
        error.displayMessages(window,err_msg)

    return result

def window():
    """
    The register window.
    There will be a few validations happening here.
    - duplicate username
    - if the favourite fruit answer is too simple
    """
    result = ''
    messages = list()

    layout = [[sg.Text('Register', size=(30, 1), justification='center', font=("Helvetica", 25))],
                [sg.Column([
                    [sg.Text('Username')],
                    [sg.Input(key='username')],
                    [sg.Text('Password')],
                    [sg.Input(key='password')],
                    [sg.Text('What\'s your favourite fruit?')],
                    [sg.Input(key='fruit')],
                    [sg.Button('Back'),sg.Button('Submit')],
                    [sg.Text(k='messages',size=(50,3))]
                    ], justification='c')
                ]
              ]

    window = sg.Window('DES', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Back':
            window.close()

            # Back to login window
            login.window()

        if event == 'Submit':
            # validate registration
            result = validate(window, values)

            if not 'Failed' == result:
                # go to login window
                window.close()
                login.window()


    window.close()
