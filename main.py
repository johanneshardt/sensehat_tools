from sense_hat import SenseHat

sense = SenseHat()

def check():
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))


def show(matrix, colors={}):
    matrix = [colors[s] for s in matrix]
    sense.set_pixels = matrix

if __name__ == "__main__":
        check()
        c = {0: [0, 0, 0], 1: [0, 255, 0]}
        m = [O, O, O, 1, 1, O, O, O,
            O, O, 1, O, O, 1, O, O,
            O, O, O, O, O, 1, O, O,
            O, O, O, O, 1, O, O, O,
            O, O, O, 1, O, O, O, O,
            O, O, O, 1, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, 1, O, O, O, O]

        show(m)


sense = SenseHat()
sense.show_message('bruh')