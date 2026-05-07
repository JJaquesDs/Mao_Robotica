import cv2


class Captura:

    """ Classe para lidar com captura de vídeo """

    def __init__(self, largura=640, altura=480):

        """ Função de inicialização """
        self.captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.captura.set(3, largura)
        self.captura.set(4, altura)

    def ler_frame(self):

        """ Função para ler os frames da captura com cv2"""
        sucesso, img = self.captura.read()
        return sucesso, img

    def liberar(self):

        """ Função para fechar janela """
        self.captura.release()
        cv2.destroyAllWindows()
