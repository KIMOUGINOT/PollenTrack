import cv2

image = cv2.imread("samples/sample_1/focus_overzoomed.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest_contour)
cropped_image = image[y:y+h, x:x+w]

# Enregistrer l'image recadrée
cv2.imwrite("samples/sample_1/cropped_image/test.png", cropped_image)
