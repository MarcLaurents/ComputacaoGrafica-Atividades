import cv2

# Carregar o arquivo de treinamento do OpenCV
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Carregar a imagem
image = cv2.imread('./image/Cate.jpg')

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar faces na imagem
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Desenhar um retângulo ao redor das faces detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostrar a imagem com as faces detectadas
cv2.imshow('Facial Recognition', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
