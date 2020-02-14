import argparse


def check():
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))


if __name__ == "__main__":
        check()
        from s_game import Snek
        s = Snek()
        s.main()