import pygame as pg
import random

from Logic import Logic
from Renderer import Renderer
from Controller import Controller

def main():
    values = [i for i in range(1, 20)]
    random.shuffle(values)
    
    logic = Logic(values)
    controller = Controller(logic)
    renderer = Renderer(logic, controller)
    renderer.main_loop()

if __name__ == "__main__":
    main()
