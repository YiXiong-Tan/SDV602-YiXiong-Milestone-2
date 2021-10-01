"""
This is the main app file.
The program will start here.

Program consists of several concepts.
- Classes/ Modules
    The purpose of making use of classes is code reusability. By initializing a new class, we are
    able to create multiple objects of the same class.
    Classes are used in most parts of the program as it is the basis of Object oriented programming which
    is heavily focused in this program.
- MVC
    Model, View, Controller pattern is a software development architecture. It separates the program to
    model which gets and holds the data needed by the view, the controller that handles functionalities and manipulates
    the model and the view. The view is the layout/ UI of the program
    MVC is used in DES and file operation modules
"""

import PySimpleGUI as sg
from pages.home import HomePage


if __name__ == "__main__":
    """main function"""

    # set the theme to DarkAmber
    sg.theme("DarkAmber")

    # Initialize a home class and run it by calling load
    home = HomePage("Ian")
    home.load()
