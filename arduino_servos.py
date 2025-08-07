from pyfirmata import Arduino, SERVO
import time


class SetupArduino:

    def __init__(self):
        self.placa: Arduino = Arduino('')  # Porta que vai ficar o arduino

        # pinos
        self.pin1: int = 10  # pinos que vão controlar os servos
        self.pin2: int = 9
        self.pin3: int = 8
        self.pin4: int = 7

        self.placa.digital[self.pin1].mode = SERVO
        self.placa.digital[self.pin2].mode = SERVO
        self.placa.digital[self.pin3].mode = SERVO
        self.placa.digital[self.pin4].mode = SERVO

    def rotacionar_servo(self, pino: int, angulo: int):
        """ Função que rotaciona o servo: ajustar a rotação conforme o servo estiver na mão """

        self.placa.digital[pino].write(angulo)
        time.sleep(0.015)
