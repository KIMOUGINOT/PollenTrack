from MyApp import *

if __name__ == "__main__":
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22
    pins_list = [in1, in2, in3, in4]
    cam = Camera(pins_list)
    cam.calibrage()