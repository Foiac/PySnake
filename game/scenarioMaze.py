import logging

import pygame
from random import randint

class scenarioMaze:

    def __init__(self):
        self.passos = None
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.speed = 10

        self.player_pos = pygame.Vector2(40,40)

    def game(self):
        self.clock = pygame.time.Clock()
        while self.running:
            self.clock.tick(self.speed)
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                elif self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_i: #and self.direction != 2:
                        self.speed = 1200
                    if self.event.key == pygame.K_o: #and self.direction != 2:
                        self.speed = 120
                    if self.event.key == pygame.K_p: #and self.direction != 2:
                        self.speed = 10

                    if self.event.key == pygame.K_w: #and self.direction != 2:
                        self.direction = 0
                    elif self.event.key == pygame.K_d: #and self.direction != 3:
                        self.direction = 1
                    elif self.event.key == pygame.K_s: #and self.direction != 0:
                        self.direction = 2
                    elif self.event.key == pygame.K_a: #and self.direction != 1:
                        self.direction = 3

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")
            self.generateLevel()
            pygame.draw.rect(self.screen, "green", pygame.Rect(self.player_pos.x, self.player_pos.y, 40, 40))
            pygame.draw.rect(self.screen, "blue", pygame.Rect(1040, 640, 40, 40))
            ### Aprendizagem por reforço aqui


            #################################


            #print(round(self.player_pos.x,0), round(self.player_pos.y,0))

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()

    def generateLevel(self):
        #pygame.draw.rect(self.screen, "white", pygame.Rect(1 * 40, 1 * 40, 40, 40))

        with open("levels/level1.txt", "r") as arquivo:
            arquivo = arquivo.readlines()

        levelMatriz = []
        for row in range(len(arquivo)):
            rows = []
            for column in arquivo[row]:
                rows.append(column)
            levelMatriz.append(rows)

        for i in range(len(levelMatriz) - 1):
            for j in range(len(levelMatriz[0])):
                print(i, j)
                if(levelMatriz[i][j] == 'X'):
                    pygame.draw.rect(self.screen, "white", pygame.Rect(j * 40, i * 40, 40, 40))