from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep

sense = SenseHat()

def check():
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))


def show(matrix, colors={}):
    matrix = [colors[s] for s in matrix]
    sense.set_pixels(matrix)


def s_game():
    class Snek():
        def __init__(self):
            self.status = True
            self.length = 2
            self.color = [0, 255, 0]
            self.background = [0, 0, 0]
            self.position = (3, 0)
            self.direction = 'r'
            self.moves = ['u', 'd']
            self.speed = 0.7
            self.bounds = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0]]
        

        def __repr__(self):
            return "snek -> status={},  length={}".format(self.status, self.length)
    

        def move(self, input=None):
            if input is None:
                input = self.direction
            
            pos = self.position
            directions = {'u': lambda pos: (pos[0]-1, pos[1]),
                          'l': lambda pos: (pos[0], pos[1]-1), 
                          'd': lambda pos: (pos[0]+1, pos[1]), 
                          'r': lambda pos: (pos[0], pos[1]+1)}

            try:
                new_pos = directions[input](pos)
                self.bounds[new_pos[0]][new_pos[1]]
                self.position = new_pos

            except IndexError:
                self.status = False
            
            opposite = {'u': 'd', 'l': 'r', 'd': 'u', 'r': 'l'}
            self.moves = [move for move in ['u', 'l', 'd', 'r'] if move not in [input, opposite[input]]]


        def draw(self, pos=None):
            if pos is None:
                pos = self.position
            
            color = {0: self.background, 1: self.color}
            matrix = [0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0]
            
            matrix[((pos[0])*8)+pos[1]] = 1
            show(matrix, color)


        def set_direction(self, event):
            convert = {'up': 'u', 'left': 'l', 'down': 'd', 'right': 'r'}
            if event.action == ACTION_PRESSED:
                new_d = convert[event.direction]
                if new_d in self.moves:
                    self.direction = new_d


        def death(self):
            blank = [0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]

            show(blank, {0: [255, 0, 0]})
            sleep(0.3)
            show(blank, {0: [0, 0, 0]})
            sense.show_message('Score: {}', self.length)

        
        def main(self):
            sense.stick.direction_any = self.set_direction
            print('Game time started')
            while self.status:
                self.draw()
                self.move()
                sleep(self.speed)
                       
            self.death()
    s = Snek()
    s.main()
if __name__ == "__main__":
        check()
        s_game()