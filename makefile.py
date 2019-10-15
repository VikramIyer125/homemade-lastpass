import sys 
import traceback
from random import randint
user_pass = []
def makepassword():
    l = ["a", "b", "c", "d", "e","f","x", "q", "z", "y", "k", "1", "2","3","4","5","6","7","A", "B", "C", "D", "E","F","X", "Q", "Z", "Y"]
    strn = ""
    for i in range(20):
        strn += l[randint(0, len(l)-1)]
    return strn
def encrypt(s): 
	l = ("a", "b", "c", "d", "e","f","x", "q", "z", "y", "k", "1", "2","3","4","5","6","7","8", "9","A", "B", "C", "D", "E","F","X", "Q", "Z", "Y")
	f = l[::-1]
	new_s=""
	for i in range(0, len(s), 1): 
		if(s[i] in l): 
			new_s+=f[l.index(s[i])]
		else: 
			new_s+=s[i]
	# for i in range(0, len(new_s), 1): 
	# 	new_s = new_s[0:i] + str(ord(new_s[i])) + new_s[i+1:]
	# for i in range(0, len(new_s),1): 
	# 	if(i%2==1): 
	# 		new_s = new_s[0:i] + f[l.index(new_s[i])] + new_s[i+1:]
	# 	else: 
	# 		new_s = new_s[0:i] + l[f.index(new_s[i])] + new_s[i+1:]
	return new_s
if (len(sys.argv) > 1): 
	for i in range(1, len(sys.argv), 1): 
		user_pass.append(sys.argv[i])
try: 
	f = user_pass[0]+".txt"
	df= open(f,"w+")
	df.write(encrypt(user_pass[1])+"\n")
	try: 
		df.write(encrypt(user_pass[2]))
	except:
		df.write(encrypt(makepassword()))
	
	df.close()
except: 
	print("not enough entered")
	traceback.print_exc()
