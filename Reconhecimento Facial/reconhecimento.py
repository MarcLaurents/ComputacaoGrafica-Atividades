import cv2

# Carregar o arquivo de treinamento do OpenCV
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializar a webcam
cap = cv2.VideoCapture(0)

while True:
    # Ler o quadro atual da webcam
    ret, frame = cap.read()

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces na imagem
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Desenhar um retângulo ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Mostrar o quadro com as faces detectadas
    cv2.imshow('Facial Recognition', frame)

    # Parar o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
