import pygame as pg
import colorsys
import random
import math

random.seed(0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 10

def hsv_to_rgb(hue, saturation=1.0, brightness=1.0):
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, brightness)  # Convert HSV to RGB
    return int(r * 255), int(g * 255), int(b * 255) 

class Card:
    def __init__(self, value, color, size):
        self.value = value
        self.color = color
        self.width, self.height = size

class Stack:
    def __init__(self, values=None):
        self.cards = []
        self.width = SCREEN_WIDTH / 2
        if values:
            self.x = 0
            max_ = max(values)
            height = SCREEN_HEIGHT / len(values)
            for value in values:
                width = (value / max_) * self.width
                color = hsv_to_rgb(value / max_, 0.7, 0.7)
                self.cards.append(Card(value, color, (width, height)))
        else:
            self.x = self.width

    def put_on(self, screen):
        x, y = self.x, 0
        for card in self.cards:
            pg.draw.rect(screen, card.color, (x, y, card.width, card.height))
            y += card.height

    def push_to(self, other: "Stack"):
        if self.cards:
            card = self.cards.pop(0)
            other.cards.insert(0, card)

    def rotate(self):
        if self.cards:
            card = self.cards.pop(0)
            self.cards.append(card)

    def reverse_rotate(self):
        if self.cards:
            card = self.cards.pop()
            self.cards.insert(0, card)

def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()

    values = [i for i in range(1, 101)]
    random.shuffle(values)
    print(values)

    stack_a = Stack(values)
    stack_b = Stack()

    is_running = True
    while is_running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                break
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    is_running = False
                    break

                elif event.key == pg.K_h:
                    stack_b.push_to(stack_a)
                elif event.key == pg.K_l:
                    stack_a.push_to(stack_b)

                elif event.key == pg.K_q:
                    stack_a.rotate()
                elif event.key == pg.K_a:
                    stack_a.reverse_rotate()

                elif event.key == pg.K_e:
                    stack_b.rotate()
                elif event.key == pg.K_d:
                    stack_b.reverse_rotate()

                elif event.key == pg.K_w:
                    stack_a.rotate()
                    stack_b.rotate()
                elif event.key == pg.K_s:
                    stack_a.reverse_rotate()
                    stack_b.reverse_rotate()

        screen.fill((0, 0, 0))
        stack_a.put_on(screen)
        stack_b.put_on(screen)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()