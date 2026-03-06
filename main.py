import pygame
from Src.Window.window import Snake_Window
from Src.Snake.snake import Snake
from Src.Controller.controller import Controller




pygame.init()

controller = Controller()#creates windows snakes and gets controller input
clock = pygame.time.Clock()

controller.test()#make the teststuff

#window.uptdate_event_queue()
#window.draw()

while(controller.running):
    controller.move_snakes()
    controller.draw_snakes()
    controller.flip_window()
    controller.uptdate_event_queue()
    clock.tick(60)
    
