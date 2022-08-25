from vosk import Model, KaldiRecognizer
import speech_recognition as s_r
import wave
import pyaudio
import idelib
import json
import winsound



def listen_comand(): #main func
    try:
        print("\nЖду команды...\n")
        return offline_listener()
        #return online_listener()
    
    except s_r.UnknownValueError:
        return 'ERROR: Какая-то ошибка, попробуй повторить команду'
    
    except s_r.RequestError:
        online_to_offline_sound()
        print('[Нет соединения с интернетом]\n[Обработка команды в оффлайн-режиме]\n')
        return offline_listener()
     

def online_listener():
    with s_r.Microphone() as mic:
          param().adjust_for_ambient_noise(source=mic, duration=0.5)
          audio = param().listen(source=mic)
          query = param().recognize_google(audio_data=audio, language='ru-RU').lower()
    return query

def offline_listener():
    try:
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()
        model = Model("A:/AVAmats/model/vosk-model-small-ru-0.22")
        rec = KaldiRecognizer(model, 16000)
        data = ''
        query = ''
        while True:
            data = stream.read(16000)
            if rec.AcceptWaveform(data):
                q = rec.Result().split()
                q = q[3:-1]         #idk why, but its nessesary
                query += q[0]
                for i in q[1:]:
                    query += ' ' + i
                return query.replace('"','')
    except:
        return 'ERROR: Проверь offline_listener в Recognizer_VA'


def start_sound(): #Activating comand sound
    winsound.PlaySound("A:\AVAmats\Sounds\Q_chordW", winsound.SND_ASYNC | winsound.SND_ALIAS)

def online_to_offline_sound():
    winsound.PlaySound("A:\AVAmats\Sounds\Q_hold_ur_horses", winsound.SND_ASYNC | winsound.SND_ALIAS)

def param(): #must have to work
    sr = s_r.Recognizer()
    sr.pause_threshold = 0.5
    return sr




    
