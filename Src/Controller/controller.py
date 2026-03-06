import pygame

from Src.Window.window import Snake_Window
from Src.Snake.snake import Snake


class Controller:
    def __init__(self):
        self.window = Snake_Window()
        self.snakes = [Snake()]
        state = "play" #menu, scoreboard...
        self.running = True
        self.two_players = False

        
    def test(self):
        snake_size = 8
        self.snakes[0].create_test_snake(snake_size)

    def uptdate_event_queue(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.quit()
                self.running = False  
            elif event.type == pygame.VIDEORESIZE:
                self.window.resize(event)

            #game logic
            elif event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                #print("pressed keys are", pressed_keys[pygame.K_w])
                
                if pressed_keys[pygame.K_d]:
                    self.snakes[0].change_direction('R')
                elif pressed_keys[pygame.K_a]:
                    self.snakes[0].change_direction('L')
                elif pressed_keys[pygame.K_w]:
                    self.snakes[0].change_direction('U')
                elif pressed_keys[pygame.K_s]:
                    self.snakes[0].change_direction('D')

                #handles two player
                if (self.two_players):
                    if pressed_keys[pygame.K_l]:
                        self.snakes[1].change_direction('R')
                    elif pressed_keys[pygame.K_j]:
                        self.snakes[1].change_direction('L')
                    elif pressed_keys[pygame.K_i]:
                        self.snakes[1].change_direction('U')
                    elif pressed_keys[pygame.K_k]:
                        self.snakes[1].change_direction('D')
    
    def move_snakes(self):
        self.snakes[0].move()
    
    def draw_snakes(self):
        self.window.draw_snake(self.snakes[0])

    def flip_window(self):
        self.window.flip_window()