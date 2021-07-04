from math import sqrt
from itertools import chain

class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.unpacked = list(chain.from_iterable(data))
        
    def is_valid(self):
        n = len(self.data)
        totalElems = len(self.unpacked)
        
        isNSquare = sqrt(totalElems) == n
        
        if isNSquare and n > 0:

            #function for checking cells if they contain exactly the numbers 1, 2 ... n+1
            checkIsValidLists = lambda x: all( [set(i) == set(range(1, n + 1)) for i in x] )
            
            rootN = int(sqrt(n))
            
            #extract rows and cols for given suduku aka. list of lists.
            rows = self.data 
            cols = [[i[j] for i in self.data] for j in range(n)]
            
            #ugly piece of code here - could not think of anything prettier at the time of writing...
            #this extracts numbers in n rootN*rootN grids and puts them in lists.
            cubes = [[list( chain.from_iterable([self.data[i + s][k * rootN:(k+1) * rootN] for i in range(rootN)]) ) for k in range(rootN)] for s in range(rootN)][0]
            
            #checks if cells only contain integers
            isOnlyIntCells = all([type(i) is int for i in self.unpacked])
            
            return isOnlyIntCells and checkIsValidLists(rows) and checkIsValidLists(cols) and checkIsValidLists(cubes)
        
        else:
            return False