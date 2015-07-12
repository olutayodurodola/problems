#python program to check if the input is prime
def check_prime(mynum):
	if mynum > 1:
		for i in range(2,mynum):
			if (mynum % 1) == 0:
				print(mynum," is not a prime number")
				break
		else:
			print(mynum,"is a prime number")
	else:
		print(mynum,"is not a prime number")

num = int(raw_input("Enter a number: "))

check_prime(num)




class PrimeChecker(object):
  def __init__(self,mynum):
  	self.mynum = mynum
    pass
  #python program to check if the input is prime
  def is_prime(self):
  	mynum = self.mynum
	  if mynum > 1:
		  for i in range(2,mynum):
			  if (mynum % 1) == 0:
				  return False
				  # print(mynum," is not a prime number")
				  break
		  else:
			  return True
			  #print(mynum,"is a prime number")
	  else:
	    return False
		  #print(mynum,"is not a prime number")

