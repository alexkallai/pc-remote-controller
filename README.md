# Windows PC remote controller
Control a Windows PC without client app, using a web server

### Current features are:

- mouse control with dedicated buttons for mouse buttons
multitouch support (for zoom and gestures) not implemented yet
- general media controls
- frequent Windows shortcuts and other useful controls


### Planned features
- multi-touch support
- authentication
- installer
- control / settings from tray icon

### Current UI

![Example image](https://raw.githubusercontent.com/alexkallai/pc-remote-controller/main/example_images/mouse_page.PNG)


### Requirements for Linux:
- <= Python 3.9 (was tested on 3.9)
- xdotool (sudo apt install xdotool)
- Linux requires sudo, because of the input simulations


### Requirements for Windows:
- TODO