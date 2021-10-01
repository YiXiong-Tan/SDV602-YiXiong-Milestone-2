"""
The home page will consists of the layout, event handlers and routes

Why this is in one file?
Because this is not a very huge file, the reason is to make finding things easier
"""

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED


class HomePage():
    """
    The home page class will initialize a home page with the username supplied

    Args:
        username: The name to be displayed on the home screen
    """

    def __init__(self, username):
        """
        This function initializes the home page.

        The number of DESes can be configured here.
        Configure the des:
            eg. {"desname":"actual name of DES", 
            "previous": "*specify the des when the previous button is clicked*", 
            "next": "*specify the des when the previous button is clicked*"}
        
        After configuring the DES, the des controller will make use of this dictionary to determine the previous page
        and next page.
        """
        self.username = username

        # setup the navs and buttons of DESes
        des_dict = {"des1": {"name": "DES 1", "previous": "des3", "next": "des2"},
                    "des2": {"name": "DES 2", "previous": "des1", "next": "des3"},
                    "des3": {"name": "DES 3", "previous": "des2", "next": "des1"}}
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
        # reset DESes
        sg.user_settings_set_entry("DESes", "")
        self.window.close()


    def load(self):
        """
        This function will load the current page.

        The event handlers will handler the events from the layout
        """
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
