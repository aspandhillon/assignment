#ques1

print('Ques1')

#Taking input from user
input_string=str(input("Enter any string: "))
list1=input_string.split() 

#creating a dictionary
dict={} 
if list1.__len__()==1:   
    for i in list1[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list1:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#ques2

print('Ques2')
#Taking input for year

day = int(input("Input a day [1-31]: "))
month = int(input("Input a month [1-12]: "))
year = int(input("Input a year: "))

#finding out if the year is a leap year or not
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False
#finding the length of month
if month in (1, 3, 5, 7, 8, 10, 12):
    month_duration = 31
elif month == 2:
    if leap_year:
        month_duration = 29
    else:
        month_duration = 28
else:
    month_duration = 30


if day < month_duration:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd-mm-yyy] %d/%d/%d." % (day, month, year))
print("\n")


#ques3

print('Ques3')

#creating the list of numbers
list=[50,356,5,25]

#Getting the required output
final_list = [(number, number**2) for number in list]
print(final_list)

print("\n")



#ques4

print('Ques4')

grade_point=int(input("Enter the grade:"))

letter_grade={ 4:'D', 5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}

performance={4:'Poor',5:'Below Average',6:'Average',7:'Good',8:'Very Good',9:'Excellent',10:'Outstanding'}

if grade_point<4 or grade_point>10:
    print("ERROR")
else:
    print("Your grade is", letter_grade[grade_point], "and", performance[grade_point], 'performance')

print("\n")



#ques5

print('Ques5')

#using the slice function for string

string1='ABCDEFGHIJK'
print(string1)

string2=string1[:9]
print(string2)

string3=string1[:7]
print(string3)

string4=string1[:5]
print(string4)

string5=string1[:3]
print(string5)

string6=string1[:1]
print(string6)

print("\n")


#ques6

print('Ques6')

sid = int(input("Enter SID of the student: "))
name = input("Enter Name of the student: ")
student_data = {sid:name}

while True:
    wish = input("Do you wish to enter details of another student?(Y or N): ").upper()
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        student_data[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input')


#6a
print("answer a:" ,student_data)

#6b
print("answer b:" ,{k:v for k,v in sorted(student_data.items(), key= lambda x:x[1])})

#6c
print("answer c:" ,{k:v for k,v in sorted(student_data.items())})

#6d
search = int(input("Please Enter SID of the student: " ))
print("d. Student with given SID is: " ,student_data[search])

print("\n")



#ques7

print('Ques7')

# Python program to display the Fibonacci sequence
def fibosequence(n):
   if n <= 1:
       return n
   else:
       return(fibosequence(n-1) + fibosequence(n-2))

terms = int(input("enter a number: "))

# check if the number of terms is valid
if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(terms):
       print(fibosequence(i))
       sum=sum+fibosequence(i)

#printing average of resultant sequence 

avg=float(sum/terms)
print("average of the resultant sequence is:", avg)
print("\n")

print("\n")



#ques8

print('Ques8')

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

#8a
set_a = (Set1|Set2)-(Set1&Set2)
print("part a answer set: ", set_a)

#8b
set_b = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print("part b answer set: ", set_b)

#8c
set_c= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print("part c answer set: ", set_c)

#8d
set_d= set()
for i in range(1, 11):
    if i not in Set1:
        set_d.add(i)
print("part d answer set: ", set_d)

#8e
set_e = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        set_e.add(i)
print("part e answer set: ", set_e)
