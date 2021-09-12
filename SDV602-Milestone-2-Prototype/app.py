import home

def main(credentials):
    """
    The purpose of main is to perform some validation tasks before going to the home page.
    
    Args:
        credentials (dict): 'username':<username> and 'password:<password>'
    """
    
    try:
        home.window(credentials)
    except ValueError:
        print(ValueError)
