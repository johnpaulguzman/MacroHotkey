from pynput import keyboard

class HotkeyHandler:
    def key_translator(self, string):
        if len(string) == 1:
            return keyboard.KeyCode(char=string)
        elif len(string) > 1:
            return keyboard.Key.__members__.get(string, None)

    def __init__(self, raw_combos, debug=False):
        self.combos = {tuple((self.key_translator(k) for k in key)): val for key, val in raw_combos.items()}
        for (key, val) in self.combos.items(): print(f"Loaded combo: {[str(k) for k in key]} for `{val[0].__name__}` with args {val[1: ]}")
        self.logger = lambda s: print(f"  > {s}") if debug else lambda s: None
        self.pressed_keys = list()
        self.void = (lambda: None, )

    def on_press(self, key):
        if key not in self.pressed_keys:
            self.pressed_keys.append(key)

    def on_release(self, key):
        (callback, *args) = self.combos.get(tuple(self.pressed_keys), self.void)
        self.logger(f"Pressed keys {self.pressed_keys}")
        self.logger(f"Running {callback.__name__}{args}")
        if (callback, *args) == self.void:
            self.pressed_keys = []
        elif key in self.pressed_keys:
            self.pressed_keys.remove(key)
        return callback(*args)

    def start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.logger(f"Joining listener {listener} to main thread")
            listener.join()


if __name__ == '__main__':
    def stop():
        print("Sending stop signal to listener...\n")
        return False
    combos = { ('shift', 'f12'): (stop, ), }
    h = HotkeyHandler(combos, debug=True)
    h.start()
