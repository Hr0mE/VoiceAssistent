import psutil
import os

def start_and_close_notepad():
    m = []
    for proc in psutil.process_iter(): # создание списков запущенных процессов
        m.append(proc.name())
        
    if 'notepad.exe' in m:
        os.system('TASKKILL /F /IM notepad.exe')
    else:
        os.system('start notepad.exe')

def open_desktop():
    os.startfile(r'C:/Users/dimma/OneDrive/Документы/Desktop')

def open_code():
    os.system('start/min python -m idlelib Voice_Assistent.py')

def refrash_code():
    os.system('start/min A:\AVAmats\Python\Voice_assistent.py')


def globa(action):
    return globals()[action]()
