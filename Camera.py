from picamera2 import Picamera2, Preview
import keyboard
from Motor import *
import cv2
import numpy as np
from camera_utilities import blurriness, pollenDetection

class Camera(Picamera2):
    def __init__(self, camera_motor_pins) :
        super().__init__()
        camera_config = self.create_preview_configuration()
        in1, in2, in3, in4 = camera_motor_pins
        self.motor = Motor(in1, in2, in3, in4)
        self.configure(camera_config)

    def take_picture(self, image_path, image_name):
        """ Take an image and save it to image_path with the label image_name

        Args:
            image_path (_string_):
            image_name (_string_): 
        """
        self.start_preview(Preview.NULL)
        self.start()
        self.capture_file(image_path+image_name) 

    def calibrage(self):
        # state = True
        # def set_state_false():
        #     state = False
        # keyboard.add_hotkey('z', lambda : self.zoom(True))
        # keyboard.add_hotkey('s', lambda : self.zoom(False))
        # keyboard.add_hotkey('a', set_state_false)
        self.start_preview()
        # while state :
        #     pass
        # self.stop_preview()

    def zoom(self, direction):
        self.motor.move(100, direction)

    def focus(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        image = np.array(frame)
        x, y, w, h = pollenDetection.pollen_detection(image)
        cropped_image = image[y:y+h, x:x+w]
        sharpness = blurriness.measure_blurriness(cropped_image)
        self.zoom(True)

        for _ in range(20) :
            cap = cv2.VideoCapture(0)
            ret, frm = cap.read()
            cap.release()
            img = np.array(frm)
            cropped_image = img[y:y+h, x:x+w]
            var = blurriness.measure_blurriness(cropped_image)
            if var > sharpness :
                image = img
                sharpness = var
                self.zoom(True)
            else :
                self.zoom(False)
        
        return image