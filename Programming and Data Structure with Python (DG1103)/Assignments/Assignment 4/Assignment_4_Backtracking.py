# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 01:16:01 2021

@author: shiuli Subhra Ghosh
"""

def knightstour(m,n,i,j):
    (a,b) = (i-1 , j-1) 
    board = [[-1 for z in range(n)] for k in range(m)]
    board[a][b] = 0 
    soln.append((a+1 , b+1))
    mx = [2, 1, -1, -2, -2, -1, 1, 2]
    my = [1, 2, 2, 1, -1, -2, -2, -1]
    pos = 1
    
    if solution(m,n,board,a,b,mx,my,pos):
        printboard(m,n,board)
        print(soln)
        
    else:
        return('Solution does not exist')

    
def issafe(m,n,x,y,board):
    if(x >= 0 and y >= 0 and x < m and y < n and board[x][y] == -1):
        return(True)
    return(False)

def printboard(m,n,board):
    for i in range(m):
        for j in range(n):
            print(board[i][j], end = ' ')
        print()
        
soln = []        
def solution(m,n,board,cx,cy,mx,my,pos):
    
    if(pos == m*n):
        return(True)
    for t in range(8):
        x = cx + mx[t]
        y = cy + my[t]
        if (issafe(m,n,x,y,board)):
            board[x][y] = pos
            soln.append((x+1,y+1))
            if (solution(m,n,board,x,y,mx,my,pos+1)):
                return(True)
            
            board[x][y] = -1
            soln.remove((x+1,y+1))
            
    return(False)