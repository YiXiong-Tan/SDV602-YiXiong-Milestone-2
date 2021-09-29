import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED


class HomePage():

    def __init__(self, username):
        """
        This is the home window.
        Navigation to the data explorer screen happens here.
        Can also add a new csv file here.

        Args:
            credentials (dict): 'username':<username>,'password':<password>
        """
        self.username = username
        self.layout = [[sg.Column([[sg.Text(f'Welcome, {username}')]], justification='l', expand_x=True), sg.Column([[sg.B('Logout')]], justification='r')],
                       [sg.Text('What do you want to do?', size=(30, 1),
                                justification='center', font=("Helvetica", 25))],
                       [sg.Column([
                           [sg.Text('Explore:')],
                           [sg.Button('DES 1', k='des1')],
                           [sg.Button('DES 2', k='des2')],
                           [sg.Button('DES 3', k='des3')]
                       ], k='c2', element_justification='c', expand_x=True)]
                       ]

        self.window = sg.Window('World Leading.. DES',self.layout, finalize=True)

    def window_close(self):
        """
        By creating a function that can be used outside of this file,
        we can call this function to perform task in this window.

        Args:
            home_window (obj): the home window
        """
        self.window.close()

        from pages.login import LoginPage
        login = LoginPage()
        login.load()

    def load(self):
        import pages.des as des

        while True:
            self.event, self.values = self.window.read()

            if self.event == sg.WIN_CLOSED:
                break

            if self.event == 'Logout':
                self.window_close()

            if self.event == 'des1' or self.event == 'des2' or self.event == 'des3':

                des.run(self.event)

            # if not self.home_window == None:
            #     self.home_window.close()
