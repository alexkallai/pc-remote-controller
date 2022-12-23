from pynput.mouse import Controller, Button

class MousePynputWrapper:

    def __init__(self) -> None:
        self.mousecontroller = Controller()

        self.buttonmap = {
            "left": Button.left,
            "right": Button.right,
            "middle": Button.middle
        }

    def release(self, button="left"):
        self.mousecontroller.release(self.buttonmap[button])

    def press(self, button="left"):
        self.mousecontroller.press(self.buttonmap[button])

    def click(self, button="left"):
        self.mousecontroller.click(self.buttonmap[button], 1)

    def move(self, x, y, absolute=False, duration=0):
        if absolute == False:
            self.mousecontroller.move(x, y)
        if absolute == True:
            self.mousecontroller.position = (x, y)

    def scroll(self, y):
        # rist arg is the horizontal, second is the vertical scroll
        self.mousecontroller.scroll(0, y)