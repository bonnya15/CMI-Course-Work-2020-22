# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:54:56 2021

@author: shiuli Subhra Ghosh
"""
m = 5
n = 6
chess_board = [[-1 for i in range(n)] for j in range(m)]

def print_board(m,n):
    for i in range(m):
        for j in range(n):
            print(chess_board[i][j], end = " ")
        print("\n")
        
        

        
def get_possibilities(x,y,m,n):
    pos_x = [2, 1, -1, -2, -2, -1, 1, 2]
    pos_y = [1, 2, 2, 1, -1, -2, -2, -1]
    possibilities = []
    for i in range(8):
        if (x + pos_x[i] >= 0 and x + pos_x[i] < m and y + pos_y[i] >= 0 and y + pos_y[i] < n and chess_board[x+pos_x[i]][y+pos_y[i]] == -1) :
            possibilities.append([x + pos_x[i] , y + pos_y[i]] )
            
    return(possibilities)       
            
 
            
def solve(i,j,m,n):
    count = 2
    x = i-1
    y = j-1
    chess_board[i-1][j-1] = 1
    for k in range(m*n - 1):
        pos = get_possibilities(x, y, m, n)
        minimum = pos[0]
        for p in pos:
            if len(get_possibilities(p[0], p[1],m,n)) <= len(get_possibilities(minimum[0], minimum[1],m,n)):
                minimum = p
        x = minimum[0]
        y = minimum[1]
        chess_board[x][y] = count
        count += 1
    
    
    
solve(1,1,m,n)   

#y = get_possibilities(0, 0, m, n) 
#minimum = y[0]    
#len(y)    
    
