"""
Day 04 
Date: 21st April 2022 thursday
Name: Bapatla sravan
File Desc: Type convertion
"""
a=3249
print(float(a)) # 3249
print(str(a)) # 3249.0

b='75'
print(int(b)) # 75
print(float(b)) # 75..0


c=32 ; d=4.9
print(c+d) # 36.9

# e='Python'
# print(int(e)) # TypeError
# print(float(e)) # TypeError ValueError: could not convert string to float: 'Python'

f='5.6'
g=float(f)
# print(int(f)) # Error
print(float(f)) # 5.6
print(int(g))


h=32 ; i='A' ; j=5.2
print(type(h)) # int
print(type(i)) # str
print(type(j)) # float
print(h+j) # 37.2
# print(i+j) # Error

k='Python'  ;  l='Fullstack'
print(k+l)  # Pythonfullstack
