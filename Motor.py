import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

# Définition des broches du pilote ULN2003AN connectées au moteur
coil_A_1_pin = 17
coil_A_2_pin = 27
coil_B_1_pin = 22
coil_B_2_pin = 23

# Initialisation des objets GPIO pour chaque broche
coil_A_1 = GPIO(coil_A_1_pin)
coil_A_2 = GPIO(coil_A_2_pin)
coil_B_1 = GPIO(coil_B_1_pin)
coil_B_2 = GPIO(coil_B_2_pin)

# Liste des séquences pour faire tourner le moteur
sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

class Motor():

    # Fonction pour faire tourner le moteur d'un pas dans une direction donnée
    def set_step(step, direction):
        coil_A_1.value = sequence[step][0]
        coil_A_2.value = sequence[step][1]
        coil_B_1.value = sequence[step][2]
        coil_B_2.value = sequence[step][3]

    # Fonction pour faire tourner le moteur d'un nombre donné de pas dans une direction donnée
    def move(steps, direction):
        for _ in range(steps):
            for step in range(8):
                set_step(step, direction)
                sleep(0.001)  # Délai entre chaque pas

    # Exemple : Faire tourner le moteur de 512 pas dans le sens horaire
    move(512, direction=1)

    # Arrêt du moteur
    def off(self):
        coil_A_1.off()
        coil_A_2.off()
        coil_B_1.off()
        coil_B_2.off()
