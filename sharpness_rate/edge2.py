import cv2
import matplotlib.pyplot as plt

# Charger l'image
image_path = "champ_clair_element_milieu_haut.jpg"  # Remplacez ceci par le chemin de votre image
img = cv2.imread(image_path)
# # Convertir l'image en niveaux de gris
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Détection de contours avec l'algorithme de Canny
# edges = cv2.Canny(gray_img, 100, 200)  # Ajustez ces valeurs selon vos besoins

# # Superposer les bords détectés sur l'image d'origine
# overlay = img.copy()
# overlay[edges != 0] = [0, 255, 0]  # Mettre les pixels des bords en vert (0, 255, 0)

# Afficher l'image avec les bords détectés
plt.imshow(img)
plt.title('Image avec les bords détectés')
plt.axis('off')  # Masquer les axes
plt.show()
