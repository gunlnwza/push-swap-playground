import pygame as pg
import colorsys

from Logic import Logic
from Controller import Controller
from setting import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def hsv_to_rgb(hue, saturation=1.0, brightness=1.0):
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, brightness)  # Convert HSV to RGB
    return int(r * 255), int(g * 255), int(b * 255) 

class Renderer:
    def __init__(self, logic: Logic, controller: Controller):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

        self.logic = logic
        self.controller = controller

        self._stack_width = SCREEN_WIDTH / 2
        self._value_height = SCREEN_HEIGHT / self.logic.n

    def _draw_stack(self, x, stack):
        stack_rect = (x, 0, self._stack_width, SCREEN_HEIGHT)
        pg.draw.rect(self.screen, (0, 0, 0), stack_rect)

        y = 0
        for value in stack:
            color = hsv_to_rgb(value / self.logic.max_value, 0.7, 0.7)
            width = (value / self.logic.max_value) * self._stack_width
            pg.draw.rect(self.screen, color, (x, y, width, self._value_height))
            y += self._value_height

        pg.display.update(stack_rect)

    def main_loop(self):
        while True:
            self.clock.tick(FPS)
            self.controller.handle_events()
            self._draw_stack(0, self.logic.stack_a)
            self._draw_stack(SCREEN_WIDTH / 2, self.logic.stack_b)
