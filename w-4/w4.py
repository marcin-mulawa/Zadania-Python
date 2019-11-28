import numpy as np


def make(n):

     my_list = np.random.choice([255,0], n*n,p=[0.2,0.8])
     my_list=my_list.reshape(n, n)

     return my_list


def add_blok(i,j,grid):
     blok = np.array([[0, 0, 0, 0],
                         [0, 255, 255, 0],
                         [0, 255, 255, 0]
                         [0, 0, 0, 0]])
     grid[i:i + 4, j:j + 4] = blok

def add_ul(i,j,grid):
     ul = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 0, 255, 255, 0, 0],
                    [0, 255, 0, 0, 255, 0],
                    [0, 0, 255, 0, 0, 255, 0],
                    [0, 0, 0, 0, 0, 0]])
     grid[i:i+6,j:j+5] = ul


def add_bochenek(i,j,grid):
     bochenek = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 0, 255, 255, 0, 0],
                          [0, 255, 0, 0, 255, 0],
                          [0, 0, 255, 0, 255, 0],
                          [0, 0, 0, 255, 0, 0],
                          [0, 0, 0, 0, 0, 0]])
     grid[i:i+6,j:j+6] = bochenek


def add_lodka(i,j,grid):
     lodka = np.array([[0, 0, 0, 0, 0],
                       [0, 255, 255, 0, 0],
                       [0, 255, 0, 255, 0],
                       [0, 0, 255, 0, 0],
                       [0, 0, 0, 0, 0]])
     grid[i:i + 5, j:j + 5] = lodka

def add_swiatla(i,j,grid):
     swiatla = np.array([[0, 0, 0, 0, 0],
                        [0, 0, 255, 0, 0],
                        [0, 0, 255, 0, 0],
                        [0, 0, 255, 0, 0],
                        [0, 0, 0, 0, 0]])
     grid[i:i+5,j:j+5] = swiatla


def add_zaba(i,j,grid):
     zaba= np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 255, 255, 255, 0],
                     [0, 255, 255, 255, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]])
     grid[i:i + 6, j:j + 6] = zaba


def add_latarnia(i,j, grid):
     latarnia = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 255, 255, 0, 0, 0],
                          [0, 255, 0, 0, 0, 0],
                          [0, 0, 0, 0, 255, 0],
                          [0, 0, 0, 255, 255, 0],
                          [0, 0, 0, 0, 0, 0]])
     grid[i:i + 6, j:j + 6] = latarnia


def check_life(i,j,grid):
     n = grid.shape[0]
     total = int((grid[i,(j-1)%n]+ grid[i,(j+1)%n]+
                 grid[(i+1)%n,j]+ grid[(i-1)%n,j]+
                 grid[(i+1)%n,(j+1)%n] + grid[(i-1)%n,(j-1)%n])/255)
     return total


def conway(i,j,grid):

     n = grid.shape[0]
     total = int((grid[i, (j - 1) % n] + grid[i, (j + 1) % n] +
                  grid[(i + 1) % n, j] + grid[(i - 1) % n, j] +
                  grid[(i + 1) % n, (j + 1) % n] + grid[(i - 1) % n, (j - 1) % n]) / 255)

     if total >= 4 or total <= 1:
          grid[i, j] = 0
     if total == 3:
          grid[i, j] = 255
     return grid

def update(grid):
     newgrid = grid.copy()
     for i in range(grid.shape[0]):
          for j in range(grid.shape[0]):
               total = check_life(i,j, newgrid)
               newgrid = conway(i, j, newgrid)

     grid = newgrid
     return grid




#grid = make(15)
#print(grid)
#print('\n\n---------------------------------------------------------------\n\n')
#add_zaba(3,3,grid)
#print(grid)

grid = make(15)
print(grid)
grid = update(grid)
print('\n\n-------------------\n\n')
print(grid)