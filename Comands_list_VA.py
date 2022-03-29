import random as r
import os
import psutil

#pattern for adding new comand       '': ['','','',''],
def comands_analis_dict():
    c_a_d = { 
    'music': ['включи','запусти','включить','запустить','рок','чирок','музыку','музыка','дискотека'],
    'open_close': ['открой','открыть','закрой','закрыть', 'активировать','активация', 'обновить','обнови','перезапустить','перезапусти'],
    }
    return c_a_d

def comands_dict(): #сделать отбор по словам "включить" запустить и тд, тогда включится музыка
    comands_dict = {
        'music': {
            'play_rock': ['рок', 'рок-н-ролл', 'рак'],
            'play_all': ['музыку', 'музыку в студию', 'танцы до упаду','музыка'],
            'play_collection': ['сборник','давай что-нибудь длинное'],
            'play_classic': ['классику','классика'],
            'play_atl': ['aиста','аист','atl','пл',],
            'play_skillet': ['скелет','skillet','скинуть','scary'],
            'play_acdc': ['что-нибудь потяжелее', 'ток'],
            'play_radiotapok': ['тапок', 'тапка','радио тапка', 'радио тапок'],
            'play_oppening': ['музыку аниме','музыка аниме','opening',],
            'play_guitar': ['гитару','гитара'],
            'play_thePrettyReckless': ['регги', 'the pretty reckless', 'забрать reckless', 'reckless','доброте враг вас','до приятеля клос'],
            'play_kish': ['короля и шута','король и шут', 'кыш', 'киш'],
            'play_grandson':['внук','внука','брэнсон','grandson', 'грэнд сан'],
            },
        'open_close': {
            'start_and_close_notepad': ['блокнот','добавить заметку','заметка','записная книжка'],
            'open_code': ['свой код', 'код','яви свою суть','кот','свой кот'],
            }
        }
    return comands_dict


def play_rock():# можно передавать в play_music список альбомов, а уже там формировать очередь
    album_list = ['Skillet','Radiotapok','ThePrettyReckless','ACDC']
    cur_album = r.choice(album_list)
    play_music(cur_album)

def play_all():
    albums = os.listdir('A:\Music')
    cur_album = r.choice(os.listdir(f'A:\Music'))
    play_music(cur_album)

def play_collection():
    play_music('Сборники')

def play_classic():
    play_music('Классика')
    
def play_atl():
    play_music('ATL')

def play_skillet():
    play_music('Skillet')

def play_acdc():
    play_music('ACDC')

def play_radiotapok():
    play_music('Radiotapok')

def play_oppenings():
    play_music('Oppenings')

def play_guitar():
    play_music('Гитара')

def play_thePrettyReckless():
    play_music('ThePrettyReckless')

def play_kish():
    play_music('КиШ')

def play_grandson():
    play_music('Grandson')
    
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
    os.system('start/min A:\AVAmats\Python\Voice_assistent.py')



def globa(i):
    return globals()[i]()
