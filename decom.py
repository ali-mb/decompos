import sys
def prime(a):
	if a > 1 :
		for x in range(2,a):
			if(a%x) == 0 :
				return False
		else :
			return True
	else :	
		return "Non"						

def decom (n):
	x=0
	if prime(n) == True:
		print(1)
		print( "*")
		print(n)
	else :		
		for i in range(2,n):
			if prime(i) == True :
				if(n%i) == 0 :
					while (n%i) == 0 :
						x=x+1 
						n=n/i
					print(x) 	
					sys.stdout.write("of")
					print(i)
					print("---")
					x=0	

a=int(input("Enter number :"))
decom(a)
#n=int(input())
#if prime(n) == True :
#	print("It's prime number")
#else :
	#print("It's composite number")	
