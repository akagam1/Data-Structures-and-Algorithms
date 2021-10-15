def karatsuba(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
			
	else:
		n = max(len(str(x)),len(str(y)))
		z= n/2

		a = x//10**(z)
		b = x%10**(z)
		c = y//10**(z)
		d = y%10**(z)

		p1 = karatsuba(a,c)
		p2 = karatsuba(b,d)
		p3 = karatsuba(a+b,c+d)-p1-p2

		final = p1*(10**n) + p3*10**z + p2


	return final

print(karatsuba(1562,1023))
print(karatsuba(17669933,17050622))



