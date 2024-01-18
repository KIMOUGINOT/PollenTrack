import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "image/champ_clair_element_milieu_haut.jpg"

image = cv2.imread(IMAGE_PATH)
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Détection de contours avec l'algorithme de Canny
edges = cv2.Canny(gray_img, 0, 80)  # Ajustez ces valeurs selon vos besoins

# Recherche des contours dans l'image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
# Création d'une copie de l'image originale pour dessiner les contours


# Dessiner les contours sur l'image copiée
minArea = min(cv2.contourArea(contours))
maxArea = max(cv2.contourArea(contours))
meanArea = (minArea + maxArea)/2
contour_img =cv2.drawContours(image, [c for c in contours if cv2.contourArea(c)>meanArea], -1, (0, 255, 0), 2)

plt.imshow(contour_img)
plt.title('Image avec les bords détectés')
plt.axis('off')  # Masquer les axes
plt.show()
