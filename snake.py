from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep
from collections import deque
from random import choice

sense = SenseHat()

def show(matrix, colors={}, brightness=1):
    for color in colors.values():
        for value in color:
            value *= brightness

    matrix = [colors[s] for s in matrix]
    sense.set_pixels(matrix)


class Snek():
    def __init__(self):
        self.b_color    = [0, 0, 0]
        self.f_color    = [255, 0, 0]
        self.s_color    = [0, 255, 0]
        self.direction  = 2
        self.fruit      = None          #this is set in the main() loop
        self.length     = 2
        self.matrix     = [(x,y) for x in range(0,8) for y in range (0,8)]
        self.moved      = True   
        self.moves      = [1, -1]
        self.position   = (2, 3)
        self.speed      = 0.7
        self.status     = True
        self.trail      = deque([(1, 3), (2, 3)], maxlen=self.length)
    

    def __repr__(self):
        return "snek -> status={},  length={}".format(self.status, self.length)


    def move(self, input=None):
        if input is None:
            input = self.direction

        pos = self.position
        directions = { 1: lambda pos: (pos[0], pos[1]-1), #up
                        -1: lambda pos: (pos[0], pos[1]+1), #down
                        2: lambda pos: (pos[0]+1, pos[1]), #right
                        -2: lambda pos: (pos[0]-1, pos[1])} #left
        x, y = directions[input](pos)
        if x < 0 or x > 7 or y < 0 or y > 7:
            self.status = False
        else:
            self.position = (x,y)
            if self.trail[0] == self.fruit:
                self.lenth += 1
                self.trail = deque(self.trail, maxlen=self.length)
            self.trail.append(self.position)
            self.moved = True


    def draw(self):
        color = {0: self.b_color, 1: self.s_color, 2: self.f_color}
        matrix = [0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0]
        for part in self.trail:
            print(part)
            matrix[part[0]+part[1]*8] = 1
        matrix[self.fruit[0]+self.fruit[1]*8] = 2
        show(matrix, color, brightness=0.5)


    def set_direction(self, event, input=None):
        if input is None:
            input = self.direction
        self.moves = [move for move in [1,-1,2,-2] if move not in [input, -input]]
        convert = {'up': 1, 'left': -2, 'down': -1, 'right': 2, 'middle': 1}
        if event.action == ACTION_PRESSED:
            new_d = convert[event.direction]
            if new_d in self.moves:
                if self.moved:
                    self.direction = new_d
                    self.moved = False


    def spawn(self):
        possible = [spot for spot in self.matrix if spot not in self.trail]
        self.fruit = choice(possible)
        
        
    def death(self, pos=None, steps=50): # steps param used for testing
        if pos is None:
            pos = self.position
        red = {0: [255,0,0]}
        screen = [0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0]
        show(screen, {0: [255, 0, 0]})
        sleep(0.1)
        show(screen, {0: [0, 0, 0]})
        sense.show_message('Score: {}'.format(self.length))

    
    def main(self):
        while True:
            sense.stick.direction_any = self.set_direction
            print('New game')
            self.spawn()
            self.draw()
            while self.status:
                sleep(self.speed)
                self.move()
                self.draw()     
            self.death()
            sense.stick.wait_for_event(emptybuffer=True)
            self.status = True
            self.direction = 2
            self.position = (0,3)