"""Module used for speech recognition"""

import os
import sys

def speak(message : str) -> None:
    """
    This function takes a message as an argument and convers it to
    speech depending on the operating system. It will execute the say
    command or espeak it the OS iOS or Linux respectively.

    Parameters
    ----------
    message : str
        String containing the message to convert to speech.

    """
    if sys.platform == 'darwin':
        tts_engine = 'say -v Alex'
    elif sys.platform  in ['linux','linux2']:
        tts_engine = 'espeak'
    else:
        raise ValueError('OS not supported')
    os.system(f'{tts_engine} "{message}"')
