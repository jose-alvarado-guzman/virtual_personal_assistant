import sys
import yaml
import speech_recognition as sr
from VirtualAssistant.SenseCells.tts import speak
from VirtualAssistant.SenseCells.stt import listen

with open('profile.yaml') as config_file:
    profile_data = yaml.safe_load(config_file)

name = profile_data['name']
city_name = profile_data['city_name']

if __name__ == '__main__':
    speak(f'Hi {name}, how can I help you today?')
    stt = listen()
    print(f'Results: {stt}')
    if not 'error' in stt:
        speak(f'Did you said, {stt}')
    else:
        speak('Sorry I have trouble understanding you')
