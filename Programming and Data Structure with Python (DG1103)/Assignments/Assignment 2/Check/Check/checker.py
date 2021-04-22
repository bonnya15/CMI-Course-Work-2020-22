import assignment2
import correct
import os
import pickle 
import copy

os.chdir("poly")

correct_poly_add = 0
correct_poly_mul = 0

for i in range(20):

	file = open(str(i) + '.p', 'rb')

	[d1,d2] = pickle.load(file)

	try:
		#print(d1, d2)
		#print(assignment2.addpoly(d1.copy(), d2.copy()))
		#print(correct.addpoly(d1.copy(),d2.copy()))
		#print("-----------------------------")
		if(assignment2.addpoly(d1.copy(), d2.copy()) == correct.addpoly(d1.copy(),d2.copy())):
			correct_poly_add +=1
	except:
		print("Error on test_case: ", i, "for addpoly")

	try:
		
		if(assignment2.multpoly(d1.copy(), d2.copy())== correct.multpoly(d1.copy(),d2.copy())):
			correct_poly_mul +=1
		else:
			print(d1, "," , d2)
	except:
		print(d1, "," , d2)
		print("Error on test_case: ", i, "for multpoly")


	
os.chdir("..")
os.chdir("listdiff")

correct_list_diff = 0

for i in range(20):

	file = open(str(i) + '.p', 'rb')

	[l_1,l_2] = pickle.load(file)

	try:
		if(assignment2.listdiff(l_1, l_2)== correct.listdiff(l_1, l_2)):
			correct_list_diff +=1
		else:
			print(l_1, l_2)
	except:
		print("Error on test_case: ", i, "for listdiff")
	

os.chdir("..")
os.chdir("matched")

correct_matched = 0

for i in range(8):

	file = open(str(i) + '.p', 'rb')

	s = pickle.load(file)

	try:
		if(assignment2.matched(s)== correct.matched(s)):
			correct_matched +=1
		else:
			print(s)
	except:
		print("Error on test_case: ", i, "for matched")

	

print("Score for matched: ", (correct_matched/8)*100)
print("Score for listdiff: ", correct_list_diff*5)
print("Score for polyadd: ", correct_poly_add*5)
print("Score for polymult: ", correct_poly_mul*5)

