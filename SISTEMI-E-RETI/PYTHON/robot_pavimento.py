import pygame #installata da noi
import sys #nativa = preinstallata

NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)
pavimento = [[1,1,0,0,0,0],
             [0,0,0,0,1,0],
             [1,0,1,0,0,0],
             [0,0,1,0,1,0],
             [0,0,1,0,0,0]]

NRIGHE = len(pavimento)
NCOLONNE = len(pavimento[0])
DIMENSIONI = (600,600)

def drawgrid():
    dimensionex = DIMENSIONI[0]//COLONNE
    dimensioney = DIMENSIONI[1]//NRIGHE
    dimensione = 50
    for x in range(0, DIMENSIONI[0], dimensionex):
        for y in range(0, DIMENSIONI[1], dimensioney):
            piastrella = pygame.Rect(x,y,dimensione)
            pygame.draw.rect(finestra, BIANCO, piastrella, 1)
    ostacolo = pygame.Rect(50, 100, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

def main():
    pygame.init()
    global finestra
    finestra = pygame.display.set_mode(DIMENSIONI)
    finestra.fill(NERO)
    while True:
        drawgrid()
        #ciclo per gestione eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

if __name__ == "__main__" :
    main()