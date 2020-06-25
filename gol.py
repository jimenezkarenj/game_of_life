import numpy as np
import time
import pygame

pygame.init()

# Ancho y alto de la pantalla
width, height = 800, 800

#Creacion de la pantalla
screen = pygame.display.set_mode((height, width))

#Color del fondo
bg = 255, 255, 255
screen.fill(bg)

#Celdas y tamaño
nxC, nyC = 50, 50
dimCW = width / nxC
dimCH = height / nyC

#Estado de las celdas vivas = 1 muerta = 0
gameState = np.zeros((nxC, nyC))

#Automata palo
gameState[21, 27] = 1
gameState[21, 28] = 1
gameState[21, 29] = 1

#Automata mobil 1
gameState[21, 11] = 1
gameState[22, 12] = 1
gameState[22, 13] = 1
gameState[21, 13] = 1
gameState[20, 13] = 1

#Automata mobil 2
gameState[31, 5] = 1
gameState[32, 6] = 1
gameState[32, 7] = 1
gameState[31, 7] = 1
gameState[30, 7] = 1

#otro automata
gameState[40, 8] = 1
gameState[41, 7] = 1
gameState[42, 7] = 1
gameState[42, 6] = 1
gameState[43, 7] = 1
gameState[44, 8] = 1

#otro automata 2
gameState[30, 10] = 1
gameState[31, 9] = 1
gameState[32, 9] = 1
gameState[32, 8] = 1
gameState[33, 9] = 1
gameState[34, 10] = 1

#otro automata 2
gameState[20, 8] = 1
gameState[21, 7] = 1
gameState[22, 7] = 1
gameState[22, 6] = 1
gameState[23, 7] = 1
gameState[24, 8] = 1


#otro automata 2
gameState[10, 10] = 1
gameState[11, 9] = 1
gameState[12, 9] = 1
gameState[12, 8] = 1
gameState[13, 9] = 1
gameState[14, 10] = 1

#Control de la ejecucion del juego
pauseExect = False
#Bucle de ejecución
while True:
    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    ev = pygame.event.get()

    for event in ev:
        #Detectamos si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        mouseClick = pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]
    for y in range(0, nxC):

        if not pauseExect:

            for x in range(0, nyC):
                #Calculamos el # de nuestro vecinos cercanos
                n_neigh =   gameState[(x - 1) %nxC, (y - 1) %nyC] + \
                            gameState[(x)     %nxC, (y - 1) %nyC] + \
                            gameState[(x + 1) %nxC, (y - 1) %nyC] + \
                            gameState[(x - 1) %nxC, (y)     %nyC] + \
                            gameState[(x + 1) %nxC, (y)     %nyC] + \
                            gameState[(x - 1) %nxC, (y + 1) %nyC] + \
                            gameState[(x)     %nxC, (y + 1) %nyC] + \
                            gameState[(x + 1) %nxC, (y + 1) %nyC]
                # Rule # 1 : Una célula muerta con exactamente 3 vecinas vivas, "revive"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                
                # Rule # 2 : Una célula viva con menos de 2 o más de 3 vecinas vivas, "muere"
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
                        
                #Creamos el poligono de cada celda a dibujar
                poly = [((x)   * dimCW, y     * dimCH),
                        ((x+1) * dimCW, y     * dimCW),
                        ((x+1) * dimCW, (y+1) * dimCW),
                        ((x)   * dimCW, (y+1) * dimCH)]
                
                #Dibujamos a cada par x e y
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (25, 25, 25), poly, 0)

    #Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    
    #Actualizamos la pantalla
    pygame.display.flip()