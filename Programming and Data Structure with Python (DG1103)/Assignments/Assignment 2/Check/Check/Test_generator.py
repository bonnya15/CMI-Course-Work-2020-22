import pickle
import random 
import os

os.chdir("poly")

for testcase in range(20):


	print(testcase)
	max_degree = 10

	poly_1 = {}
	poly_2 = {}

	for i in range(max_degree + 1):

		zero_1 = random.randint(0,1)
		zero_2 = random.randint(0,1)
		if(zero_1 == 0):
			coeff_1 = random.randint(-100,100)
			if(coeff_1!=0):
				poly_1[i] = coeff_1 

		if(zero_2 == 0):
			coeff_2 = random.randint(-100,100)
			if(coeff_2!=0):
				poly_2[i] = coeff_2 


	pickle.dump([poly_1, poly_2], open( str(testcase) + ".p", "wb" ) )

os.chdir("..")

os.chdir("listdiff")

for testcase in range(20):

	print(testcase)

	l_1 = []

	m = 0
	while(m < 100):
		m =random.randint(m + 1, 110)
		l_1.append(m)

	l_2 = []
	m = 0
	while(m < 100):
		m =random.randint(m + 1, 110)
		l_2.append(m)

	pickle.dump([l_1, l_2], open( str(testcase) + ".p", "wb"))


os.chdir("..")

os.chdir("matched")

st = []
st.append("((jkl)78(A)&l(8(dd(FJI:),):)?)")
st.append("aasjbu281192y38172910`0`99!(@)!WI@E!))!W)*DWJ)")
st.append("()19129101()!sjnds(!s0)")
st.append("(a)*(?)")
st.append("((ajk)12)21w()r43(s)))(")
st.append("(a(s)dffv)y(bg)y(67)n")
st.append("zb%78")
st.append("(7)(a")

for testcase in range(8):

	print(testcase)
	pickle.dump(st[testcase], open( str(testcase) + ".p", "wb"))





