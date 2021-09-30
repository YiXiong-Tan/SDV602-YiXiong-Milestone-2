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

        # setup the navs and buttons of DESes
        des_dict = {"des1": {"name": "DES 1", "next": "des2"}, 
                    "des2": {"name": "DES 2", "previous": "des1", "next": "des3"}, 
                    "des3": {"name": "DES 3", "previous":"des2"}}
        sg.user_settings_set_entry("DESes", des_dict)

        # construct the buttons
        des_button_list = [[sg.Text('Explore:')]]
        for key in des_dict.keys():
            des_button_list.append(
                [sg.Button(des_dict[key]["name"], k=key, size=(20, 2), font="18")])

        self.layout = [[sg.Column([[sg.Text(f'Welcome, {username}')]], justification='l', expand_x=True), sg.Column([[sg.B('Logout')]], justification='r')],
                       [sg.Text('What do you want to do?', size=(30, 1),
                                justification='center', font=("Helvetica", 25))],
                       [sg.Column(des_button_list, k='c2',
                                  element_justification='c', expand_x=True)]
                       ]

        self.window = sg.Window('World Leading.. DES',
                                self.layout, finalize=True)

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
