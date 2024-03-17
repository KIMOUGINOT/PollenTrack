from MyApp import *

if __name__ == "__main__":
    in1 = 22
    in2 = 27
    in3 = 17
    in4 = 23
    pins_list = [in1, in2, in3, in4]
    cam = Camera(pins_list)
    cam.calibrage()
    cam.focus()
    cam.off()