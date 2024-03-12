import cv2

def apply_blur_and_save(image_path, output_path, blur_type='gaussian', kernel_size=(5, 5)):
    # Charger l'image
    image = cv2.imread(image_path)

    # Appliquer le flou gaussien ou le flou moyen
    if blur_type == 'gaussian':
        blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    elif blur_type == 'average':
        blurred_image = cv2.blur(image, kernel_size)
    else:
        raise ValueError("Invalid blur type. Choose 'gaussian' or 'average'.")

    # Enregistrer l'image floue
    cv2.imwrite(output_path, blurred_image)

# Chemin vers l'image d'entrée
image_path = "image/colourForms.png"

# Chemin de sortie pour l'image floue
output_path = "samples/sample_6/cropped_image/colourFormsBlurred.png"

# Appliquer le flou gaussien par défaut
apply_blur_and_save(image_path, output_path)

# Vous pouvez également spécifier le type de flou et la taille du noyau (kernel)
# apply_blur_and_save(image_path, output_path, blur_type='average', kernel_size=(7, 7))
