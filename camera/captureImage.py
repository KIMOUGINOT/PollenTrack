from picamera2 import Picamera2, Preview

def take_picture(image_path, image_name):
    """_take an image and save it to image_path with the label image_name_

    Args:
        image_path (_string_):
        image_name (_string_): 
    """
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start_preview(Preview.NULL)
    picam2.start()
    picam2.capture_file(image_path+image_name)
