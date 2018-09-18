from Assemblies.game import GameField
import numpy as np
import time

import matplotlib.pyplot as plt

class MyGameField(GameField):
    
    # https://spyhce.com/blog/understanding-new-and-init
    # https://docs.python.org/2/tutorial/classes.html
    # https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
    # https://cython.readthedocs.io/en/latest/src/userguide/special_methods.html
    
    def __init__ (self, size, b, perc=21, seed=-1):
        rnd = np.random
        if seed != -1: 
            rnd.seed = seed
        else:
            rnd.seed = time.time()
        
        self._L = L
        self._b = b
        
        self.field = np.array(rnd.rand(size, size) > 0.01 * perc, dtype=int)

    
    def show(self, point_size=10, scale=10):
        plt.clf()
        plt.figure(figsize = (scale*1, scale*0.666))
        point_size = scale / (len(self.L)**2) * 10000

        y, x = (1 - self._field).nonzero()
        plt.scatter(x + y*np.sin(np.pi/6), y * np.sin(np.pi/3), s=point_size, marker='h')
        
        y, x = self._field.nonzero()
        plt.scatter(x + y*np.sin(np.pi/6), y * np.sin(np.pi/3), s=point_size, marker='h', c='r')
        plt.show()

