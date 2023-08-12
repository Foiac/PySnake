import logging

import pygame
from random import randint
from inteligence.reinforcementLearningSnake import reiforcementLearning

class scenarioSnake:

    def __init__(self, gameMode):
        self.passos = None
        pygame.init()
        self.gameMode = gameMode
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.speed = 10

        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

        self.snake = [(self.player_pos.x, self.player_pos.y)]

        self.apple_pos = pygame.Vector2(0,0)
        self.appleFlag = True
        self.direction = -1
        self.directionAtual = "STOP"
        self.tamanho = 2
        self.matrizResultado=[]

    def game(self):
        self.clock = pygame.time.Clock()

        ar = reiforcementLearning(8, 4, 0.7, 0.3, 0.01, self.gameMode)
        if self.gameMode == 2:
            ar = reiforcementLearning(4, 4, 0.7, 0.3, 0.01, self.gameMode)

        self.passos = 0
        self.appleNumber = 1

        while self.running:
            if self.gameMode != 1:
                self.clock.tick(self.speed)
            else:
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

            if(self.appleFlag):
                self.apple_pos.x = randint(0, 1240/40)*40
                self.apple_pos.y = randint(0, 680/40)*40
                self.appleFlag = False

            pygame.draw.rect(self.screen, "red", pygame.Rect(self.apple_pos.x, self.apple_pos.y, 40, 40))
            for pos in self.snake:
                pygame.draw.rect(self.screen, "white", pygame.Rect(pos[0], pos[1], 40, 40))

            ### Aprendizagem por reforço aqui

            if self.gameMode != 1:
                self.direction = ar.startLearning(self.player_pos.x, self.player_pos.y, self.apple_pos.x, self.apple_pos.y, self.snake, self.directionAtual)

            #################################

            if self.direction == 0 and self.directionAtual != "DOWN":
                self.snake[0] = (self.snake[0][0], self.snake[0][1] - 40)
                self.player_pos.y -= 40
                self.directionAtual = "UP"
            elif self.direction == 0 and self.directionAtual == "DOWN":
                self.snake[0] = (self.snake[0][0], self.snake[0][1] + 40)
                self.player_pos.y += 40
                self.directionAtual = "DOWN"

            elif self.direction == 1 and self.directionAtual != "LEFT":
                self.snake[0] = (self.snake[0][0] + 40, self.snake[0][1])
                self.player_pos.x += 40
                self.directionAtual = "RIGHT"
            elif self.direction == 1 and self.directionAtual == "LEFT":
                self.snake[0] = (self.snake[0][0] - 40, self.snake[0][1])
                self.player_pos.x -= 40
                self.directionAtual = "LEFT"

            elif self.direction == 2 and self.directionAtual != "UP":
                self.snake[0] = (self.snake[0][0], self.snake[0][1] + 40)
                self.player_pos.y += 40
                self.directionAtual = "DOWN"
            elif self.direction == 2 and self.directionAtual == "UP":
                self.snake[0] = (self.snake[0][0], self.snake[0][1] - 40)
                self.player_pos.y -= 40
                self.directionAtual = "UP"

            elif self.direction == 3 and self.directionAtual != "RIGHT":
                self.snake[0] = (self.snake[0][0] - 40, self.snake[0][1])
                self.player_pos.x -= 40
                self.directionAtual = "LEFT"
            elif self.direction == 3 and self.directionAtual == "RIGHT":
                self.snake[0] = (self.snake[0][0] + 40, self.snake[0][1])
                self.player_pos.x += 40
                self.directionAtual = "RIGHT"

            if(self.gameMode != 2):
                if(self.player_pos in self.snake[1:-1]): #reiniciar cobra se bater
                    self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
                    self.snake = [self.player_pos]
                    for pos in self.snake:
                        pygame.draw.rect(self.screen, "white", pygame.Rect(pos[0], pos[1], 40, 40))

            if self.player_pos.x > 1240:
                self.snake[0] = (0, self.snake[0][1])
                self.player_pos.x = 0
            elif self.player_pos.x < 0:
                self.snake[0] = (1240, self.snake[0][1])
                self.player_pos.x = 1240
            elif self.player_pos.y > 680:
                self.snake[0] = (self.snake[0][0], 0)
                self.player_pos.y = 0
            elif self.player_pos.y < 0:
                self.snake[0] = (self.snake[0][0], 680)
                self.player_pos.y = 680

            # print("snake antes", self.snake)
            # for i in range(len(self.snake) -1, 0, -1):
            #     print(i)
            #     print(self.snake[i])
            #     self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])
            # print("snake depois", self.snake)

            self.passos+=1
            if self.player_pos == self.apple_pos:
                self.appleFlag = True
                self.snake.append((self.player_pos.x, self.player_pos.y))
                self.matrizResultado.append((self.appleNumber, self.passos))
                self.passos = 0
                self.appleNumber +=1

            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])

            ar.reward(self.player_pos.x, self.player_pos.y , self.apple_pos.x, self.apple_pos.y, self.directionAtual, self.snake)

            #print(round(self.player_pos.x,0), round(self.player_pos.y,0))

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60) / 1000



        pygame.quit()