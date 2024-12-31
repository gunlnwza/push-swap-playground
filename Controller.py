import pygame as pg

from Logic import Logic

class Controller:
    def __init__(self, logic: Logic):
        self.logic = logic

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()

                elif event.key == pg.K_h:
                    self.logic.pa()
                elif event.key == pg.K_l:
                    self.logic.pb()

                elif event.key == pg.K_q:
                    self.logic.ra()
                elif event.key == pg.K_w:
                    self.logic.rr()
                elif event.key == pg.K_e:
                    self.logic.rb()
                
                elif event.key == pg.K_a:
                    self.logic.rra()
                elif event.key == pg.K_s:
                    self.logic.rrr()
                elif event.key == pg.K_d:
                    self.logic.rrb()
