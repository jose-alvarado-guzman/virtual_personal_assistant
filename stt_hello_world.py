import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say something!')
    audio = r.listen(source)

with open('recording.wav','wb') as file:
    file.write(audio.get_wav_data())

try:
    print(f'Do you said {r.recognize_google(audio)}')
except sr.UnknownValueError:
    print('Sorry I could not understand what you said')
except sr.RequestError:
    print('Could not request results from Google Speech Recognition service')
