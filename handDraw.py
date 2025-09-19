import mediapipe as mp
import cv2

from arduino_servos import SetupArduino

class MaoDeteccao:
    """ Classe para detectar a mão com cv2 e mediapipe"""

    def __init__(self, arduino: SetupArduino, max_maos=1):

        """ Função de inicialização """
        self.mao = mp.solutions.hands
        self.mao_obj = self.mao.Hands(max_num_hands=max_maos)
        self.mp_desenho = mp.solutions.drawing_utils
        self.arduino = arduino

    def processar(self, img):

        """ Função para processar a imagem da mão com cv2 para rgb"""
        frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resultados = self.mao_obj.process(frame_rgb)
        return resultados

    def desenhar(self, img, resultados):

        pontos = []
        h, w, _ = img.shape

        """ Função para desenhar os pontos na mão com mediapipe """
        if resultados.multi_hand_landmarks:
            for pontos_mao in resultados.multi_hand_landmarks:
                self.mp_desenho.draw_landmarks(img, pontos_mao, self.mao.HAND_CONNECTIONS)
                # podemos enumerar esses pontos da seguinte forma
                for id, cord in enumerate(pontos_mao.landmark):
                    cx, cy = int(cord.x * w), int(cord.y * h)
                    # cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    cv2.circle(img, (cx, cy), 4, (255, 0, 0), -1)
                    pontos.append((cx, cy))

                if pontos:
                    """
                    A enquete para descobrir se o anelar era maior ou menor que o indicador ficou:
                        menor -- 29%
                        maior -- 61%
                        não sei, desconfio que meus dedos são tortos :-( -- 10%
                    
                    Obrigado a todos os contribuintes da pesquisa!
                    """
                    dist_polegar = abs(pontos[17][0] - pontos[4][0])
                    dist_indicador = pontos[5][1] - pontos[8][1]
                    dist_medio = pontos[9][1] - pontos[12][1]
                    dist_anelar = pontos[13][1] - pontos[16][1]
                    dist_mindinho = pontos[17][1] - pontos[20][1]

                    if dist_polegar < 80:

                        self.arduino.abrir_fechar(self.arduino.pin1, 1)
                    else:
                        self.arduino.abrir_fechar(self.arduino.pin1, 0)

                    if dist_indicador > 40:
                        self.arduino.abrir_fechar(self.arduino.pin2, 0)
                    else:
                        self.arduino.abrir_fechar(self.arduino.pin2, 1)

                    if dist_medio > 40:
                        self.arduino.abrir_fechar(self.arduino.pin3, 0)
                    else:
                        self.arduino.abrir_fechar(self.arduino.pin3, 1)

                    if dist_anelar > 40:
                        self.arduino.abrir_fechar(self.arduino.pin4, 0)
                    else:
                        self.arduino.abrir_fechar(self.arduino.pin4, 1)

                    if dist_mindinho > 40:
                        self.arduino.abrir_fechar(self.arduino.pin5, 0)
                    else:
                        self.arduino.abrir_fechar(self.arduino.pin5, 1)

