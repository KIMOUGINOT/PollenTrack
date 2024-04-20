import RPi.GPIO as GPIO
import time

import RPi.GPIO as GPIO
import threading
import time

class Button(threading.Thread):
    def __init__(self, pin):
        super().__init__()
        self.pin = pin
        self.callback_single = None
        self.callback_double = None
        self.double_click_interval = 0.3  # intervalle pour le double clic en secondes
        self.running = True
        self.last_time = 0
        self.click_count = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def set_callback_single(self, callback):
        self.callback_single = callback

    def set_callback_double(self, callback):
        self.callback_double = callback

    def run(self):
        while self.running:
            if GPIO.input(self.pin) == GPIO.LOW:
                current_time = time.time()
                if current_time - self.last_time > self.double_click_interval:
                    # Nouveau clic simple détecté
                    self.click_count = 1
                else:
                    # Clic supplémentaire dans l'intervalle du double clic
                    self.click_count += 1

                self.last_time = current_time

                if self.click_count == 1 and self.callback_single:
                    # Exécuter le callback pour un clic simple
                    self.callback_single()
                elif self.click_count == 2 and self.callback_double:
                    # Exécuter le callback pour un double clic
                    self.callback_double()

                # Attendre que le bouton soit relâché pour éviter les détections répétées
                while GPIO.input(self.pin) == GPIO.LOW:
                    time.sleep(0.05)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    def single_click_callback():
        print("Clic simple détecté")

    def double_click_callback():
        print("Double clic détecté")

    button = Button(11)  # Utilisez le numéro de la broche GPIO à laquelle le bouton est connecté
    button.set_callback_single(single_click_callback)
    button.set_callback_double(double_click_callback)
    button.start()  # Démarrez le thread d'écoute du bouton

    try:
        while True:
            # Votre routine principale à exécuter ici
            print("Routine en cours...")
            time.sleep(1)  # Exemple : attendre 1 seconde entre chaque étape de la routine
    except KeyboardInterrupt:
        pass
    finally:
        button.stop()  # Arrêtez le thread d'écoute du bouton
        button.join()  # Attendez que le thread se termine
        GPIO.cleanup()  # Nettoyez les broches GPIO à la fin du programme


