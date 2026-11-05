#string------------

a = "Hello"
print(a)
a = "Hello"
print(a)
print(a[4])
print(a[-4])

#Formatted strings---------

age = 16
print(f"I am sweet {age} now!")


#Strings methods-------------

#string/Text er opor operation chalatey gele string method use korte hoy.

name = "Sourav"

print(name)
print(name.upper())
print(name.lower())
print(name.replace("S","Sho"))


#Numbers and Math operations-------------


a = 10
b = 20
print(a+b)
c = a+b
print(c)

print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 10
b = 3
print(a/b) 
print(a//b) 
print(a%b) 
print(2**3) 

a = int(input())
b = int(input())
print(a+b)


#Operator precedence(Follow PEMDAS Law)---------------

print(10+20*2)
print((10+(20*2)))


#Math functions---------------

#Absulate value =[poromman] always positive thakbe

print(abs(5))
print(abs(-5))

#import math
#print(math.cos())


#If,elif,else-------------------

a = 5
b = 7

#Relational operator show below:
#< = is less than
#> = is greater than
#= = Assign kora
#== = is equql to(compair kora)
#! = is not equal to

print(a+b)
print(a<b)
print(a>b)

#Comparison operators-----------

#if a is greater thab b
#print a is bigger
#else
#print a is not the bigger one


a = int(input())
b = int(input())
if a > b:
    print("a is bigger")
elif b > a:
    print("b is bigger")    
else:
    print("both are equal")



#Logical operators----------------


#(And(abong),Or(othoba),Not(na))

if True and True:
    print("Amake ki kew dekhbe?")

a = 10 
b = 20
c = 30

if c>a and c>b:
    print("C sobcheye boro!")

a = 5    
b = 7

if a > b:
    print("A boro!")
    print("Hehehehe!")
    print("Huhuhuhu!")
else:
    print("B boro!")
    print("Hihihihi!")  

a = "Hello"
print(a.replace("H", "B"))
print(a)

#Dynamically typed
#b*b - 4*a*c
















