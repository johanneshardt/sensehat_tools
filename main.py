from sense_hat import SenseHat
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
            self.speed = 0.8
        

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

            self.position = directions[input](pos)
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

        def collision(self):
            self.status = False

        
        def main(self):
            print('Game time started')
            for _ in range(5):
                self.draw()
                self.move()
                sleep(self.speed)
    s = Snek()
    s.main()
if __name__ == "__main__":
        check()
        s_game()