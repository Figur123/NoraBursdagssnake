import pygame

class Snake_Window:
    
    
    def __init__(self):
        #window stuff
        self.width, self.height = 400, 400

        self.flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        self.window = pygame.display.set_mode((self.width, self.height),self.flags, vsync=1)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("the real snakes")
        
        self.running = True

    def uptdate_event_queue(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.w, event.h
    
    def draw(self):
        self.window.fill((0,0,0))
        pygame.display.flip()
        self.clock.tick(60)
            
        
        
