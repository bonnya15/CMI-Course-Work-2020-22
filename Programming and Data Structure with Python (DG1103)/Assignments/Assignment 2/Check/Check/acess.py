import os
import pickle 

print("Folder name:")
folder_name = input()

print("Testcase number:")
testcase = input()

try:
	os.chdir(folder_name)
	out = pickle.load(open(str(testcase) +".p", "rb"))
	print(out)
except:
	print("enter valid arguments")

