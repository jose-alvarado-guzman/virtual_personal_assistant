"Module use to convert speech to text."

import os
from typing import Optional, Dict, Any
import speech_recognition as sr

def listen(save_audio : Optional[bool] = False,
        audio_directory : Optional[str] = '.',
        audio_file_name : Optional[str] = 'recording') -> Dict[str,Any]:
    """Function use to convert speech to text.

    Parameters
    ----------
    save_audio: bool, optional
        Indicate whether to save the audio to file.
    audio_directory: str, optional
    audio_file_name: str, optional
        Name of the file used to store the audio.

    Return
    ------
    Dict[str, Any]
        Dictionary containing the results of the Googlei speech recognition.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as microphone:
        audio = recognizer.listen(microphone)

    if save_audio:
        if not (os.path.exists(audio_directory) and os.path.isdir(audio_directory)):
            os.makedirs(audio_directory)
        full_file_name = os.path.join(audio_directory,audio_file_name)
        with open(f'{full_file_name}.wav','wb') as file:
            file.write(audio.get_wav_data())
    try:
        result = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        result = {'error':'Processing'}
    except sr.RequestError:
        result = {'error':'Connecting'}
    return result
