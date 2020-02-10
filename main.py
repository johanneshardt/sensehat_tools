from sense_hat import SenseHat

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
        

        def __repr__(self):
            return "snek -> status={},  length={}".format(self.status, self.length)
    

        def move(input=self.direction, pos=self.position):
            directions = {'u': lambda pos: (pos[0]-1, pos[1]),
                          'l': lambda pos: (pos[0], pos[1]-1), 
                          'd': lambda pos: (pos[0]+1, pos[1]), 
                          'r': lambda pos: (pos[0], pos[1]+1)}

            self.position = directions[input](pos)


        def draw(pos=self.position):
            color = {0: self.background, 1: self.color}
            matrix = [0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0]
            
            matrix[(pos[0]-1)+pos[1]] = 1
            show(matrix, color)

        def collision(self):
            self.status = False
 
    s = Snek()
    s.draw()

if __name__ == "__main__":
        check()
        s_game()