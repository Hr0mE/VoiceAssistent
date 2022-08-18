import CL_music_VA as muslist
import CL_openclose_VA as openclose


#pattern for adding new comand       '': ['','','',''],
def comands_analis_dict():
    c_a_d = { 
    'music': ['включи','запусти','включить','запустить','рок','чирок','музыку','музыка','дискотека'],
    'open_close': ['открой','открыть','закрой','закрыть', 'активировать','активация', 'обновить','обнови','перезапустить','перезапусти'],
    }
    return c_a_d

def comands_dict():
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
            'play_test':['тестирование',"тест", "тестовый", "тесто"]
            },
        'open_close': {
            'start_and_close_notepad': ['блокнот','добавить заметку','заметка','записная книжка'],
            'open_code': ['свой код', 'код','яви свою суть','кот','свой кот'],
            'open_desktop': ["рабочий стол"],
            }
        }
    return comands_dict

def music(song):
    return muslist.globa(song)

def open_close(action):
    return openclose.globa(action)

def globa(command, action):
    return globals()[command](action)
