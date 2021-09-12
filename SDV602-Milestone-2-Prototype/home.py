import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import login, dataExplorer

def window_close(home_window):
    """
    By creating a function that can be used outside of this file, 
    we can call this function to perform task in this window.

    Args:
        home_window (obj): the home window
    """
    home_window.close()
    login.window()

def window(credentials={}):
    """
    This is the home window.
    Navigation to the data explorer screen happens here.
    Can also add a new csv file here.

    Args:
        credentials (dict): 'username':<username>,'password':<password>
    """
    layout = [  [sg.Column([[sg.Text(f'Welcome, {credentials["username"]}')]],justification='l',expand_x=True),sg.Column([[sg.B('Logout')]],justification='r')],
                [sg.Text('What do you want to do?', size=(30, 1), justification='center', font=("Helvetica", 25))],
                [sg.Column([
                    [sg.Text('Explore:')],
                    [sg.Button('2015 Fire occurence',k='key1')],
                    [sg.Button('2016 Fire occurence',k='key2')],
                    [sg.Text('Or:')],
                    [sg.Button('Add New',k='key3')]
                ], k='c2', element_justification='c', expand_x=True)]
              ]

    home_window = sg.Window('World Leading.. DES', layout, finalize=True)

    while True:
        home_window, event, values = sg.read_all_windows()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Logout':
            window_close(home_window)

        if event == 'key1' or event == 'key2' or event == 'key3':
            dataExplorer.window(event, home_window)
    
    if not home_window == None:
        home_window.close()
