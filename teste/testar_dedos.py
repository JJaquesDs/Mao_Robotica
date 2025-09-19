from arduino_servos import SetupArduino
import time

arduino = SetupArduino()


def testar_todos():
    """ Função para testar os dedos, primeiro inicializa todos em 0 e rotaciona em angulo ajustável com sleep() """

    # pino 1 (indicador)
    arduino.rotacionar_servo(arduino.pin1, 130)  # testando com 130, mas pode ser ajustado conforme necessidade
    time.sleep(1)
    arduino.rotacionar_servo(arduino.pin1, 130)

    # pino 2 (médio)
    arduino.rotacionar_servo(arduino.pin2, 130)
    time.sleep(1)
    arduino.rotacionar_servo(arduino.pin2, 0)

    # pino 3 (anelar)
    arduino.rotacionar_servo(arduino.pin3, 130)
    time.sleep(1)
    arduino.rotacionar_servo(arduino.pin3, 0)

    # pino 4 (mindinho)
    arduino.rotacionar_servo(arduino.pin4, 130)
    time.sleep(1)
    arduino.rotacionar_servo(arduino.pin4, 0)
    print("fim do teste")
