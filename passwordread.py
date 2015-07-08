import math

content = []
no_of_valid_pwd = 0


with open("passwordtext.txt","r+") as fo:
     content = fo.readlines()

#print len(content)







def checkvalidpassword(pwd):
 	
 	my_number = 0
 	my_lowercase = 0
 	my_uppercase = 0
 	
 	for i in pwd:  #this checks for numbers
 		
 		if i.isupper():
 			my_uppercase += 1
 		elif i.islower():
 			my_lowercase += 1
 		elif i.isdigit():
 			my_number += 1

	#print my_number,my_lowercase,my_uppercase
 	if (my_number>=4) and (my_lowercase>=2) and (my_uppercase>=4):	
 		return True
 	else:
 		return False




for item in content:
	item
	#print checkvalidpassword(item)
 	if checkvalidpassword(item) == True:
 		no_of_valid_pwd += 1
 	else:
 		pass

print "Number of valid passwords are: "
print no_of_valid_pwd   #This displays the answer

 









 		
 	
 
 
