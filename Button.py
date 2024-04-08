import RPi.GPIO as GPIO
import time

class Button():
    def __init__(self, pin):
        self.pin = pin
        self.last_time = 0
        self.callback_single = None
        self.callback_double = None
        self.double_click_interval = 0.3 # intervalle pour le double clic en secondes

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self._button_callback, bouncetime=200)

    def _button_callback(self, channel):
        current_time = time.time()
        if current_time - self.last_time < self.double_click_interval:
            if self.callback_double:
                self.callback_double()
        else:
            if self.callback_single:
                self.callback_single()
        self.last_time = current_time

    def on_single_click(self, callback):
        self.callback_single = callback

    def on_double_click(self, callback):
        self.callback_double = callback

if __name__ == "__main__":
    # Exemple d'utilisation
    def single_click_callback():
        print("Clic simple détecté")

    def double_click_callback():
        print("Double clic détecté")
    button = Button(11)  # Utilisez le numéro de la broche GPIO à laquelle le bouton est connecté
    button.on_single_click(single_click_callback)
    button.on_double_click(double_click_callback)

    try:
        while True:
            time.sleep(0.1) # Garde le programme actif pour écouter les événements du bouton
    except KeyboardInterrupt:
        GPIO.cleanup()  # Nettoie les broches GPIO lors de l'arrêt du programme

