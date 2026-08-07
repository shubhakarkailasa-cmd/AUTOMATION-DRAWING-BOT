import pyautogui
import time
time.sleep(4)

print("welcome to automate diagram...")

position=[]
print("""
        1)RECORD
        2)REPLAY
        3)VIEW POSTIONS
        4) EXIT
        5) SAVE""")

def record_postion():
        while True:
                user=input("do u want to take positions")
                if user.lower()!='yes':
                    break
                else:
                    pyautogui.position()
                    if len(position)>9:
                        print('positons limit has been reached')
                        break
                    else:
                        a=pyautogui.position()
                        position.append(a)
                        print('position has been captured',position)
def replay_position():
        if not position:
            print('please take positions first')
        else:
            for postions in position:
                pyautogui.dragTo(postions,duration=2)
                print('movement has been completed')
def view_position():
        if not position:
            print('no positions has been stored...')
        else:
            print(position)
def exit_terminal():
        print('thank you..')
        exit()
def save_position():
        if position:
            try:
                file=input('enter the file name you want to store')
                with open(file + '.txt','x') as file:
                    file.write(str(position)+ '\n' )
            except FileExistsError:
                print('same file has already has been created try again...')
                    
        else:
            print('no position are there to capture')
while True:
    try:
        choice=int(input('enter the choice number'))
        if choice==1:
            record_postion()
        elif choice==2:
            replay_position()
        elif choice==3:
            view_position()
        elif choice==4:
            exit_terminal()
        elif choice==5:
            save_position()
    except ValueError:
        print('please enter in number format')
    
             



