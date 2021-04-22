# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:29:07 2021

@author: shiuli Subhra Ghosh
"""
from collections import defaultdict

f = open(r'tennis.in', 'r')
v = f.readlines()
f.close()

a = [':','-']

#cleaning the set and converting the elements in a list for better readibility 

for j in range(len(v)):
    for k in a:
        v[j] = v[j].replace(k,',')
    v[j] = v[j].split(',')

# n is the number of sets played in a match 
n = []

for i in range(len(v)):
    n.append((len(v[i])-2)//2)


# initialising dictionaries for obtaining different results. 
winner_three_set = defaultdict(int)
winner_five_set = defaultdict(int)
number_of_sets_won = defaultdict(int)
number_of_sets_lost = defaultdict(int)
number_of_games_won = defaultdict(int)
number_of_games_lost = defaultdict(int)

#Main driver loop for obtaining results in pre-initialised dictionaries
for i in range(len(v)):
    p = 0
    q = 0

#This loop is for obtaining the total number of games won and lost by the players    
    for j in range(2,len(v[i]),2):
        number_of_games_won[v[i][0]] += int(v[i][j])
        number_of_games_won[v[i][1]] += int(v[i][j+1])
        number_of_games_lost[v[i][0]] += int(v[i][j+1])
        number_of_games_lost[v[i][1]] += int(v[i][j])

# This is the part where the results are obtained for 1,2,3 and 5     
    if n[i] == 2: 
        winner_three_set[v[i][0]] += 1
        number_of_sets_won[v[i][0]] += 2
        number_of_sets_lost[v[i][1]] += 2
    elif n[i] == 3:
        for j in range(2,len(v[i]),2):
            if int(v[i][j]) - int(v[i][j+1]) < 0:
                 p = 1
                 break
        else:
            q = 1
        winner_three_set[v[i][0]] += p
        winner_five_set[v[i][0]] += q 
        if p == 1:
            number_of_sets_won[v[i][0]] += 2
            number_of_sets_won[v[i][1]] += 1
            number_of_sets_lost[v[i][0]] += 1
            number_of_sets_lost[v[i][1]] += 2
        elif q == 1:
            number_of_sets_won[v[i][0]] += 3
            number_of_sets_lost[v[i][1]] += 3
    else:
        winner_five_set[v[i][0]] +=  1
        if n[i] == 4:
            number_of_sets_won[v[i][0]] += 3
            number_of_sets_won[v[i][1]] += 1
            number_of_sets_lost[v[i][0]] += 1
            number_of_sets_lost[v[i][1]] += 3
        
        elif n[i] == 5:
            number_of_sets_won[v[i][0]] += 3
            number_of_sets_won[v[i][1]] += 2
            number_of_sets_lost[v[i][0]] += 2
            number_of_sets_lost[v[i][1]] += 3
 

#Talikng the keys of the dictionary in List form
l = list(number_of_sets_won.keys())
lst = []
#appending all the results from the dictionery to the nested list
for i in range(len(l)):
    ele = []
    ele.append(l[i])
    ele.append(winner_five_set[l[i]])
    ele.append(winner_three_set[l[i]])
    ele.append(number_of_sets_won[l[i]])
    ele.append(number_of_games_won[l[i]])
    ele.append(number_of_sets_lost[l[i]])
    ele.append(number_of_games_lost[l[i]])
    lst.append(ele)

#sorting that nested list using python inbult function
lst.sort(key = lambda x: (-int(x[1]),-int(x[2]),-int(x[3]),-int(x[4]),int(x[5]),int(x[6])))


#for writing in a file, The list elements must be in string data type
#So, converting it into string format. 
#it's a naive approach, but I couldn't make my mind work for writing direct from a nested list
s = ''
l1 = []
l2 = [x[0] for x in lst]
for i in range(len(l)):
      s = l2[i] + ' ' + str(winner_five_set[l2[i]]) +' ' + str(winner_three_set[l2[i]]) + ' ' + str(number_of_sets_won[l2[i]]) +' ' + str(number_of_games_won[l2[i]]) +' ' + str(number_of_sets_lost[l2[i]]) + ' ' + str(number_of_games_lost[l2[i]]) + '\n'
      l1.append(s)  

#printing the file as tennis.out using writelines argument. 
with open('tennis.out','w') as fp:
    fp.writelines(l1)
fp.close()   
                
                
                
        
    
    
        
       
        
        
    
        
        
        