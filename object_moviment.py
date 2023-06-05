import cv2

video = cv2.VideoCapture('FroggerHighway.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

# Definir o tamanho fixo da janela
window_width = 800
window_height = 600

# Criar a janela com o tamanho fixo
cv2.namedWindow('Moving Object Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Moving Object Detection', window_width, window_height)

while True:
  ret, frame = video.read()
  if not ret:
    break
  
  # Aplicar a subração d oplano de fundo
  fgmask = fgbg.apply(frame)
  
  # Aplicar um limiar para binarizar o resultado
  _, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
  
  # Encontrar contornos dos objetos em movimento
  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:
      # Obter as coordenadas do retangulo envolvente
      x, y, w, h = cv2.boundingRect(contour)
      
      # Desenhar o retangulo envolvente nos objetos em movimento
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
  
  # Redimensionar o quadro para o tamanho da janela
  frame = cv2.resize(frame, (window_width, window_height))
  
  # Mostrar o resultado
  cv2.imshow('Moving Object Detection', frame)
  
  # Verificar se a tecla 'q' foi pressionada para sair
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Liberar os recursos
video.release()
cv2.destroyAllWindows()
  