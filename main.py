# This is a sample Python script.
from game.speech import speech
from game.scenarioSnake import scenarioSnake
from game.scenarioMaze import scenarioMaze
from inteligence.reinforcementLearningSnake import reiforcementLearning
import speech_recognition as sr

import pygame
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #teste = scenarioMaze()
    #teste.game()
    gameMode = int(input("1 - Free Mode\n2 - Not Learning Colision\n3 - Learning Colision\nType Game Mode:\n"))
    teste = scenarioSnake(gameMode)
    teste.game()
    #teste = speech();
    #teste.listener()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
