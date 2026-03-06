import pygame
from Src.Snake.snake import Snake

class Snake_Window:

    def __init__(self):
        #window stuff
        self.width, self.height = 400, 400

        self.flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        self.window = pygame.display.set_mode((self.width, self.height),self.flags, vsync=1)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("the real snakes")
        

    def quit(self):
        pygame.quit()

    def resize(self, event):
        self.width, self.height = event.w, event.h
        #self.window = pygame.display.set_mode((self.width, self.height), self.flags, vsync=1)
    
    def draw_snake(self, snake:Snake):
        width = snake.block_size-2
        height = width
        for pos in snake.snakePossitions:
            rect = pygame.Rect(int(pos[0]), int(pos[1]), width, height)
            pygame.draw.rect(self.window, color="red", rect = rect)

    def flip_window(self):
        pygame.display.flip()
        self.window.fill(color='black')

            
        
        
