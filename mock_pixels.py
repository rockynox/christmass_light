class MockPixels:
    def __init__(self, debug: bool = False):
        self.debug = debug

    def __setitem__(self, index, val):
        if self.debug:
            print(f"LED{index} -> {val}")

    def show(self):
        pass

    def fill(self, colors):
        if self.debug:
            print(f"FILL with {colors}")
