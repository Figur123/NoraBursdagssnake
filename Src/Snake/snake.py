import numpy as np
class Snake:
    def __init__(self):
        self.updateQueue = ['R', 'R']#first one is to store user input as the snake should not change before gridalignment
        self.snakePossitions = np.array([[0,0]])

        self.speed = 1
        self.block_size = 10
        self.last_direction_change = 0

    def __str__(self):
        return str(self.snakePossitions)

    def create_test_snake(self, size):
        self.snakePossitions[0] = [self.block_size * size, 0]

        for i in range(size):
            self.grow()
            self.updateQueue.append('R')

    def grow(self):
        new_blob_pos = np.copy(self.snakePossitions[-1])
        new_blob_pos[0] += -self.block_size
        self.snakePossitions = np.vstack((self.snakePossitions, new_blob_pos))

    def change_direction(self, new_dir):
        curr_dir = self.updateQueue[1]

        if (curr_dir == 'R' or curr_dir == 'L' ):
            if (new_dir == 'U' or new_dir == 'D'):
                self.updateQueue[0] = new_dir
        
        elif (curr_dir == 'U' or curr_dir == 'D' ):
            if (new_dir == 'R' or new_dir == 'L'):
                self.updateQueue[0] = new_dir
        


        
        #print(dir)


    def move(self):
        if self.last_direction_change >= self.block_size:
            #roll snake 
            self.updateQueue = np.roll(self.updateQueue,1)
            self.updateQueue[0] = self.updateQueue[1]
            
            #reset gridaligning
            self.last_direction_change = 0

        for i in range(len(self.snakePossitions)):
            #figure the direction and speed
            segment_update = self.updateQueue[i + 1]#first index is stored direction
            direction = np.array([0,0])
            if (segment_update == 'R'):
                direction[0] = self.speed
            elif (segment_update == 'L'):
                direction[0] = -self.speed
            elif (segment_update == 'U'):
                direction[1] = -self.speed
            elif (segment_update == 'D'):
                direction[1] = self.speed
            else:
                #print("something went horribly wrong segment dont have direction")
                pass
            #apply
            #print("segment update = ", segment_update)
            self.snakePossitions[i] = np.add(self.snakePossitions[i], direction)
        self.last_direction_change += self.speed
        
            
        
    
