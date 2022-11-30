class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


class MockPixels(Singleton):
    _pixels = {}

    def __init__(self, debug: bool = False):
        self.debug = debug

    def __setitem__(self, index, val):
        self._pixels[index] = val
        if self.debug:
            print(f"LED{index} -> {val}")

    def show(self):
        # if self.debug:
        #     print(f"###### SHOW ######")
        pass

    def fill(self, colors):
        if self.debug:
            print(f"FILL with {colors}")
