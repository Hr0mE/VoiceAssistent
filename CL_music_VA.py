import random as r
import os
import pygame
import time
import threading

def play_rock():
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

def play_test():
    play_music('Test')


FLAG = True
def play_music(cur_album): #Переписать под асинхрон
    pygame.init()
    
    raw_playlist = os.listdir(f'A:\Music\{cur_album}')#only names.suffix
    r.shuffle(raw_playlist)
    path_playlist = [f'A:\Music\{cur_album}\{track}' for track in raw_playlist]#pathes to songs

    playlist_on()
    global FLAG
    def loop():
        while len(path_playlist) > 0 and FLAG: #Сделать проверку на внешнюю остановку потока
            if not pygame.mixer.get_busy():
                pygame.mixer.music.load(path_playlist[0])
                temp = path_playlist[0].split('\\')[-1].split('.')[0]
                print(f"Сейчас играет {temp}")
                song = pygame.mixer.Sound(path_playlist.pop(0))
                pygame.mixer.Sound.play(song)   
            else:
                if not FLAG:
                    pygame.mixer.Sound.stop(song)
                    print('\n' + 'breaked the loop' + '\n')#time.sleep(0.5)
                    break
                continue

    threading.Thread(target=loop).start()
            
def playlist_off():
    global FLAG
    print(f'STATE BEFORE {FLAG}')
    FLAG = False
    print(f'STATE AFTER {FLAG}')
    
def playlist_on():
    global FLAG
    FLAG = True

    '''
    cur_track = 0
    running = True
    while running: # Переписать под асинхрон, чтобы была возможность вводить команды
        
        for n, s in enumerate(path_playlist):
            print(s)
            if cur_track == n:
                pygame.mixer.music.load(s)
                song = pygame.mixer.Sound(s)
                pygame.mixer.Sound.play(song)
                #print(f'lenght of song: {pygame.mixer.Sound.get_length(song)} sec')
                print(pygame.mixer.get_busy())
                pygame.time.delay(round(pygame.mixer.Sound.get_length(song)*1000))
                print(pygame.mixer.get_busy())
                cur_track += 1
            if cur_track == len(path_playlist)-1:
                print('queue finished')
                running = False
                break
    '''
    '''
    cur_track = r.choice(os.listdir(f'A:\Music\{cur_album}'))
    playing = f'A:\Music/"{cur_album}"/"{cur_track}"'.replace('"','').replace('/',"\\")
    os.system(f'Start {playing}')
    res = playing.split('\\')[-1].split('.')[0]
    print(f'Играет {res}')
    '''
def globa(command):
    return globals()[command]()
