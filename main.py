from capture import Captura
from handDraw import MaoDeteccao
import cv2


def main():

    video = Captura()
    mao = MaoDeteccao()

    while True:
        sucesso, img = video.ler_frame()
        if not sucesso:
            break

        resultados = mao.processar(img)
        mao.desenhar(img, resultados)

        cv2.imshow("Tela Espelho", img)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
            break

    video.liberar()


if __name__ == "__main__":
    main()
