import sys
import os
import traceback
files = os.listdir()
def decode(s): 
	l = ("a", "b", "c", "d", "e","f","x", "q", "z", "y", "k", "1", "2","3","4","5","6","7","8", "9","A", "B", "C", "D", "E","F","X", "Q", "Z", "Y")
	f = l[::-1]
	new_s=""
	for i in range(0, len(s), 1): 
		if(s[i] in l): 
			new_s+=l[f.index(s[i])]
		else: 
			new_s+=s[i]
	return new_s; 
if (len(sys.argv) > 1):
	address = " ".join(sys.argv[1:])
try:
	with open(address+".txt") as file:
		n = file.read()
		print(decode(n))
except FileNotFoundError: 
	for f in files: 
		if(f[0] == address[0]): 
			print(f)
except:
	print("no file found")
	traceback.print_exc()
