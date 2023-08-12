# This is a sample Python script.
from game.speech import speech
from game.scenario import scenario
from inteligence.reinforcementLearningSnake import reiforcementLearning
import speech_recognition as sr

import pygame
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gameMode = int(input("1 - Free Mode\n2 - Not Learning Colision\n3 - Learning Colision\nType Game Mode:\n"))
    teste = scenario(gameMode)
    teste.game()
    #teste = speech();
    #teste.listener()
    #ar = reiforcementLearning(4, 4, 10, -100, 0.2)
    #ar.startLearning(2,2,4,4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
