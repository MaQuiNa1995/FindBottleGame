#!/bin/python
import pygame,sys
from pygame.locals import *
from random import randint 

pygame.init()

Ventana = pygame.display.set_mode([400, 400])

pygame.display.set_caption('Catch The Potion Alpha 0.2')

Imagen = pygame.image.load('Mat/Adamantite.png')

Poti = pygame.image.load('Mat/Poti_mana.png')

posX = 0
posY = 400
velocidad = 10

posic = posX
posici = posY

posiX = randint(30,270)
Posici_poti = (80,370)


purpura=(165,25,145)
negro=(0,0,0)
verde=(0,255,0)

fondo_img = pygame.image.load('Mat/Bloque.png')



while True:
	Ventana.fill(negro)
        Ventana.blit(fondo_img,(0,-5))
	pygame.draw.rect(Ventana,(verde),(80,370,102,371))
	pygame.draw.rect(Ventana,(purpura),(340,0,400,400))
        pygame.draw.rect(Ventana,(verde),(0,90,60,90))
       	Ventana.blit(Imagen,(posX,posY))
	Ventana.blit(Poti,(Posici_poti))
        
	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
		sys.exit()

	    elif posX > 340:
        	posX=340

            elif posX < 0:
		posX=0

            elif posY < 0:
		posY=0

	    elif posY > 310:
        	posY=310
	
	    elif posX==0 and posY==90:
			print("Has Ganado!!!!!")
	
     	    elif event.type==KEYDOWN:
           	if event.key==K_LEFT:
           	  	posX=posX-velocidad
          	elif event.key==K_RIGHT:
         		posX=posX+velocidad
		elif event.key==K_UP:
			if posX > 330:
				posY=posY-velocidad
		elif event.key==K_DOWN:
			if posX > 330:
	    			posY=posY+velocidad
						
	    elif event.type==KEYUP:
	   	if event.key==K_LEFT:
			print(posX, posY)
		elif event.key==K_RIGHT:
			print(posX, posY)
	
	    
	pygame.display.update ()
