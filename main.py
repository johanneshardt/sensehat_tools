from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep
from collections import deque

sense = SenseHat()

def check():
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))


def show(matrix, colors={}, brightness=1):
    for color in colors.values():
        for value in color:
            value *= brightness

    matrix = [colors[s] for s in matrix]
    sense.set_pixels(matrix)


def s_game():
    class Snek():
        def __init__(self):
            self.background = [0, 0, 0]
            self.color = [0, 255, 0]
            self.direction = 2
            self.length = 2
            self.matrix = [0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0]
            self.moved = True   
            self.moves = [1, -1]
            self.position = (2, 3)
            self.speed = 0.7
            self.status = True
            self.trail = deque([(1, 3), (2, 3)], maxlen=self.length)
        

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
                self.trail.append(self.position)
                self.moved = True


        def draw(self):

            color = {0: self.background, 1: self.color}

            matrix = [0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0]
            
            for part in self.trail:
                matrix[part[0]+part[1]*8] = 1

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

        def spawn():
            return
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
    s = Snek()
    s.main()


if __name__ == "__main__":
        check()
        s_game()