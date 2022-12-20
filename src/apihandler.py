import time
import mouse
from pynput.keyboard import Key, Controller
from configparser import ConfigParser

config = ConfigParser()
config.read("settings.cfg")

#Mouse coordinates: x vertical, increasing left to right, 
#                   y horizontal, increasing top to bottom
# (the canvas coordinates are the same)

# CONFIGURATION VARIABLES
LOG_FUNCTIONALITY = True
COORDINATE_MULTIPLIER = float(config["mouse"]["speed_multiplier"])
DOUBLE_CLICK_TIME_DELAY = float(config["mouse"]["double_click_time_delay"])

def zeroGlobalVars():
    #print("LOG: ZEROING GLOBAL VARIABLES")
    global th
    th.__init__()

def resetMouseState():
    #print("LOG: RESETTING MOUSE STATE")
    #if mouse.is_pressed(button='left'):
    mouse.release(button='left')
    #if mouse.is_pressed(button='right'):
    mouse.release(button='right')
    #if mouse.is_pressed(button='middle'):
    mouse.release(button='middle')

#Touch event handler
def touchEventHandler():
    global th

    #print("Current event:", currentEvent)

    if (len(th.currentXArray) > 2):
        zeroGlobalVars()
        resetMouseState()
        return

    if th.currentEvent == "touchstart":
        if len(th.touchStartTimeArray) == 0:
            th.touchStartTimeArray.append( [th.currentTouchIDArray[-1], time.time()] )
        elif len(th.touchEndTimeArray) == 1 and (time.time()-th.touchStartTimeArray[0][1]) < DOUBLE_CLICK_TIME_DELAY:
            mouse.press(button='left')
        th.previousVarXArray = th.currentXArray
        th.previousVarYArray = th.currentYArray
        return

        
    elif th.currentEvent == "touchmove":
        if th.wasThereMovementSinceTouchStart == True:
            mouse.move(COORDINATE_MULTIPLIER*(th.currentXArray[0]-th.previousVarXArray[0]), COORDINATE_MULTIPLIER*(th.currentYArray[0]-th.previousVarYArray[0]), absolute=False, duration=0)
            print("DIFF:", th.currentXArray[0]-th.previousVarXArray[0])
        th.previousVarXArray = th.currentXArray
        th.previousVarYArray = th.currentYArray
        th.wasThereMovementSinceTouchStart = True
        return

    # touchend event receives changedtouches array!
    elif th.currentEvent == "touchend":
            th.touchEndTimeArray = [time.time()]
            resetMouseState()
            return

    elif th.currentEvent == "touchcancel":
        print("-")
        resetMouseState()
        #wasThereMovementSinceTouchStart = False
        return

# Mouse related button presses (for actual buttons on the web page)
def mouseButtonHandler():
    global th
    if th.currentEvent == "leftclick" :  mouse.click(button='left')
    if th.currentEvent == "rightclick":  mouse.click(button='right')
    if th.currentEvent == "midclick"  :  mouse.click(button='middle')

# Keypress and key combination presser
def pressOnKeyboard(inputArray):
    keyboard = Controller()

    for keyname in inputArray:
        keyboard.press(keyname)
    for keyname in inputArray:
        keyboard.release(keyname)


# Keyboard button press handler
def keyboardButtonHandler():
    global th
    if th.currentEvent ==  "enter"        : pressOnKeyboard( [Key.enter] )
    if th.currentEvent ==  "backspace"    : pressOnKeyboard( [Key.backspace ] )
    if th.currentEvent ==  "delete"       : pressOnKeyboard( [Key.delete] )
    if th.currentEvent ==  "home"         : pressOnKeyboard( [Key.home] )
    if th.currentEvent ==  "end"          : pressOnKeyboard( [Key.end] )
    if th.currentEvent ==  "pageup"       : pressOnKeyboard( [Key.page_up] )
    if th.currentEvent ==  "pagedown"     : pressOnKeyboard( [Key.page_down] )
    if th.currentEvent ==  "printscreen"  : pressOnKeyboard( [Key.print_screen] )
    if th.currentEvent ==  "copy"         : pressOnKeyboard( [Key.ctrl, 'c'] )
    if th.currentEvent ==  "paste"        : pressOnKeyboard( [Key.ctrl, 'v'] )
    if th.currentEvent ==  "desktop"      : pressOnKeyboard( [Key.cmd,  'd'] )
    if th.currentEvent ==  "contextmenu"  : pressOnKeyboard( [Key.menu] )
    if th.currentEvent ==  "undo"         : pressOnKeyboard( [Key.ctrl, 'z'] )
    if th.currentEvent ==  "uparrow"      : pressOnKeyboard( [Key.up] )
    if th.currentEvent ==  "selectall"    : pressOnKeyboard( [Key.ctrl, 'a'] )
    if th.currentEvent ==  "leftarrow"    : pressOnKeyboard( [Key.left] )
    if th.currentEvent ==  "downarrow"    : pressOnKeyboard( [Key.down] )
    if th.currentEvent ==  "rightarrow"   : pressOnKeyboard( [Key.right] )

# Media button press handler
def mediaButtonHandler():
    global th
    if th.currentEvent ==  "playpause"     : pressOnKeyboard( [Key.media_play_pause] )
    if th.currentEvent ==  "escape"        : pressOnKeyboard( [Key.esc] )
    if th.currentEvent ==  "previous"      : pressOnKeyboard( [Key.media_previous] )
    if th.currentEvent ==  "fullscreen_yt" : pressOnKeyboard( ['f'] )
    if th.currentEvent ==  "next"          : pressOnKeyboard( [Key.media_next] )
    if th.currentEvent ==  "volumeup"      : pressOnKeyboard( [Key.media_volume_up] )
    if th.currentEvent ==  "mute"          : pressOnKeyboard( [Key.media_volume_mute] )
    if th.currentEvent ==  "volumedown"    : pressOnKeyboard( [Key.media_volume_down] )
    if th.currentEvent ==  "open"          : pressOnKeyboard( [Key.ctrl, 'o'] )
    if th.currentEvent ==  "closeprogram"  : pressOnKeyboard( [Key.alt, Key.f4] )
    if th.currentEvent ==  "fullscreen"    : pressOnKeyboard( [Key.alt, Key.enter] )
    if th.currentEvent ==  "changefocus"   : pressOnKeyboard( [Key.alt, Key.tab] )