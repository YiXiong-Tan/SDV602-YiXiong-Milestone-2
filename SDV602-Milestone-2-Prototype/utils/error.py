"""
All the error handling should be stored here.
"""
class Error:
    """The Error Class"""
    
    def displayMessages(window,messages=['']):
        """
        Display messages based on the window

        Args:
            window (Window): specify the window of message to be displayed
            messages (list): PySimpleGUI window
        """
        
        # update messages text
        message_in_line = ''
        for msg in messages:
            message_in_line += '\n'+msg

        window['messages'].update(f'{message_in_line}')
