import mediapipe as mp
import cv2


class MaoDeteccao:
    """ Classe para detectar a mão com cv2 e mediapipe"""

    def __init__(self, max_maos=1):

        """ Função de inicialização """
        self.mao = mp.solutions.hands
        self.mao_obj = self.mao.Hands(max_num_hands=max_maos)
        self.mp_desenho = mp.solutions.drawing_utils

    def processar(self, img):

        """ Função para processar a imagem da mão com cv2 """
        frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resultados = self.mao_obj.process(frame_rgb)
        return resultados

    def desenhar(self, img, resultados):

        """ Função para desenhar os pontos na mão com mediapipe """
        if resultados.multi_hand_landmarks:
            for hand_landmarks in resultados.multi_hand_landmarks:
                self.mp_desenho.draw_landmarks(img, hand_landmarks, self.mao.HAND_CONNECTIONS)
