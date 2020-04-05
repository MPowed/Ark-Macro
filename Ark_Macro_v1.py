#!python
# coding: utf-8
from pynput.keyboard import Key, Controller as KeyboardController 
from pynput.mouse import Button, Controller as MouseController
from pynput import keyboard
import time
import threading
import sys
from ctypes import *



user32 = windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
if screensize == (1920, 1200):
    mousePOS1 = (1265, 240)
    mousePOS2 = (1525, 245)
    mousePOS3 = (800, 650)
elif screensize == (1920, 1080):
    mousePOS1 = (1260, 180)
    mousePOS2 = (1530, 185)
    mousePOS3 = (800, 590)
elif screensize == (2560, 1440):
    mousePOS1 = (1600, 350)
    mousePOS2 = (1870, 350)
    mousePOS3 = (1120, 780)
else:
    print('Resolution Error: Script not made for your resolution!')


current_keys = set()

kybrd  = KeyboardController()
mouse  = MouseController()
delay  = 0.4
button = Button.left

mouseClickStartStop = keyboard.Key.f1
keepMetal  = keyboard.Key.f2
keepMeat   = keyboard.Key.f3
keepWood   = keyboard.Key.f4
keepStone  = keyboard.Key.f5
keepHide   = keyboard.Key.f6
keepNarco  = keyboard.Key.f7
keepTinto  = keyboard.Key.f8
keepBerry  = keyboard.Key.f9
keepChitin = keyboard.Key.f10
keepEle    = keyboard.Key.f11
meatnHide = {keyboard.Key.shift, keyboard.Key.f3}
narconTinto = {keyboard.Key.shift, keyboard.Key.f7}
mejoberry = {keyboard.Key.shift, keyboard.Key.f9}
toggleFood = keyboard.Key.delete
foodButton = keyboard.Key.page_down


feed = False
foodSet = 0
food = ['raw meat', 'mejo', 'berry', "fish meat"]


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls')
        
def run_as_admin(argv=None, debug=False):
    shell32 = windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True
        
    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print ('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None



class ClickMouse(threading.Thread):

    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        

    def startClicking(self):
        self.running = True

    def stopClicking(self):
        self.running = False

    def run(self):
        while True:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)

clickThread = ClickMouse(delay, button)
clickThread.daemon = True
clickThread.start()

def printSpace():
    for k in range(13):
        print('')

def printScreen(food):
    print('Ready!')
    print('F1  - Auto Clicker')
    print('F2  - Keep Metal Only')
    print('F3  - Keep Meat Only')
    print('F4  - Keep Wood Only')
    print('F5  - Keep Stone Only (Not Tested)')
    print('F6  - Keep Hide Only (Not Tested)')
    print('F7  - Keep Narco Only')
    print('F8  - Keep Tinto Only')
    print('F9  - Keep Berry Only')
    print('F10 - Keep Chitin Only')
    print('F11 - Keep Element Only')
    print('Shift + F3 - Keep Meat and Hide')
    print('Shift + F7 - Keep Narcos and Tintos Only')
    print('Shift + F9 - Keep MejoBerrys Only')
    print('DEL - Toggle Feeding -', food)
    print('Pg Dn - Feed food listed above')

def feeding(what):
    ok = windll.user32.BlockInput(True)
    kybrd.press('f')
    kybrd.release('f')
    time.sleep(1)
    mouse.position = (140, 240)
    mouse.click(Button.left)
    time.sleep(.1)
    kybrd.type(what)
    time.sleep(.1)
    mouse.position = (350, 250)
    mouse.click(Button.left)
    time.sleep(.1)
    mouse.position = (800, 650)
    mouse.click(Button.left)
    kybrd.press(keyboard.Key.esc)
    kybrd.release(keyboard.Key.esc)
    ok = windll.user32.BlockInput(False)

def drop(what):
    time.sleep(.3)
    mouse.position = mousePOS1
    mouse.click(Button.left, 1)
    time.sleep(.1)
    kybrd.type(what)
    time.sleep(.1)
    mouse.position = mousePOS2
    mouse.click(Button.left, 1)
    time.sleep(.1)
    mouse.position = mousePOS3
    mouse.click(Button.left, 1)


def beginDrop():
    ok = windll.user32.BlockInput(True)
    # print("Sorting Inventory")
    clickThread.stopClicking()

    kybrd.press('f')
    kybrd.release('f')
    time.sleep(1)

def endDrop(click):
    kybrd.press('f')
    kybrd.release('f')
    time.sleep(.2)
    ok = windll.user32.BlockInput(False)
    if click:
        clickThread.startClicking()

    

