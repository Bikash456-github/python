######################integer#####################
#->float
n1=55
f1=55
f1=float(n1)
print(f1,type(f1)) #55.0 <class 'float'>

print("_"*50)
##int  ->String##
n2=456567
#print(n2,type(n2))
s2=str(n2)
print(s2,type(s2),s2[2]) #456567 <class 'str'> 6

print("_"*50)
str3='Hello'
print(str3)

print("_"*50)
##int -> list## conversion is not possible
"""
n3=8956948
l1=list(n3)
"""
print("_"*50)
##int => tuple conversion is not possible
print("_"*50)
#int -> dictionary  conversion is not possible
print("_"*50)
#int _>set conversion is not possible

#float -> int
f1=56.78
n1=int(f1)
print(n1,type(n1))
#56<class 'int'>