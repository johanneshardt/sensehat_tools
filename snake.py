from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep
from collections import deque
from random import choice

sense = SenseHat()


def show(matrix, colors={}, brightness=1):
    for color in colors.values():
        for channel in color:
            channel *= brightness
    matrix = [colors[s] for s in matrix]
    sense.set_pixels(matrix)


class Snek:
    def __init__(self):
        self.bounds = lambda x, y: x < 0 or x > 7 or y < 0 or y > 7
        self.brightness = 1
        self.colors = {
            "background": [0, 0, 0],
            "death": [255, 0, 0],
            "fruit": [255, 0, 0],
            "snake": [0, 255, 0],
            "eaten_fruit": [255, 98, 0],
        }
        self.dimensions = (8, 8)
        self.direction = 2
        self.directions = {
            1: lambda pos: (pos[0], pos[1] - 1),
            -1: lambda pos: (pos[0], pos[1] + 1),
            2: lambda pos: (pos[0] + 1, pos[1]),
            -2: lambda pos: (pos[0] - 1, pos[1]),
        }
        self.eaten = None
        self.fruit = None
        self.length = 2
        self.matrix = [
            (x, y)
            for x in range(0, self.dimensions[0])
            for y in range(0, self.dimensions[1])
        ]
        self.moved = True
        self.moves = [1, -1]
        self.position = (2, 3)
        self.raw_direction = None
        self.speed = 0.5
        self.status = True
        self.trail = deque([(1, 3), (2, 3)], maxlen=self.length)

    def __repr__(self):
        return "snek -> status={},  length={}".format(self.status, self.length)

    def move(self):
        input = self.direction
        pos = self.position
        x, y = self.directions[input](pos)
        if self.bounds(x, y):
            self.status = False
        elif (x, y) in self.trail:
            self.status = False
        else:
            self.position = (x, y)
            if self.trail[-1] == self.fruit:
                self.eaten = self.fruit
                self.spawn()

            if self.trail[0] == self.eaten:
                self.eaten = None
                self.length += 1
                self.trail = deque(self.trail, maxlen=self.length)
            self.trail.append(self.position)
            self.moved = True

    def draw(self):
        colors = {
            0: self.colors["background"],
            1: self.colors["eaten_fruit"],
            2: self.colors["fruit"],
            3: self.colors["snake"],
        }

        screen = [0 for pos in self.matrix]
        brightness_steps = [
            int((channel - 0.2 * channel) // self.length)
            for channel in self.colors["snake"]
        ]

        for index, pos in enumerate(reversed(self.trail), 1):
            new_color = [
                int(channel - brightness_steps[i] * index)
                for i, channel in enumerate(self.colors["snake"])
            ]
            colors[index + 3] = new_color
            screen[pos[0] + pos[1] * 8] = index + 3

        screen[self.fruit[0] + self.fruit[1] * 8] = 2
        if self.eaten is not None:
            screen[self.eaten[0] + self.eaten[1] * 8] = 1

        show(screen, colors)

    def set_direction(self, event):
        input = self.direction
        self.moves = [move for move in [1, -1, 2, -2] if move not in [input, -input]]
        convert = {"up": 1, "left": -2, "down": -1, "right": 2, "middle": 1}
        if event.action == ACTION_PRESSED:
            new_direction = convert[event.direction]
            self.raw_direction = new_direction
            if new_direction in self.moves:
                if self.moved:
                    self.direction = new_direction
                    self.moved = False

    def spawn(self):
        possible = [spot for spot in self.matrix if spot not in self.trail]
        self.fruit = choice(possible)

    def choose_difficulty(self):
        sense.show_message("Difficulty:", scroll_speed=0.03)
        difficulty = 5
        sense.show_letter(str(difficulty))
        event = sense.stick.wait_for_event(emptybuffer=True)
        while event.direction != "middle":
            if event.direction == 'up' and difficulty < 9:
                difficulty += 1
            elif event.direction == 'down' and difficulty > 0:
                difficulty -= 1
            sense.show_letter(str(difficulty))
            event = sense.stick.wait_for_event(emptybuffer=True)
        self.speed = 0.5 - 0.05 * difficulty
        print('Speed set to: {}'.format(self.speed))

    def death(self):  # steps param used for testing
        colors = {0: self.colors["background"], 1: self.colors["death"]}
        screen = [0 for i in range(self.dimensions[0] * self.dimensions[1])]

        for part in self.trail:
            screen[part[0] + part[1] * 8] = 1
            show(screen, colors)
            sleep(0.03)

        sleep(0.5)
        sense.show_message("Score: {}".format(self.length), scroll_speed=0.03)

    def reset(self):
        self.status = True
        self.fruit = None
        self.eaten = None
        self.length = 2
        self.direction = 2
        self.position = (2, 3)
        self.trail = deque([(1, 3), (2, 3)], maxlen=self.length)

    def game(self):
        sense.stick.direction_any = self.set_direction
        while True:

            print("New game")
            self.choose_difficulty()
            self.spawn()
            self.draw()
            while self.status:
                sleep(self.speed)
                self.move()
                self.draw()
            self.death()
            sense.stick.wait_for_event(emptybuffer=True)
            self.reset()
