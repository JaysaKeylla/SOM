# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:28:05 2018

@author: Jaysa
"""

import numpy as np
import cv2
import cv2.aruco as aruco
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Variaveis da WebCan e do no Canvas

cap = cv2.VideoCapture(0)

img = np.zeros((480,640,3), np.uint8)
img = cv2.flip(img, 1)


while(True):
    # Capturando Frame por Frame
    
    ret, frame = cap.read()
    
    # Inverte a nossa camera Horizontalmente
    
    frame = cv2.flip(frame, 1)
    
    # O tamanho na nossa webcam é 480x640
    # O dicionario usado do AruCO foi o AruCO_Original
    
    aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
    parameters =  aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    print(ids)
    print(corners)
    frame = aruco.drawDetectedMarkers(frame, corners)
    
    # Vai desenhar quando o Detectar um AruCO marker, se for detectado um Ruido no Ids, não será printado nada
    
    if(np.all(ids != 0)):
      if(len(corners)>0):
        x = corners[0][0][0][0]
        y = corners[0][0][0][1]
        cv2.circle(img,(x,y),20,(255,255,255),-1)
    
        
    # Mostrar a Janela da WebCam e nosso Canvas    
    cv2.imshow('WebCam',frame)
    cv2.imshow('Canvas',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      
      # Pressione 'q' para sair
      
        break
      
    elif cv2.waitKey(1) & 0xFF == ord('p'):
      
      # Pressione 'p' para salvar a imagem
      
      cv2.imwrite('Imagem.jpg',img)
      print("Imagem Salva")
      
    elif cv2.waitKey(1) & 0xFF == ord('e'):
      
      # Pressione 'e' para apagar a imagem criada
      print("Imagem Limpada")
      img = np.zeros((480,640,3), np.uint8)
      img = cv2.flip(img, 1)

# Quando tudo estiver Terminado, é deletado as Janelas
      
cap.release()
cv2.destroyAllWindows()
