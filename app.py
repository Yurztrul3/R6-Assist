import win32api, win32con
import time
import keyboard
from pynput.mouse import Listener
from threading import Thread
import tkinter as tk
from tkinter import ttk
import pyautogui
import subprocess

# R6 Assist Variables

Usable_Keybinds = ['q', 'e', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 
                   'b', 'n', 'm', ',', '.', '/', 'ctrl', 'tab', 'alt', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                   '-', '=', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

Anti_Recoil = False
SpinBot = False

Weapon_Mode = 'Primary'

WPM_K = "x"
SB_K = "l"

Recoil_Time = 0.5
Recoil_Time2 = 0

SPull_Y = 0
SPull_X = 0

SPull_Y2 = 0
SPull_X2 = 0

Left_Clicked = False
Right_Clicked = False

# App Variables

Last_Operator = None
Current_Opperator = None

# Operator Data

AutoOps = ['sledge', 'ash', 'twitch', 'fuze', 'hibana', 'ying', 'dokkaebi', 'iana',
                     'zero', 'nokk', 'buck', 'blackbeard', 'finka', 'ram', 'thermite',
                     'zofia', 'sens', 'lion', 'jackal', 'maverick', 'nomad', 'gridlock', 'amaru',
                     'ace', 'flores', 'osa', 'grim', 'brava', 'deimos', 'mute', 'bandit', 'valk', 'echo', 'mira', 'lesion', 'ela', 'warden', 'thorn', 'azami',
                     'solis', 'vigil', 'doc', 'mozzie', 'jager', 'frost', 'pulse', 'cav', 'maestro', 'alibi',
                     'kaid', 'goyo', 'wamai', 'oryx', 'melusi', 'aruni', 'bird', 'fenrir', 'tubarao', 'skopos']

Attack_Operators = ['sledge', 'ash', 'twitch', 'fuze', 'hibana', 'ying', 'dokkaebi', 'iana',
                     'zero', 'nokk', 'buck', 'blackbeard', 'finka', 'ram', 'thermite',
                     'zofia', 'sens', 'lion', 'jackal', 'maverick', 'nomad', 'gridlock', 'amaru',
                     'ace', 'flores', 'osa', 'grim', 'brava', 'deimos']
Defend_Operators = ['mute', 'bandit', 'valk', 'echo', 'mira', 'lesion', 'ela', 'warden', 'thorn', 'azami',
                     'solis', 'vigil', 'doc', 'mozzie', 'jager', 'frost', 'pulse', 'cav', 'maestro', 'alibi',
                     'kaid', 'goyo', 'wamai', 'oryx', 'melusi', 'aruni', 'bird', 'fenrir', 'tubarao', 'skopos']

Pistol_OPS = ['striker', 'sledge', 'thatcher', "ash", 'thermite', 'twitch', 'glaz', 'fuze', 'iq', 'buck', 'capitao', 'hibana', 'jackal', 'ying', 'zofia', 
                    'lion', 'finka', 'maverick', 'nomad', 'nokk', 'iana', 'ace', 'zero', 'flores', 'osa', 'sens', 'grim', 'ram', 'deimos', 'pulse',
                    'doc', 'rook', 'kapkan', 'tachanka', 'jager', 'bandit', 'valk', 'cav', 'lesion', 'ela', 'maestro', 'alibi', 'kaid', 'mozzie',
                    'goyo', 'wamai', 'oryx', 'aruni', 'azami', 'fenrir', 'tuarao', 'skopos']

#R6 Assist Functions

def ez_recoil():
    while True:
        if Anti_Recoil == True:
            if Left_Clicked == True and Right_Clicked == True:
                if Weapon_Mode == "Primary":
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, SPull_Y, SPull_X, 0, 0)
                    time.sleep(float(Recoil_Time))
                elif Weapon_Mode == "Secondary":
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, SPull_Y2, SPull_X2, 0, 0)
                    time.sleep(float(Recoil_Time2))
            elif Left_Clicked == False and Right_Clicked == True and SpinBot == True:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 0, 0, 0)
        elif Right_Clicked == True and SpinBot == True:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 0, 0, 0)
        else:
            pass
        time.sleep(0.00001)

# R6 Assist Mouse Functions

def on_click(x, y, button, pressed):
    global Left_Clicked
    global Right_Clicked
    ##global CB_Enabled

    if pressed:
        if button == button.left:
            Left_Clicked = True
        elif button == button.right:
            Right_Clicked = True    
    else:
        if button == button.left:
            Left_Clicked = False
        elif button == button.right:
            Right_Clicked = False
            #CB_Enabled = False

    time.sleep(0.00001)

# R6 Assist Keyboard Functions

def Change_WeaponMode():
    global Weapon_Mode
    if Current_Opperator != None:
        if Weapon_Mode == "Primary":
            Weapon_Mode = "Secondary"
            Weapon_Mode_label.configure(text=f'Weapon: {Weapon_Mode}')
        elif Weapon_Mode == "Secondary":
            Weapon_Mode = "Primary"
            Weapon_Mode_label.configure(text=f'Weapon: {Weapon_Mode}')
    else:
        pass

