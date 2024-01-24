import cv2
import numpy as np

# Charger l'image
image_path = "Logo_Pollentrack.png"
image = cv2.imread(image_path)

# Vérifier si l'image est chargée correctement
if image is None:
    print("Impossible de charger l'image.")
    exit()

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un flou pour améliorer la détection des contours (facultatif)
gray_image_blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Utiliser la détection de contours Canny
edges = cv2.Canny(gray_image_blurred, 50, 150)

# Afficher l'image originale, en niveaux de gris, et les contours détectés
cv2.imshow("Image Originale", image)
cv2.imshow("Image en Niveaux de Gris", gray_image)
cv2.imshow("Contours Détectés", edges)

# Attendre une touche et fermer les fenêtres
cv2.waitKey(0)
cv2.destroyAllWindows()
