from picamera2 import Picamera2, Preview
# import keyboard
from Motor import *
import cv2
import numpy as np
from camera_utilities import blurriness, pollenDetection

class Camera(Picamera2):
    def __init__(self, camera_motor_pins) :
        super().__init__()
        camera_config = self.create_preview_configuration(main={"size" : (800, 600)})
        self.motor = Motor(camera_motor_pins)
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

    def take_3_pictures(self, image_path, image_name):
        """ Acquire 3 pictures with a slight difference in focus and save it to image_path with the label image_name

        Args:
            image_path (string): 
            image_name (string): 
        """
        self.focus()
        for i in range(3):
            # Changer la mise au point pour chaque prise de vue
            
            if i == 1:
                self.zoom(False)
            elif i == 2:
                self.zoom(True)
                self.zoom(True) 

            # Prendre une photo avec la mise au point actuelle
            # Enregistrer l'image
            self.take_picture(image_path, f"{image_name}_{i+1}.jpg")


    def calibrage(self):
        # state = True
        # def set_state_false():
        #     state = False
        # keyboard.add_hotkey('z', lambda : self.zoom(True))
        # keyboard.add_hotkey('s', lambda : self.zoom(False))
        # keyboard.add_hotkey('a', set_state_false)
        self.start_preview(Preview.QTGL)
        self.start()
        # while state :
        #     pass
        # self.stop_preview()

    def zoom(self, direction):
        """activate the motor for x steps to the direction given in parameters

        Args:
            direction (_bool_): True if clock-wise and False in the opposite case
        """
        self.motor.move(100, direction)

    def focus(self):
        """Activate the motor to get the image sharp using pollen detection and blurriness measurement
        """
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

    def off(self) :
        self.motor.off()