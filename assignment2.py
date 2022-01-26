#ques1
inputstring="Python is a case sensitive language"

#a 
print('Length of the input string is: ',len(inputstring))

#b
print('Reversing the order of string : ',inputstring[::-1])

#c
newstring=inputstring[10:26]
print('New string is: ', newstring)

#d
print(inputstring.replace("a case sensitive","object oriented"))

#e
print('Index of substring "a" in the given input string: ',inputstring.index("a"))

#f
print('Removing the white spaces from given input: ',inputstring.replace(" ",""))



#ques2
name="Aspan Dhillon"
sid="21104045"
department="Electrical Engineering"
cgpa="9.8"

print("Hey,",name,"here!",'\n' "My SID is ",sid,'\n' "I am from ",department,"and my CGPA is ",cgpa)

#ques3
a=56
b=10

#a
print('a&b ',a&b)
#b
print('a|b ',a|b)
#c
print('a^b ',a^b)
#d
print('Left shift a: ',a<<2)
print('Left shift b: ',b<<2) 
#e
print('Right shift a: ',a>>2) 
print('Right shift b: ',b>>2) 


#ques4
number1=input('Enter the first number:')
number2=input('Enter the second number:')
number3=input('Enter the third number:')
numbers=[number1,number2,number3]
numbers.sort()
print('Greatest of these three numbers is: ',numbers[-1])


#ques5
string=str(input('Enter input string: '))
if "name" in string:
print('Yes')
else:
print('No')

#ques6
a=input('Enter the first side:')
b=input('Enter the second side:')
c=input('Enter the third side:')
if b+c>a:
print('Yes, the triangle will be formed')
elif a+c>b:
print('Yes, the triangle will be formed')
elif a+b>c:
print('Yes, the triangle will be formed')
else:
print('No, the triangle will not be formed')

