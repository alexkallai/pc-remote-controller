import pystray
import PIL.Image
import sys
import os

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_icon = os.path.abspath(os.path.join(bundle_dir, 'remote_icon.png'))

image = PIL.Image.open(path_to_icon)
icon_hint = "PC remote controller"

def click_handler(icon, item):
    if str(item) == "Do something":
        print("Did something!")
    if str(item) == "Exit":
        trayapp.stop()
        sys.exit()



menu_structure = pystray.Menu(
    pystray.MenuItem("Do something", click_handler),
    pystray.MenuItem("Exit", click_handler)
)
trayapp = pystray.Icon("Remote", image, icon_hint, menu=menu_structure)

#print("Tray icon starting!")
#trayapp.run()