Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#ques1
inputstring="Python is a case sensitive language"


#a 
print('Length of the input string is: ',len(inputstring))

Length of the input string is:  35
#c
newstring=inputstring[10:26]
print('New string is: ', newstring)
New string is:  a case sensitive
#d
print(inputstring.replace("a case sensitive","object oriented"))
Python is object oriented language
#e
print('Index of substring "a" in the given input string: ',inputstring.index("a"))
Index of substring "a" in the given input string:  10
#f
print('Removing the white spaces from given input: ',inputstring.replace(" ",""))
Removing the white spaces from given input:  Pythonisacasesensitivelanguage



#ques2
name="Aspan Dhillon"
sid="21104045"
department="Electrical Engineering"
cgpa="9.8"
print("Hey,",name,"here!",'\n' "My SID is ",sid,'\n' "I am from ",department,"and my CGPA is ",cgpa)

Hey, Aspan Dhillon here! 
My SID is  21104045 
I am from  Electrical Engineering and my CGPA is  9.8



#ques3
a=56
b=10
#a
print('a&b ',a&b)
a&b  8
#b
print('a|b ',a|b)
a|b  58
#c
print('a^b ',a^b)
a^b  50
#d
print('Left shift a: ',a<<2)
Left shift a:  224
print('Left shift b: ',b<<2)
Left shift b:  40
#e
print('Right shift a: ',a>>2)
Right shift a:  14
print('Right shift b: ',b>>2) 

Right shift b:  2



#ques4
number1=input('Enter the first number:')
Enter the first number:12
number2=input('Enter the second number:')
Enter the second number:23
number3=input('Enter the third number:')
Enter the third number:45
numbers=[number1,number2,number3]
numbers.sort()
print('Greatest of these three numbers is: ',numbers[-1])
Greatest of these three numbers is:  45



#ques5
string=str(input('Enter input string: '))
Enter input string: My name is Aspan
if "name" in string:
    print('Yes')
else:
    print('No')

    
Yes



#ques6
a=input('Enter the first side:')
Enter the first side:20
b=input('Enter the second side:')
Enter the second side:50
c=input('Enter the third side:')
Enter the third side:100
if b+c>a:
    print('Yes, the triangle will be formed')
elif a+c>b:
    print('Yes, the triangle will be formed')
elif a+b>c:
    print('Yes, the triangle will be formed')
else:
    print('No, the triangle will not be formed')

    
Yes, the triangle will be formed
