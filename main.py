from MyApp import *

if __name__ == "__main__":

    fan_pin = 9 #inserer les pins
    led_pins = [23, 24, 8] #inserer les pins
    camera_pins = [2, 3, 17, 27]
    motor_pins = [26, 19] #inserer les pins
    button_pin = 11 #inserer les pins

    cycle = MyApp(fan_pin, led_pins, motor_pins, camera_pins, button_pin)
    # cycle.routine_test_sans_button()
    cycle.led.on(0,0,1)
    cycle.camera.calibrage()
    cycle.camera.zoom(100,True)
    cycle.camera.focus()
    cycle.off()
     