import sys
import yaml
import speech_recognition as sr
from VirtualAssistant.SenseCells.tts import speak
from VirtualAssistant.SenseCells.stt import listen
from VirtualAssistant.dialect import Assistant

with open('profile.yaml', encoding='utf8') as config_file:
    profile_data = yaml.safe_load(config_file)

name = profile_data['name']
city_name = profile_data['city_name']
assistant_name = profile_data['virtual_assistant_name']

if __name__ == '__main__':
    virtual_assistant = Assistant(assistant_name)
#    speak(f'Hi {name}, how are you today?')
#    stt = listen()
    while True:
        query = input('> ')
        if query in ['quit','bye']:
            break
        response = virtual_assistant.get_response(query)
        print(response)
#    if not 'error' in stt:
#        speak(response)
#    else:
#        speak('Sorry I have trouble understanding you')
