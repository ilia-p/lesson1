def sum_string(str1,str2,delimeter=' '):
	str1=str(str1)
	str2=str(str2)
	x = str1+delimeter+str2
	return x.upper()
x=sum_string('23','Petrov')
print(x)