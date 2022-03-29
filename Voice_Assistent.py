import Comands_list_VA as C_l #lib with comands #in "C_l" l is small letter L
import Recognizer_VA as R_VA #lib Speach-to-text
import time
import keyboard

        
def activating(query):
    qs = query.split()
    flag = qs[0]    #To sort comands, check Comands_list.comands_analis_dict()
    c_a_d = C_l.comands_analis_dict()
    for key, value in c_a_d.items():
        if flag in value:
            for i, j in C_l.comands_dict()[key].items():
                if len(qs) > 1:
                    q = query.split()[1:][0] #cutting the first part of command
                else:
                    q = query
                if q in j or query in j:     
                    C_l.globa(i)   #activating func with name i
                else:
                    continue      #Must have to work
def main():
    R_VA.start_sound()
    query = R_VA.listen_comand()
    #print(f"'{query}'" + ',') #Useful for adding new words in comands dict
    print(f'Исполняется команда "{query}"\n')
    activating(query)
            
def start():
    if __name__ == '__main__':
        main()

start()
keyboard.add_hotkey('insert', lambda: start())
keyboard.wait()
