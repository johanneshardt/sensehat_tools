import argparse
from sense_hat import SenseHat


sense = SenseHat()


def check():
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))


if __name__ == "__main__":
        check()
        from snake import Snek
        s = Snek()
        s.main(speed=0.3)