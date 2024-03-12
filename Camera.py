from picamera2 import Picamera2, Preview

class Camera(Picamera2):
    def __init__(self) :
        super().__init__()
        camera_config = self.create_preview_configuration()
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