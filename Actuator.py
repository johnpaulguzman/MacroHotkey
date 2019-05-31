import pyautogui
import pywinauto

class Actuator:
    def key_translator(self, string):
        pass  # TODO !!!

    def __init__(self, default_interval=0.1, debug=False):
        self.default_interval = default_interval
        self.logger = lambda s: print(f"  > {s}") if debug else lambda s: None

    def send_keys(self, key_codes, interval=None):
        """ Sends keys or key codes (key + down or up) via DirectX """
        interval = self.default_interval if interval is None else interval
        format_keys = lambda key: key if type(key) is str else f"{{{key[0]} {'down' if key[1] else 'up'}}}"
        format_keys = "".join(map(format_keys, key_codes))
        self.logger(f"Sending: {format_keys}")
        pywinauto.keyboard.send_keys(format_keys, pause=interval)

    def send_clicks(self, positions=(None, ), is_left=True, interval=None):
        """ Sends clicks ... """
        interval = self.default_interval if interval is None else interval
        for position in positions:
            pos_args = [] if position is None else position
            mode = "left" if is_left else "right"
            self.logger(f"Clicking: {pos_args} {mode}")
            pyautogui.click(*pos_args, button=mode, interval=interval)

    def pos(self):
        return pyautogui.position()

    def move(self, position):
        pyautogui.moveTo(position)

if __name__ == '__main__':
    a = Actuator(default_interval=0.1, debug=True)
    a.send_keys(list("hello") + [('VK_SHIFT', True)] + list("world") + [('VK_SHIFT', False)] + list("!!!"))
    a.send_clicks([None, None, (1, 1)])
