import sys
if sys.platform.startswith("win32"):
    import mouse
if sys.platform.startswith("linux"):
    import shutil
    from subprocess import run
    if not shutil.which("xdotool"):
        print("xdotool is not found with the which command, please install before running")
        quit()

# Wrapper class for mouse using xdotools
class Mousewrapper:

    def __init__(self) -> None:
        self.left = 1
        self.middle = 2
        self.right = 3
        self.wheel_up = 4
        self.wheel_down = 5

        self.buttonmap = {
            "left": self.left,
            "right": self.right,
            "middle": self.middle,
            "wheel_up": self.wheel_up,
            "wheel_down": self.wheel_down
        }

    def release(self, button="left"):
        run(["xdotool", "mouseup", f"{self.buttonmap[button]}"])

    def press(self, button="left"):
        run(["xdotool", "mousedown", f"{self.buttonmap[button]}"])

    def click(self, button="left"):
        run(["xdotool", "click", f"{self.buttonmap[button]}"])

    def move(self, x, y, absolute=False, duration=0):
        if absolute == False:
            run(["xdotool", "mousemove_relative", "--", f"{x}", f"{y}"])
        if absolute == True:
            run(["xdotool", "mousemove", f"{x}", f"{y}"])

    def scroll(self, y):
        # TODO
        pass
