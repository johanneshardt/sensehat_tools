import argparse
from sense_hat import SenseHat


sense = SenseHat()
parser = argparse.ArgumentParser(prog='sense_tools',
                                 description='''
                                        A collection of projects demonstrating the capabilities of 
                                        a raspberry pi sensehat-addon.''',
                                        
                                epilog='Created by Johannes hardt, 2020.')


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