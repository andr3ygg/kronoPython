import os 
filename = input("filename: ")

if os.path.exists(filename):
	print("File exists")
elif not os.path.exists(filename):
	os.mkdir(f"./{filename}")
else:
	print("error")
