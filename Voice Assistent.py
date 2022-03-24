import os
import random as r
import speech_recognition as s_r
import pyaudio
import wave
import time
#import keyboard

sr = s_r.Recognizer()
sr.pause_threshold = 0.5

comands_dict = {
    'play_music': {
        'play_rock': ['включи рок', 'включи рок-н-ролл', 'чирок', 'рок', 'включи что-нибудь потяжелее','запусти рок-н-ролл'],
        'play_all': ['включи музыку', 'запусти музыку', 'музыку', 'музыку в студию', 'танцы до упаду', ''],
        'play_collection': ['включи классику','включи сборник','запусти классику','запусти сборник','давай что-нибудь длинное',
],
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

def play_rock():
    album_list = ['Skillet','Radiotapok','ThreeDaysGrace','ACDC']
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
    
def play_music(cur_album):
    cur_track = r.choice(os.listdir(f'A:\Music\{cur_album}'))
    playing = f'A:\Music/"{cur_album}"/"{cur_track}"'.replace('"','').replace('/',"\\")
    os.system(f'start {playing}')
    res = playing.split('\\')[-1].split('.')[0]
    print(f'Играет {res}')

    #m = {}
    #for album in range(len(albums)):
    #    m[albums[album]] = os.listdir(f'A:\Music\{albums[album]}')


def main():
    query = listen_comand()
    #print(f"'{query}'" + ',')
    print(query)
    
    for i, j in comands_dict['play_music'].items():
        if query in j:
            globals()[i]()
        else:
            continue
    
if __name__ == '__main__':
    main()


        



