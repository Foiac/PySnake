from random import randint, random
import pygame

class reiforcementLearning:

    def __init__(self, states, actions, alpha, teta, e, gameMode):
        ## linhas são os estados, onde:
        ## 0 - maçã no primeiro quadrante
        ## 1 - maçã no segundo quadrante
        ## 2 - maçã no terceiro quadrante
        ## 3 - maçã no quarto quadrante
        ## 4 - obstáculo acima
        ## 5 - obstáculo a direita
        ## 6 - obstáculo a esquerda

        self.gameMode = gameMode
        self.stateF = None
        self.matrizQ=[]
        for i in range(states):
            self.row=[]
            for j in range(actions):
                self.row.append(0)
            self.matrizQ.append(self.row)
        #print("Tamanho matrizQ: " + str(len(self.matrizQ)))
        b = 1
        r = -9
        m = -3
        rr = -9
        self.matrizR = [[b, m, r, r], [m, r, r, b], [r, r, b, m], [r, b, m, r], [rr, b, rr, b], [b, rr, b, rr], [rr, b, rr, b], [b, rr, b, rr]]
        if self.gameMode == 2:
            self.matrizR = [[b, m, r, r], [m, r, r, b], [r, r, b, m], [r, b, m, r]] #[rr, b, rr, b], [b, rr, b, rr], [rr, b, rr, b]]
        elif self.gameMode == 3:
            self.matrizR = [[b, m, r, r], [m, r, r, b], [r, r, b, m], [r, b, m, r], [rr, b, rr, b], [b, rr, b, rr], [rr, b, rr, b], [b, rr, b, rr]]

        self.ePol = e
        self.alpha = alpha
        self.teta = teta
        self.stateI = -1
        self.action = -1

    def startLearning(self, snake_x, snake_y, apple_x, apple_y, snake, direction):
        self.stateI = self.getState(snake_x, snake_y, apple_x, apple_y, snake, direction)

        if random() < self.ePol:
            self.action = randint(0,3)
        else:
            self.action = self.matrizQ[self.stateI].index(max(self.matrizQ[self.stateI]))
            #print("action = " + str(self.action))
        return self.action

    def reward(self, snake_x, snake_y, apple_x, apple_y, direction, snake):
        if (direction == "UP"): self.action = 0
        elif (direction == "RIGHT"): self.action = 1
        elif (direction == "DOWN"): self.action = 2
        elif (direction == "LEFT"): self.action = 3

        self.stateF = self.getState(snake_x, snake_y, apple_x, apple_y, snake, direction)
        #print("Estado atual: " + str(self.stateF) + " Direção " + str(direction))
        self.matrizQ[self.stateI][self.action] = self.matrizQ[self.stateI][self.action] + self.alpha*(self.matrizR[self.stateI][self.action] + self.teta * max(self.matrizQ[self.stateF]) - self.matrizQ[self.stateI][self.action])
        # print(self.matrizQ)
        # print(self.matrizQ[self.stateI][self.action])

        for j in range(len(self.matrizQ)):
            for i in range(len(self.matrizQ[0])):
                #print("i = " + str(i) + " j = " + str(j))
                print(round(self.matrizQ[j][i], 1), end = " ")
            print()
        print()

    def getState(self, snake_x, snake_y, apple_x, apple_y, snake, direction):
        cabeca = (snake[0][0], snake[0][1])
        #print("snake: ", snake[2:], " cabeça: ", cabeca)
        if self.gameMode == 3 or self.gameMode == 1:
            for corpo in snake[2:]:
                if direction == "UP":
                    if(cabeca[1] == corpo[1] + 40):
                        return 4

                elif direction == "RIGHT":
                    if (cabeca[0] + 40 == corpo[0]):
                        return 5

                elif direction == "DOWN":
                    if (cabeca[1] == corpo[1] - 40):
                        return 6

                elif direction == "LEFT":
                    if(cabeca[0] == corpo[0] + 40):
                        return 7

        if((snake_x <= apple_x) and (snake_y > apple_y)):
            return 0 ## primeiro quadrante
        elif ((snake_x > apple_x) and (snake_y >= apple_y)):
            return 1 ## segundo quadrante
        elif ((snake_x >= apple_x) and (snake_y < apple_y)):
            return 2 ## terceiro quadrante
        elif ((snake_x < apple_x) and (snake_y <= apple_y)):
            return 3 ## quarto quadrante
        else:
            return 0

