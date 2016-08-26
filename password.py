#Password Program
#By Aidan Sciortino
#Written to teach python
resetPass = input("Do you want to reset your password? (y/n): ")
if resetPass == "y":
	f = open("passwd.txt","w")
	newPass = input("Enter your new password: ")
	f.write(newPass + "\n")
	f.close()
f = open("passwd.txt", 'r')
pLength = len(f.readline())
f.seek(0)
password = f.readline(pLength - 1)
passIn = ""
repeat = True
while(repeat):
	passIn = input("Enter your Password: ")
	if passIn == password:
		print("Super Secret Message")
		repeat = False
	else :
		print("Password incorrect")