def executeMetal():
    beginDrop()
    
    drop('o')
    drop('b')
    drop('c')
    drop('f')
    drop('h')
    drop('meat')

    endDrop(True)


def executeMeat():
    beginDrop()
    
    drop('b')
    drop('h')
    drop('o')
    drop('s')
    drop('prim')

    endDrop(False)

def executeWood():
    beginDrop()

    drop('t')
    drop('h')

    endDrop(True)

def executeStone():
    beginDrop()
    
    drop('f')
    drop('oil')
    drop('sa')

    endDrop(True)

def executeHide():
    beginDrop()
    
    drop('m')
    drop('b')
    drop('w')
    drop('t')
    drop('prim')

    endDrop(False)

def executeNarco():
    beginDrop()
    
    drop('s')
    drop('az')
    drop('m')
    drop('t')
    drop('w')

    endDrop(False)

def executeTinto():
    beginDrop()
    
    drop('s')
    drop('a')
    drop('m')
    drop('w')

    endDrop(False)

def executeBerry():
    beginDrop()
    
    drop('s')
    drop('th')
    drop('na')
    drop('wo')

    endDrop(False)

def executeChitin():
    beginDrop()

    drop('meat')
    drop('b')
    drop('hide')
    drop('d')
    drop('thatch')

    endDrop(False)

def executeEle():
    beginDrop()
    
    drop('st')
    drop('th')
    drop('be')
    drop('seed')
    drop('f')

    endDrop(True)

def executeMeatnHide():
    kybrd.release(keyboard.Key.shift)
    beginDrop()
        
    drop('b')
    drop('ch')
    drop('o')
    drop('s')
    drop('prim')

    endDrop(False)

def executeNarconTinto():
    kybrd.release(keyboard.Key.shift)
    beginDrop()
    
    drop('s')
    drop('am')
    drop('az')
    drop('m')
    drop('th')
    drop('w')

    endDrop(False)

def executeMejoberry():
    kybrd.release(keyboard.Key.shift)
    beginDrop()
    
    drop('s')
    drop('a')
    drop('t')
    drop('w')

    endDrop(False)
    

def on_press(key):
    global feed, food, foodSet
    if key == mouseClickStartStop:
        if clickThread.running:
            clickThread.stopClicking()
        else:
            clickThread.startClicking()



    elif key == keepMetal and keyboard.Key.shift not in current_keys:
        print(mouse.position)
    elif key == keepMeat and keyboard.Key.shift not in current_keys:
        executeMeat()
    elif key == keepWood and keyboard.Key.shift not in current_keys:
        executeWood()
    elif key == keepStone and keyboard.Key.shift not in current_keys:
        executeStone()
    elif key == keepHide and keyboard.Key.shift not in current_keys:
        executeHide()
    elif key == keepNarco and keyboard.Key.shift not in current_keys:
        executeNarco()
    elif key == keepTinto and keyboard.Key.shift not in current_keys:
        executeTinto()
    elif key == keepBerry and keyboard.Key.shift not in current_keys:
        executeBerry()
    elif key == keepChitin and keyboard.Key.shift not in current_keys:
        executeChitin()
    elif key == keepEle and keyboard.Key.shift not in current_keys:
        executeEle()
    elif key == toggleFood and keyboard.Key.shift not in current_keys:
        if feed == True:
            feed = False
            printSpace()
            printScreen('Off')
            printSpace()
            if foodSet != len(food)-1:
                foodSet += 1
            else:
                foodSet = 0
        else:
            feed = True
            printSpace()
            printScreen(food[foodSet])
            printSpace()
    elif key == foodButton:
            if feed == True:
                feeding(food[foodSet])


    if key in meatnHide:
    	current_keys.add(key)
    	if all(k in current_keys for k in meatnHide):
    		executeMeatnHide()
    elif key in narconTinto:
        current_keys.add(key)
        if all(k in current_keys for k in narconTinto):
            executeNarconTinto()
    elif key in mejoberry:
        current_keys.add(key)
        if all(k in current_keys for k in mejoberry):
            executeMejoberry()
           

def on_release(key):
	current_keys.clear()

def program():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        printScreen('Off')
        listener.join()

if __name__ == '__main__':
    ret = run_as_admin()
    if ret is True:
        print ('Loading!')
        program()
    elif ret is None:
        print ('I am elevating to admin privilege.')
    else:
        print ('Error(ret=%d): cannot elevate privilege.' % (ret, ))

    
