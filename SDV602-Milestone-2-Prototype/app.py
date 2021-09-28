import PySimpleGUI as sg

if __name__ == "__main__":

    sg.theme("DarkAmber")
    # from pages.login import LoginPage
    # login = LoginPage()
    # login.load()

    from pages.home import HomePage

    home = HomePage("Ian")
    home.load() 