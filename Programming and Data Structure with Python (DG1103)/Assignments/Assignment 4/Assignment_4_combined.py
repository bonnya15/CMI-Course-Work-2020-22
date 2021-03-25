# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 02:09:07 2021

@author: shiuli Subhra Ghosh
"""
def knightstour(m,n,i,j):
    soln = []
    (a,b) = (i-1 , j-1) 
    board = [[-1 for z in range(n)] for k in range(m)]
    board[a][b] = 0 
    soln.append((a+1 , b+1))
    pos = 1
    
    if solution(m,n,board,a,b,pos,soln):
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
  
        
def get_possibilities(x,y,m,n,board):
    mx = [2, 1, -1, -2, -2, -1, 1, 2]
    my = [1, 2, 2, 1, -1, -2, -2, -1]
    possibilities = []
    for i in range(8):
        if issafe(m,n,(x + mx[i]),(y + my[i]),board):
            possibilities.append([x + mx[i] , y + my[i]] )
            
    return(possibilities)   
    
 
        
def solution(m,n,board,cx,cy,pos,soln):
    
    if(pos == m*n):
        return(True)
    
    possi = get_possibilities(cx, cy, m, n, board)
    len_possi = []
    for p in possi:
        len_possi.append(len(get_possibilities(p[0], p[1],m,n,board)))
    combined = list(zip(possi,len_possi))
    sor = sorted(combined, key = lambda x : x[1])
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