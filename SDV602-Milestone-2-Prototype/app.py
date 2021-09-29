import PySimpleGUI as sg
from pages.home import HomePage

if __name__ == "__main__":

    sg.theme("DarkAmber")
    # from pages.login import LoginPage
    # login = LoginPage()
    # login.load()

    home = HomePage("Ian")
    home.load()
