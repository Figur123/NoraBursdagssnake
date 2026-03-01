import numpy as np
class Snake:
    def __init__(self):
        self.updateQueue = ['R']
        self.snakePossitions = np.array([[0,0]])
        self.currentDir = 'L'
        self.speed = 1
        self.size = 1

    def grow(self):
        pass

    def move(self):
        for i in range(len(self.updateQueue)):
            segment_update = self.updateQueue[i]
            direction = np.array([0,0])
            if (segment_update == 'R'):
                direction[0] = self.speed
            elif (segment_update == 'L'):
                direction[0] = -self.speed
            elif (segment_update == 'U'):
                direction[1] = self.speed
            elif (segment_update == 'D'):
                direction[1] = -self.speed
            else:
                print("something went horribly wrong segment dont have direction")
        
    
