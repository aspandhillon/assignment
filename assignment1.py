#ques1
num1=int(input('Enter first number '))
/n
num2=int(input('Enter second number '))
/n
num3=int(input('Enter third number '))
/n
average=(num1+num2+num3)/3
print(average)



#ques2
gross=int(input('Enter your Gross Income '))
/n
number=int(input('Enter the number of Dependents '))
/n
taxable_income = gross-10000-(3000*number)
print(taxable_income)
/n
tax = taxable_income*0.2
print(tax)



#ques3
Ram = [41114000,'Ram','M','ESC1101',9.4]
/n
print('Student Details: ', Ram)



#ques4
student1=int(input('Enter marks of first student: '))
/n
student2=int(input('Enter marks of second student: '))
/n
student3=int(input('Enter marks of third student: '))
/n
student4=int(input('Enter marks of fourth student: '))
/n
student5=int(input('Enter marks of fifth student: '))
/n
marks=[student1,student2,student3,student4,student5]
marks.sort()
print('Sorted order of marks: ', marks)



#ques5a
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Color.remove('Black')
print(Color)


#ques5b
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Color[3:5] = ['Purple']  
#Replaced Black and Pink with Purple
print(Color)

