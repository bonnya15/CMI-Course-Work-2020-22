# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 23:01:32 2021

@author: shiuli Subhra Ghosh
"""

def knightstour(m,n,i,j):
    soln = [] #Empty list is taken for linear solution 
    (a,b) = (i-1 , j-1) 
    board = [[-1 for z in range(n)] for k in range(m)] #Chess Board initialization 
    board[a][b] = 0 
    soln.append((a+1 , b+1))
    pos = 1
    
    if solution(m,n,board,a,b,pos,soln):
        return(print(soln))
        
    else:
        return([]) #when there is no solution 

# To check if the next move is in side the board or not    
def issafe(m,n,x,y,board):
    if(x >= 0 and y >= 0 and x < m and y < n and board[x][y] == -1):
        return(True)
    return(False)
  
# To get all the possibilities for the next move        
def get_possibilities(x,y,m,n,board):
    mx = [2, 1, -1, -2, -2, -1, 1, 2]
    my = [1, 2, 2, 1, -1, -2, -2, -1]
    possibilities = []
    for i in range(8):
        if issafe(m,n,(x + mx[i]),(y + my[i]),board):
            possibilities.append([x + mx[i] , y + my[i]] )
            
    return(possibilities)   
    
 
# Main Solution function        
def solution(m,n,board,cx,cy,pos,soln):
    
    if(pos == m*n):
        return(True)
    
    possi = get_possibilities(cx, cy, m, n, board)
    len_possi = []
    # Implementing Warnsdorff Solution in backtracking 
    for p in possi:
        len_possi.append(len(get_possibilities(p[0], p[1],m,n,board)))
    combined = list(zip(possi,len_possi))
    sor = sorted(combined, key = lambda x : x[1])  #Stable Sort 
    for i in range(len(sor)):
        x = sor[i][0][0]
        y = sor[i][0][1]
        if issafe(m,n,x,y,board):
            board[x][y] = pos
            soln.append((x+1,y+1))
            if (solution(m,n,board,x,y,pos+1,soln)):
                return(True)
            
            board[x][y] = -1
            soln.remove((x+1,y+1))
            
    return(False)