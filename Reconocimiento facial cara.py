import cv2 # Abrir python 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Importar la libreria previamente descargada del reconocimiento facial

cap = cv2.VideoCapture(1) # Abrir la webcam del sistema, cuando añadamos la webcam cambiar el numero 0 del parentesis por 1

while True: #   Bucle infinito 
    _,  img = cap.read() # Leer cada uno de los fotogramas 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convertir la imagen a escala de grises
    faces = face_cascade.detectMultiScale(gray, 1.05, 3) # Detectar todas las caras en la imagen, los parametros 1.1 y 4 se iran modificando en función de la imagen que pongamos para que funcones mejor
    for (x, y, w, h) in faces: # Dibujar un rectángulo alrededor de cada cara detectada
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img) # Mostrar la cara con todas los modificaciones anteriores
    k = cv2.waitKey(30) # Comando de openCV para que cuando pulsemos la tecla que eligamos, en este caso escape, se cierre el bucle
    if k == 27: # 27 es el código de la tecla escape
        break
cap.release() # Cerrar la webcam
cv2.destroyAllWindows() # Cerrar todas las ventanas de OpenCV 