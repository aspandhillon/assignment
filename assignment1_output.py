Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#ques1
num1=int(input('Enter first number '))
Enter first number 260
num2=int(input('Enter second number '))
Enter second number 540
num3=int(input('Enter third number '))
Enter third number 680
average=(num1+num2+num3)/3
print(average)
493.3333333333333




#ques2
gross=int(input('Enter your Gross Income '))
Enter your Gross Income 20000
number=int(input('Enter the number of Dependents '))
Enter the number of Dependents 2
taxable_income = gross-10000-(3000*number)
print('Taxable Income= ', taxable_income)
Taxable Income=  4000
tax = taxable_income*0.2
print('Tax= ', tax)
Tax=  800.0



#ques3
Ram = [41114000,'Ram','M','ESC1101',9.4]
print('Student Details: ', Ram)
Student Details:  [41114000, 'Ram', 'M', 'ESC1101', 9.4]



#ques4
student1=int(input('Enter marks of first student: '))
Enter marks of first student: 98
student2=int(input('Enter marks of second student: '))
Enter marks of second student: 89
student3=int(input('Enter marks of third student: '))
Enter marks of third student: 90
student4=int(input('Enter marks of fourth student: '))
Enter marks of fourth student: 95
student5=int(input('Enter marks of fifth student: '))
Enter marks of fifth student: 85
marks=[student1,student2,student3,student4,student5]
marks.sort()
print('Sorted order of marks: ', marks)
Sorted order of marks:  [85, 89, 90, 95, 98]




#ques5
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Color.remove('Black')
#The colour black will be removed from the list
print(Color)
['Red', 'Green', 'White', 'Pink', 'Yellow']




#ques5b
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Color[3:5] = ['Purple']
#Replacing colours Black and Pink with Purple
print(Color)
['Red', 'Green', 'White', 'Purple', 'Yellow']
