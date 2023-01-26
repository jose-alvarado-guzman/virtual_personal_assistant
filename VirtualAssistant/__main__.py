import sys
import yaml
import argparse
import speech_recognition as sr
from VirtualAssistant.SenseCells.tts import speak
from VirtualAssistant.SenseCells.stt import listen
from VirtualAssistant.brain import Assistant

with open('profile.yaml', encoding='utf8') as config_file:
    profile_data = yaml.safe_load(config_file)

name = profile_data['name']
assistant_name = profile_data['virtual_assistant_name']
city_name = profile_data['city_name']
assistant_name = profile_data['virtual_assistant_name']

if __name__ == '__main__':
    argument_description = (f'Launch virtual assistance: {name}')
    argument_parser = argparse.ArgumentParser(argument_description)
    argument_parser.add_argument('-t','--textual',action='store_true',
                                 help=('Indicate if you want to launch the virtual '
                                        'assistance in conversational mode\n'))
    virtual_assistant = Assistant(assistant_name)
    arguments = argument_parser.parse_args()
    greeting = f'Hi {name}, my name is {assistant_name}, your personal virtual assistant.'
    quit_instruction = 'When you are ready to stop interacting with me'
    if arguments.textual:
        print(f'> {greeting}')
        print('> ' + quit_instruction + ' type quit')
        while True:
            query = input('> ')
            if query.lower() == 'quit':
                break
            response = virtual_assistant.get_response(query)
            print(f'> {response}')
    else:
        speak(greeting)
        speak(quit_instruction + ' say goodbye')
        while True:
            stt = listen().lower()
            if 'goodbye' in stt:
                break
            response = virtual_assistant.get_response(stt)
            if not 'error' in stt:
                print(response)
                speak(response)
            elif 'processing' in stt:
                speak("Sorry I did not undestand your request")
            elif 'connecting' in stt:
                speak('Sorry, I have trouble connecting to the internet')
