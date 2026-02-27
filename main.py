import pygame
from Src.Window.window import Snake_Window


pygame.init()


window = Snake_Window()
while(window.running):
    window.uptdate_event_queue()
    window.draw()


pygame.quit()