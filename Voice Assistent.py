import os
import random as r
import speech_recognition as s_r
import pyaudio
import wave
import time
import psutil
import keyboard
import winsound
import idelib


sr = s_r.Recognizer()
sr.pause_threshold = 0.5


comands_dict = {
    'comands': {
        'play_rock': ['включи рок', 'включи рок-н-ролл', 'чирок', 'рок', 'включи что-нибудь потяжелее','запусти рок-н-ролл'],
        'play_all': ['включи музыку', 'запусти музыку', 'музыку', 'музыку в студию', 'танцы до упаду','музыка'],
        'play_collection': ['включи классику','включи сборник','запусти классику','запусти сборник','давай что-нибудь длинное'],
        'start_and_close_notepad': ['блокнот','запусти блокнот','добавить заметку','заметка','записная книжка','закрой блокнот','открой блокнот', 'закрыть блокнот', 'открыть блокнот'],
        'open_code': ['открой свой код', 'открой код','открыть код','яви свою суть','открыть кот','открой кот','открой свой кот','запусти код','запусти кот'],
        'refrash_code': ['перезапустить код','обновить код','обновление','перезапуск','обновить кот','перезапустить кот'],
        }
    }


def listen_comand():
    try:
        with s_r.Microphone() as mic:
          sr.adjust_for_ambient_noise(source=mic, duration=0.5)
          audio = sr.listen(source=mic)
          query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query

    except s_r.UnknownValueError:
        return 'Какая-то ошибка, попробуй повторить команду'

def play_rock():# можно передавать в play_music список альбомов, а уже там формировать очередь
    album_list = ['Skillet','Radiotapok','ThePrettyReckless','ACDC']
    cur_album = r.choice(album_list)
    play_music(cur_album)

def play_all():
    albums = os.listdir('A:\Music')
    cur_album = r.choice(os.listdir(f'A:\Music'))
    play_music(cur_album)

def play_collection():
    album_list = ['Классика','Сборники']
    cur_album = r.choice(album_list)
    play_music(cur_album)
    
def play_music(cur_album): # можно генерировать список песен в альбоме и запускать
    cur_track = r.choice(os.listdir(f'A:\Music\{cur_album}'))
    playing = f'A:\Music/"{cur_album}"/"{cur_track}"'.replace('"','').replace('/',"\\")
    os.system(f'Start {playing}')
    res = playing.split('\\')[-1].split('.')[0]
    print(f'Играет {res}')

def start_and_close_notepad():
    m = []
    for proc in psutil.process_iter(): # создание списков запущенных процессов
        m.append(proc.name())
        
    if 'notepad.exe' in m:
        os.system('TASKKILL /F /IM notepad.exe')
    else:
        os.system('start notepad.exe')

def open_code():
    os.system('start/min python -m idlelib Voice_Assistent.py')

def refrash_code():
    os.system('start A:\PythonFiles\Voice_assistent.py')

def main():
    
    print("\n Listening...")
    winsound.PlaySound("A:\VAmats\Q_chordW", winsound.SND_ASYNC | winsound.SND_ALIAS)
        
    query = listen_comand()
    #print(f"'{query}'" + ',')

    print(query)
    
    for i, j in comands_dict['comands'].items():
        if query in j:
            globals()[i]()
        else:
            continue
    
def start():
    if __name__ == '__main__':
        main()

keyboard.add_hotkey('insert', lambda: start())
keyboard.wait()
        



