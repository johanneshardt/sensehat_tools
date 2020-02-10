from sense_hat import SenseHat

sense = SenseHat()

def check():
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))


def show(matrix, colors={}):
    matrix = [colors[s] for s in matrix]]
    sense.set_pixels = matrix

if __name__ == "__main__":
        check()


sense = SenseHat()
sense.show_message('bruh')