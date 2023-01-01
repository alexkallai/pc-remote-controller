import pystray
import PIL.Image
import sys
import os

# Load icon
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_icon = os.path.abspath(os.path.join(bundle_dir, 'remote_icon.png'))
image = PIL.Image.open(path_to_icon)
# Specify mouse hover text
icon_hint = "PC remote controller"

# Functions for menu elements
def click_handler(icon, item):
    if str(item) == "Do something":
        print("Did something!")
    if str(item) == "Exit":
        # TODO if running in a separate thread, the whole process should be stopped
        trayapp.stop()
        sys.exit()

# Define menu structure
menu_structure = pystray.Menu(
    pystray.MenuItem("Do something", click_handler),
    pystray.MenuItem("Exit", click_handler)
)

# Menu will NOT appear on linux due to venv limitations
# https://github.com/moses-palmer/pystray/issues/20
trayapp = pystray.Icon("Remote", image, icon_hint, menu=menu_structure)

if __name__ == "__main__":
    print("Tray icon starting!")
    trayapp.run()