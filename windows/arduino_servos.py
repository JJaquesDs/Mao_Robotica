from pyfirmata2 import Arduino, SERVO, util
import time


class SetupArduino:

    def __init__(self):
        self.placa: Arduino = Arduino('COM7')  # Porta que vai ficar o arduino

        # pinos
        
        self.pin1: int = 7  # pinos que vão controlar os servos
        self.pin2: int = 6
        self.pin3: int = 5
        self.pin4: int = 4
        self.pin5: int = 3

        self.placa.digital[self.pin1].mode = SERVO
        self.placa.digital[self.pin2].mode = SERVO
        self.placa.digital[self.pin3].mode = SERVO
        self.placa.digital[self.pin4].mode = SERVO
        self.placa.digital[self.pin5].mode = SERVO

    def rotacionar_servo(self, pino, angulo, invertido=False):
        """ Função que rotaciona o servo: ajustar a rotação conforme o servo estiver na mão """

        if invertido:
            angulo = 180 - angulo

        self.placa.digital[pino].write(angulo)
        time.sleep(0.015)

    def abrir_fechar(self, pino, on_off, invertido=False):
        if on_off == 1:
            self.rotacionar_servo(pino, 140, invertido)
        else:
            self.rotacionar_servo(pino, 0, invertido)

    def service_movimentos(self, pinos):
        """ Método que contém a lógica de movimentação dos dedos """
        pontos = []  #  Uma matriz para guardar os pontos da mão




