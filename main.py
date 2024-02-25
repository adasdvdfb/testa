import pyxel
import random
import time

foodx = random.randint(20, 95)
foody = random.randint(20, 95)

cellx = random.randint(75, 95)
celly = random.randint(75, 95)

smarts = 1
eaten = 750
pump = 0
lung = 0
model = ""
_type = ""
color = 2

class App:
    def __init__(self):
        global model
        if (smarts > 0) and (smarts <= 3):
            model = "DAVSMART1"
        elif  (smarts > 3) and (smarts <= 7):
            model = "DAVSMART2"
        elif smarts > 14:
            model = "DAVSMART3"
        pump = eaten / 17 + random.randint(1, 3)
        sugar = eaten * 8 + random.randint(1, 3)
        lung = eaten * 17 + random.randint(1, 3)
        pyxel.init(160, 120, title=f"Cell - Info: Mind Power: {smarts}, Sugar Storage: {eaten}, Sugar Water Pump: {pump}, Sugar Particles: {sugar}, Respiratory Power: {lung}")
        if eaten > 0:
            pyxel.run(self.update, self.draw)
        else:
            pyxel.run(self.update, self.lose)

    def is_touching_food(self):
        touch_range = 6
        return abs(foodx - cellx) < touch_range and abs(foody - celly) < touch_range

    def move(self, model):
        global foodx, foody, cellx, celly, smarts, eaten
        if model == "DAVSMART3":
            if foodx > cellx:
                cellx += 5
            elif foodx < cellx:
                cellx -= 5
            if foody > celly:
                celly += 5
            elif foody < celly:
                celly -= 5
        elif model == "DAVSMART2":
            local = random.randint(1, 3)
            if local == 3:
                if foodx > cellx:
                    cellx += 5
                elif foodx < cellx:
                    cellx -= 5
                if foody > celly:
                    celly += 5
                elif foody < celly:
                    celly -= 5
            else:
                localx = random.randint(10, 100)
                localy = random.randint(10, 100)
                if localx > cellx:
                    cellx += 5
                elif localx < cellx:
                    cellx -= 5
                if localy > celly:
                    celly += 5
                elif localy < celly:
                    celly -= 5
        elif model == "DAVSMART1":
            localx = random.randint(10, 100)
            localy = random.randint(10, 100)
            if localx > cellx:
                cellx += 5
            elif localx < cellx:
                cellx -= 5
            if localy > celly:
                celly += 5
            elif localy < celly:
                celly -= 5

        if self.is_touching_food():
            smarts += 1
            foodx = random.randint(20, 95)
            foody = random.randint(20, 95)
            eaten += 10
        else:
            eaten -= 0.25

    def update(self):
        global cellx, celly, foody, foodx, model, eaten, _type, color
        pyxel.mouse(visible=True)
        if (smarts > 0) and (smarts <= 5):
            model = "DAVSMART1"
            _type = "Cell"
            color = 2
        elif  (smarts > 5) and (smarts <= 7):
            model = "DAVSMART2"
            _type = "Larvae"
            color = 16
        elif smarts > 15:
            model = "DAVSMART3"
            _type = "Fly"
            color = 1
        pump = eaten / 17 + random.randint(1, 3)
        sugar = eaten * 8 + random.randint(1, 3)
        lung = eaten * 17 + random.randint(1, 3)
        pyxel.title(f"Cell - Info: Mind Power: {smarts}, Sugar Storage: {eaten}, Sugar Water Pump: {pump}, Sugar Particles: {sugar}, Respiratory Power: {lung}")
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_E):
            cellx = pyxel.mouse_x
            celly = pyxel.mouse_y
        elif pyxel.btnp(pyxel.KEY_Q):
            foodx = pyxel.mouse_x
            foody = pyxel.mouse_y
        elif pyxel.btnp(pyxel.KEY_F):
            foodx = cellx
            foody = celly
        elif pyxel.btnp(pyxel.KEY_G):
            eaten = 10
        if eaten < 1:
            self.lose()
        

    def draw(self):
        global _type, color
        self.move(model)
        pyxel.cls(0)
        pyxel.rect(foodx, foody, 10, 10, 9)
        pyxel.rect(cellx, celly, 8, 8, color)
        pyxel.text(10, 10, "Type: " + _type, 16)

    def lose(self):
        pyxel.cls(0)
        pyxel.text(45, 55, "STARVED TO DEATH", 16)
        time.sleep(5)
        pyxel.quit()
App()