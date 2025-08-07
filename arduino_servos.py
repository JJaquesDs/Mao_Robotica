from pyfirmata import Arduino, SERVO


def setup_arduino():
    placa = Arduino('')  # Porta que vai ficar o arduino

    # pinos
    pin1 = 0
    pin2 = 0
    pin3 = 0
    pin4 = 0

    placa.digital[pin1].mode = SERVO
    placa.digital[pin2].mode = SERVO
    placa.digital[pin3].mode = SERVO
    placa.digital[pin4].mode = SERVO

    # TODO: talvez um for pra ter menos retornos?
    return placa, pin1, pin2, pin3, pin4

