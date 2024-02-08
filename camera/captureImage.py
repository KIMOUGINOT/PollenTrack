import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)  # Définir la résolution de l'image
    camera.start_preview()  # Démarrer la prévisualisation de la caméra
    input("Appuyez sur Entrée pour capturer l'image...")
    camera.capture('image.jpg')  # Capturer et enregistrer l'image sous le nom 'image.jpg'
