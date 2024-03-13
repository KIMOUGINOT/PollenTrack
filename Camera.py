from picamera2 import Picamera2, Preview
from Motor import *
import cv2
import numpy as np
from camera_utilities import blurriness, pollenDetection

class Camera(Picamera2):
    def __init__(self) :
        super().__init__()
        camera_config = self.create_preview_configuration()
        self.motor = Motor()
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

    # def zoom(self, direction):
            

    def focus(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        image = np.array(frame)
        x, y, w, h = pollenDetection.pollen_detection(image)
        cropped_image = image[y:y+h, x:x+w]
        sharpness = blurriness.measure_blurriness(cropped_image)
        self.zoom(1)

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
                self.zoom(1)
            else :
                self.zoom(-1)
        
        return image