import time
import sys
if sys.platform.startswith("linux"):
    import mousehandler
    # TODO: if this is working with Windows, then refactor accordingly (remove mouse package dep)
    mouse = mousehandler.MousePynputWrapper()
if sys.platform.startswith("win32"):
    import mouse
from pynput.keyboard import Controller
from pynput.keyboard import Key
from configparser import ConfigParser


config = ConfigParser()
config.read("settings.cfg")

#Mouse coordinates: x vertical, increasing left to right, 
#                   y horizontal, increasing top to bottom
# (the canvas coordinates are the same)

COORDINATE_MULTIPLIER = float(config["mouse"]["speed_multiplier"])
DOUBLE_CLICK_TIME_DELAY = float(config["mouse"]["double_click_time_delay"])

class Event:

    def __init__(self) -> None:
        # Initialize the class variables
        self.state = "start"

        self.currentEvent = ""
        self.previousEvent = ""

        self.currentXArray = []
        self.currentYArray = []
        self.currentTouchIDArray = []

        self.previousVarXArray = []
        self.previousVarYArray = []
        self.previousTouchIDArray = []

        self.wasThereMovementSinceTouchStart = False

        # TEMPORARY
        self.touchStartTime = None
        self.touchEndTime = None

th = Event()

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

    # Multi-touch not supported in this function
    if (len(th.currentTouchIDArray) > 1):
        print("RESET")
        zeroGlobalVars()
        resetMouseState()
        return

    if th.currentEvent == "touchstart":
        print("TOUCHSTART")
        # Check
        if len(th.currentXArray) < 2:
            th.touchStartTime = time.time()
        elif (time.time() - th.touchEndTime) < DOUBLE_CLICK_TIME_DELAY and (time.time() - th.touchStartTime) < DOUBLE_CLICK_TIME_DELAY:
            mouse.press(button='left')

        # End
        th.previousVarXArray = th.currentXArray
        th.previousVarYArray = th.currentYArray
        return

        
    elif th.currentEvent == "touchmove":
        print("TOUCHMOVE")
        # Check
        #if th.wasThereMovementSinceTouchStart == True:
        mouse.move(
            COORDINATE_MULTIPLIER*(th.currentXArray[0]-th.previousVarXArray[0]), 
            COORDINATE_MULTIPLIER*(th.currentYArray[0]-th.previousVarYArray[0]), 
            absolute=False, 
            duration=0)
        #print("DIFF:", th.currentXArray[0]-th.previousVarXArray[0])
        
        # End
        th.previousVarXArray = th.currentXArray
        th.previousVarYArray = th.currentYArray
        th.wasThereMovementSinceTouchStart = True
        return

    # touchend event receives changedtouches array!
    elif th.currentEvent == "touchend":
        print("TOUCHEND")
        th.touchEndTime = [time.time()]
        if (time.time() - th.touchStartTime) < DOUBLE_CLICK_TIME_DELAY:
            mouse.click(button='left')
        resetMouseState()
        return

    elif th.currentEvent == "touchcancel":
        print("TOUCHCANCEL")
        resetMouseState()
        #wasThereMovementSinceTouchStart = False
        return

