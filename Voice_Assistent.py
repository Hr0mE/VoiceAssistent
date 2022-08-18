import Comands_list_VA as C_l #lib with comands #in "C_l" l is small letter L
import Recognizer_VA as R_VA #lib Speach-to-text
import time
import keyboard

        
def activating(query):
    try:
        qs = query.split()
        flag = qs[0]    #To sort comands, check Comands_list.comands_analis_dict()
        c_a_d = C_l.comands_analis_dict()
        for key, value in c_a_d.items():
            if flag in value:
                for i, j in C_l.comands_dict()[key].items():
                    q = ' '.join(query.split()[1:]) #cutting the first part of command
                    if q in j or query in j:
                        C_l.globa(key, i)   #activating func with name i
                        break
                    else:
                        continue      #code doesn`t work without it
    except IndexError: #rewrite it
        return "ERROR: Ничего не расслышал, повтори команду"
def main():
    R_VA.start_sound()
    #query = R_VA.listen_comand()
    #print(f"'{query}'" + ',') #Useful for adding new words in comands dict
    query = input('command: ')
    print(f'Исполняется команда "{query}"\n')
    activating(query)
            
def start():
    if __name__ == '__main__':
        main()


keyboard.add_hotkey('insert', lambda: start())
keyboard.wait()
