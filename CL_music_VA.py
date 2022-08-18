import random as r
import os
import pygame

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

def play_test():
    play_music('Test')
    
def play_music(cur_album):
    pygame.init()
    
    raw_playlist = os.listdir(f'A:\Music\{cur_album}')#only names.suffix
    r.shuffle(raw_playlist)
    path_playlist = [f'A:\Music\{cur_album}\{track}' for track in raw_playlist]#pathes to songs

    cur_track = 0
    running = True
    while running: # Переписать под асинхрон, чтобы была возможность вводить команды
        ''' ПЕРЕПИСАТЬ ЧЕРЕЗ pygame.mixer.get_busy() который выдаёт Тру, когда трек играет'''
        '''
        while len(path_playlist_del) > 0:
            if pygame.mixer.get_busy():
                pygame.mixer.music.queue(path_playlist_del[0])
                path_playlist_del.pop(0)
                print(pygame.mixer.get_busy())

        '''
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
    cur_track = r.choice(os.listdir(f'A:\Music\{cur_album}'))
    playing = f'A:\Music/"{cur_album}"/"{cur_track}"'.replace('"','').replace('/',"\\")
    os.system(f'Start {playing}')
    res = playing.split('\\')[-1].split('.')[0]
    print(f'Играет {res}')
    '''
def globa(command):
    return globals()[command]()