# Mouse related button presses (for actual buttons on the web page)
def mouseButtonHandler():
    global th
    if th.currentEvent == "leftclick" :  mouse.click(button='left')   ; return
    if th.currentEvent == "rightclick":  mouse.click(button='right')  ; return
    if th.currentEvent == "midclick"  :  mouse.click(button='middle') ; return

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
    if th.currentEvent == "enter"       : pressOnKeyboard( [Key.enter] )        ; return
    if th.currentEvent == "backspace"   : pressOnKeyboard( [Key.backspace ] )   ; return
    if th.currentEvent == "delete"      : pressOnKeyboard( [Key.delete] )       ; return
    if th.currentEvent == "home"        : pressOnKeyboard( [Key.home] )         ; return
    if th.currentEvent == "end"         : pressOnKeyboard( [Key.end] )          ; return
    if th.currentEvent == "pageup"      : pressOnKeyboard( [Key.page_up] )      ; return
    if th.currentEvent == "pagedown"    : pressOnKeyboard( [Key.page_down] )    ; return
    if th.currentEvent == "printscreen" : pressOnKeyboard( [Key.print_screen] ) ; return
    if th.currentEvent == "copy"        : pressOnKeyboard( [Key.ctrl, 'c'] )    ; return
    if th.currentEvent == "paste"       : pressOnKeyboard( [Key.ctrl, 'v'] )    ; return
    if th.currentEvent == "desktop"     : pressOnKeyboard( [Key.cmd,  'd'] )    ; return
    if th.currentEvent == "contextmenu" : pressOnKeyboard( [Key.menu] )         ; return
    if th.currentEvent == "undo"        : pressOnKeyboard( [Key.ctrl, 'z'] )    ; return
    if th.currentEvent == "uparrow"     : pressOnKeyboard( [Key.up] )           ; return
    if th.currentEvent == "selectall"   : pressOnKeyboard( [Key.ctrl, 'a'] )    ; return
    if th.currentEvent == "leftarrow"   : pressOnKeyboard( [Key.left] )         ; return
    if th.currentEvent == "downarrow"   : pressOnKeyboard( [Key.down] )         ; return
    if th.currentEvent == "rightarrow"  : pressOnKeyboard( [Key.right] )        ; return

# Media button press handler
def mediaButtonHandler():
    global th
    if th.currentEvent ==  "playpause"     : pressOnKeyboard( [Key.media_play_pause] )   ; return
    if th.currentEvent ==  "escape"        : pressOnKeyboard( [Key.esc] )                ; return
    if th.currentEvent ==  "previous"      : pressOnKeyboard( [Key.media_previous] )     ; return
    if th.currentEvent ==  "fullscreen_yt" : pressOnKeyboard( ['f'] )                    ; return
    if th.currentEvent ==  "next"          : pressOnKeyboard( [Key.media_next] )         ; return
    if th.currentEvent ==  "volumeup"      : pressOnKeyboard( [Key.media_volume_up] )    ; return
    if th.currentEvent ==  "mute"          : pressOnKeyboard( [Key.media_volume_mute] )  ; return
    if th.currentEvent ==  "volumedown"    : pressOnKeyboard( [Key.media_volume_down] )  ; return
    if th.currentEvent ==  "open"          : pressOnKeyboard( [Key.ctrl, 'o'] )          ; return
    if th.currentEvent ==  "closeprogram"  : pressOnKeyboard( [Key.alt, Key.f4] )        ; return
    if th.currentEvent ==  "fullscreen"    : pressOnKeyboard( [Key.alt, Key.enter] )     ; return
    if th.currentEvent ==  "changefocus"   : pressOnKeyboard( [Key.alt, Key.tab] )       ; return

#Handles the requests
def api_handler(message):
    global th
    messageDict = message

    th.currentEvent = messageDict['eventType']
    #print(messageDict)
    # Mousemove events
    if  th.currentEvent in ["touchstart", "touchend", "touchmove" , "touchcancel"]:
        th.currentXArray = messageDict['xCoordinateArray'] if "xCoordinateArray" in messageDict else []
        th.currentYArray = messageDict['yCoordinateArray'] if "yCoordinateArray" in messageDict else []
        th.currentTouchIDArray = messageDict['coordinateIdentifier'] if "coordinateIdentifier" in messageDict else []

        touchEventHandler()
        return

    # Mouse button events
    if th.currentEvent in ["leftclick", "rightclick", "midclick"]:
        mouseButtonHandler()
        return

   # Keyboard button events
    if ( 
            th.currentEvent in [
            "enter",
            "backspace",
            "delete",
            "home",
            "end",
            "pageup",
            "pagedown",
            "printscreen",
            "copy",
            "paste",
            "desktop",
            "contextmenu",
            "undo",
            "uparrow",
            "selectall",
            "leftarrow",
            "downarrow",
            "rightarrow"
            ]
            ):
        keyboardButtonHandler()
        return

    # Multimedia button events
    if ( 
            th.currentEvent in [
            "playpause",
            "escape",
            "previous",
            "fullscreen_yt",
            "next",
            "volumeup",
            "mute",
            "volumedown",
            "open",
            "closeprogram",
            "fullscreen",
            "changefocus"
            ]
            ):
            mediaButtonHandler()
            return