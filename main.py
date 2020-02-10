from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep

sense = SenseHat()
sense.stick.direction_any = direction

def check():
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))


def show(matrix, colors={}):
    matrix = [colors[s] for s in matrix]
    sense.set_pixels(matrix)


def direction(event):
    print(sense.stick.get_events[-1][1])


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
                self.position = directions[input](pos)
            except IndexError:
                self.status = False
            
            opposite = {'u': 'd', 'l': 'r', 'd': 'u', 'r': 'l'}
            self.moves = ['u', 'l', 'd', 'r'] - [input, opposite[input]]
            print(self.position)


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
            print('Game time started')
            while self.status:
                self.draw()
                self.move()
                sleep(self.speed)
    s = Snek()
    s.main()
if __name__ == "__main__":
        check()
        s_game()