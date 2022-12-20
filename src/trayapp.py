import pystray
import PIL.Image

image = PIL.Image.open("src/remote_icon.png")
icon_hint = "PC remote controller"

def click_handler(icon, item):
    if str(item) == "Do something":
        print("Did something!")
    if str(item) == "Exit":
        trayapp.stop()

menu_structure = pystray.Menu(
    pystray.MenuItem("Do something", click_handler),
    pystray.MenuItem("Exit", click_handler)
)
trayapp = pystray.Icon("Remote", image, icon_hint, menu=menu_structure)

trayapp.run()