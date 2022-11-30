import cv2
import mediapipe as mp


def tirar_foto(web_cam: int = 0):

    webcam = cv2.VideoCapture(web_cam)  # abrindo conexão com webcam

    if webcam.isOpened():
        validacao, frame = webcam.read()
        while validacao:
            validacao, frame = webcam.read()
            cv2.imshow("Video da Webcam", frame)
            key = cv2.waitKey(5)
            if key == 13:  # ENTER
                cv2.imwrite("Foto.png", frame)
                break
            if key == 27:  # ESC
                break

    webcam.release()  # fechando conexão com webcam
    cv2.destroyAllWindows()


def seguir_rosto(web_cam: int = 0):

    webcam = cv2.VideoCapture(web_cam)  # abrindo conexão com webcam

    # ativando a solução de reconhecimento de rosto
    reconhecimento_rosto = mp.solutions.face_detection
    # criando o item que consegue ler uma imagem e reconhecer os rostos ali dentro
    reconhecedor_rosto = reconhecimento_rosto.FaceDetection()
    # ativando a solução de desenho
    desenho = mp.solutions.drawing_utils

    while webcam.isOpened():
        validacao, frame = webcam.read()

        if not validacao:
            break

        # usa o reconhecedor para criar uma lista com os rostos reconhecidos
        lista_rostos = reconhecedor_rosto.process(frame)

        if lista_rostos.detections:  # caso algum rosto tenha sido reconhecido
            for rosto in lista_rostos.detections:  # para cada rosto que foi reconhecido
                # desenha o rosto na imagem
                desenho.draw_detection(frame, rosto)

        # mostra a imagem da webcam para a gente
        cv2.imshow("Rostos na sua webcam", frame)

        if cv2.waitKey(5) == 27:  # ESC # garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da webcam
            break

    webcam.release()  # encerra a conexão com a webcam
    cv2.destroyAllWindows()  # fecha a janela que mostra o que a webcam está vendo
