from capture import Captura
from handDraw import MaoDeteccao
#from teste import testar_dedos as teste
from arduino_servos import SetupArduino
import cv2


def main():

    video = Captura()
    arduino = SetupArduino()
    mao_img = MaoDeteccao(arduino)

    #teste.testar_todos()

    while True:
        sucesso, img = video.ler_frame()
        if not sucesso:
            break

        resultados = mao_img.processar(img)
        mao_img.desenhar(img, resultados)

        cv2.imshow("Tela Espelho", img)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
            break

    video.liberar()


if __name__ == "__main__":
    main()
