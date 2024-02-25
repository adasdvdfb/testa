import pyxel

particles = [
    {
        "name": "egg",
        "result": False
    },
    {
        "name": "salt",
        "result": False
    },
]

class App:
    string = ""
    selected = 0
    def __init__(self):
        pyxel.init(100, 100, "Cooking Game")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_E):
            self.selected += 1
        elif pyxel.btnp(pyxel.KEY_KP_ENTER):
            self.string += particles[self.selected][0]

    def draw(self):
        pyxel.text(10,10, "Selected: " + self.selected)
        pyxel.text(10,20, "Prepared: " + self.string)

App()