I_Num = 0  
B_Num = 0          
def on_press():
    global I_Num
    global B_Num
    while True:
        time.sleep(0.0000000000002)
        #print(pyautogui.displayMousePosition())
        if keyboard.read_key() == WPM_K:
            if I_Num == 0:
                I_Num = 1
                Change_WeaponMode()
            elif I_Num == 1:
                I_Num = 0
        elif keyboard.read_key() == SB_K:
            if B_Num == 0:
                B_Num = 1
                Toggle_Spinbot()
            elif B_Num == 1:
                B_Num = 0
                Toggle_Spinbot()

# App Functions

def check_pixel(x, y, target_r, target_g, target_b):
    # Call the compiled C++ program and pass coordinates and target color values
    result = subprocess.run(
        ['check_pixel.exe', str(x), str(y), str(target_r), str(target_g), str(target_b)], 
        capture_output=True, text=True
    )
    
    # Parse the output of the C++ program
    return result.stdout.strip().lower() == 'true'

def AutoOP_Detection():

    while True:

        X1, Y1 = 503, 192
        X2, Y2 = 316, 157

        Target_Color1 = (0, 255, 230)
        Target_Color2 = (255, 255, 255)

        if check_pixel(X1, Y1, *Target_Color1) and check_pixel(X2, Y2, *Target_Color2):
            print("Ready")

            for op in AutoOps:

                try:

                    match = pyautogui.locateOnScreen(f'appdata/operatorimages/{op}.png', region=(763, 16, 28, 28), confidence=0.5)

                    if match:

                        if op != Current_Opperator:

                            DropDown_Box.set(op)

                    else:
                        pass
                
                except pyautogui.ImageNotFoundException:
                    pass
        else:
            time.sleep(1.6)


def Settings_Window():

    global WPM_K
    global SB_K
    global AutoOp

    def close_window():

        global WPM_K
        global SB_K

        if weapon_mode_entry.get() == Spinbot_entry.get():
            pass
        else:
            with open("wpm_kb", "w") as f:
                f.write(weapon_mode_entry.get())
                f.close()

            with open("sb_kb", "w") as f:
                f.write(Spinbot_entry.get())
                f.close()

            time.sleep(0.3)

            WPM_K = weapon_mode_entry.get()
            SB_K = Spinbot_entry.get()

            Settings_W.destroy()

    wpm_kb_file = open(f'wpm_kb', 'r')
    wpm_kb_Data = wpm_kb_file.readlines()
    WPM_K = wpm_kb_Data[0]
    wpm_kb_file.close()

    sb_kb_file = open('sb_kb', 'r')
    sb_kb_Data = sb_kb_file.readlines()
    SB_K = sb_kb_Data[0]
    sb_kb_file.close()

    Settings_W = tk.Toplevel(root)
    Settings_W.title("Settings")
    Settings_W.minsize(350, 150)
    Settings_W.maxsize(350, 150)
    Settings_W.configure(background='black')
    Settings_W.iconbitmap('appdata/appicon.ico')

    weapon_mode_btn = tk.Label(Settings_W, text='Weapon Mode Keybind: ', background='white', foreground='black')
    weapon_mode_btn.place(x=30, y=20)

    weapon_mode_entry = ttk.Combobox(Settings_W, values=Usable_Keybinds)
    weapon_mode_entry.set(WPM_Keybind)
    weapon_mode_entry.place(x=165, y=20)

    Spinbot_btn = tk.Label(Settings_W, text='     Spin-Bot Keybind:       ', background='white', foreground='black')
    Spinbot_btn.place(x=30, y=40)

    Spinbot_entry = ttk.Combobox(Settings_W, values=Usable_Keybinds)
    Spinbot_entry.set(SB_Keybind)
    Spinbot_entry.place(x=165, y=40)

    AutoOP_btn = tk.Label(Settings_W, text='       Auto-OP (Beta):         ', background='white', foreground='black')
    AutoOP_btn.place(x=30, y=60)

    AutoOP_entry = ttk.Combobox(Settings_W, values=['on', 'off'])
    AutoOP_entry.set(SB_Keybind)
    AutoOP_entry.place(x=165, y=60)

    SaveChanges_Button = tk.Button(Settings_W, text='Save Changes', background='white', foreground='black', command=close_window)
    SaveChanges_Button.place(x=145, y=100)

def View_Attackers():
    DropDown_Box['values'] = Attack_Operators

def View_Deffenders():
    DropDown_Box['values'] = Defend_Operators

def Toggle_Recoil():
    global Anti_Recoil
    if Anti_Recoil == False:
        Anti_Recoil = True
        Recoil_Button.configure(background='green')
    elif Anti_Recoil == True:
        Anti_Recoil = False
        Recoil_Button.configure(background='red')

