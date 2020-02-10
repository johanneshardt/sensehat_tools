from sense_hat import SenseHat

def check():
        sense = SenseHat()
        print("Humidity:     {}".format(sense.humidity))
        print("Temperatur:   {}".format(sense.temp))
        print("Pressure:     {}".format(sense.pressure))
        print("North:        {}".format(sense.compass))

if __name__ == "__main__":
        check()


sense = SenseHat()
sense.show_message('bruh')