def Toggle_Spinbot():
    global SpinBot
    if SpinBot == False:
        SpinBot = True
        SpinBot_Button.configure(background='green')
    elif SpinBot == True:
        SpinBot = False
        SpinBot_Button.configure(background='red')

def Change_Values(User_Choice):

    global Recoil_Time
    global Recoil_Time2
    
    global SPull_Y
    global SPull_X

    global SPull_Y2
    global SPull_X2

    OperatorFile = open(f'data/{User_Choice}', 'r')
    Operator_Data = OperatorFile.readlines()

    Operator_Rtimes = Operator_Data[0]
    Opp_SpullY = Operator_Data[1]
    Opp_SpullX = Operator_Data[2]
    Operator_Rtimes2 = Operator_Data[4]
    Oppe_SpullY2 = Operator_Data[5]
    Oppe_SpullX2 = Operator_Data[6]

    Recoil_Time = Operator_Rtimes
    Recoil_Time2 = Operator_Rtimes2

    SPull_Y = int(Opp_SpullY)
    SPull_X = int(Opp_SpullX)

    SPull_Y2 = int(Oppe_SpullY2)
    SPull_X2 = int(Oppe_SpullX2)
    print(f"Operator Changed: {Last_Operator} -> {Current_Opperator}")


def Take_Pic(operator):

    screenshot = pyautogui.screenshot(region=(868, 16, 28,28))
    screenshot.save(f'appdata/operatorimages/{operator}.png')

def Check_OperatorChange():

    global Last_Operator
    global Current_Opperator

    while True:
        time.sleep(0.001)
        User_Choice = DropDown_Box.get()
        if User_Choice in Attack_Operators or User_Choice in Defend_Operators:
            if Last_Operator == None:
                Last_Operator = User_Choice
                Current_Opperator = User_Choice
                Change_Values(User_Choice=User_Choice)
                #Take_Pic(Current_Opperator)
            elif Last_Operator != None:
                Last_Operator = Current_Opperator
                if Current_Opperator == None:
                    Current_Opperator = User_Choice
                    Change_Values(User_Choice=User_Choice)
                    #Take_Pic(Current_Opperator)
                elif Current_Opperator != User_Choice:
                    Current_Opperator = User_Choice
                    Change_Values(User_Choice=User_Choice)
                    #Take_Pic(Current_Opperator)
                   
# App Code

root = tk.Tk()
root.title("R6 Assist | V 0.7")
root.configure(background='black')
root.minsize(350, 150)
root.maxsize(350, 150)
root.iconbitmap('appdata/appicon.ico')

White_Bar = tk.Frame(root, background='white')
White_Bar.configure(width=5, height=150)
White_Bar.place(x=100, y=0)

Change_Operator_Label = tk.Label(root, text=f"Change Operator", background='black', foreground='white')
Change_Operator_Label.place(x=180, y=10)

Recoil_Button = tk.Button(root, text="  Recoil  ", background='red', foreground='white', activeforeground='green', command=Toggle_Recoil)
Recoil_Button.place(x=25, y=20)

SpinBot_Button = tk.Button(root, text=" Spinbot ", background='red', foreground='white', activeforeground='green', command=Toggle_Spinbot)
SpinBot_Button.place(x=25, y=60)

Settings_Button = tk.Button(root, text=" Settings", activebackground="white", activeforeground='green', command=Settings_Window)
Settings_Button.place(x=25, y=100)

Defenders_Button = tk.Button(root, text="Defenders", background='blue', foreground='white', activebackground='blue', activeforeground='green', command=View_Deffenders)
Defenders_Button.place(x=150, y=100)

Weapon_Mode_label = tk.Label(root, text=f'Weapon: {Weapon_Mode}', background='black', foreground='white')
Weapon_Mode_label.place(x=174, y=28)

Attackers_Button = tk.Button(root, text="Attackers", background='orange', foreground='white', activebackground='orange', activeforeground='green', command=View_Attackers)
Attackers_Button.place(x=250, y=100)

DropDown_Box = ttk.Combobox(root, values=Attack_Operators)
DropDown_Box.place(x=160, y=50)

# Run app and Threads

Check_Operator_Thread = Thread(target=Check_OperatorChange)
Check_Operator_Thread.start()

Recoil_Thread = Thread(target=ez_recoil)
Recoil_Thread.start()

Keyboard_Thread = Thread(target=on_press)
Keyboard_Thread.start()

AutoOp_Thread = Thread(target=AutoOP_Detection)
AutoOp_Thread.start()

wpm_kb_file = open(f'wpm_kb', 'r')
wpm_kb_Data = wpm_kb_file.readlines()
WPM_Keybind = wpm_kb_Data[0]
wpm_kb_file.close()

sb_kb_file = open('sb_kb', 'r')
sb_kb_Data = sb_kb_file.readlines()
SB_Keybind = sb_kb_Data[0]
sb_kb_file.close()

with Listener(on_click=on_click) as listener:
    root.mainloop()
    listener.join()