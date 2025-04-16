#TASK 1 - Create a Dictionary of Student Marks

student_marks = {'alice':85, 'Victor':90 , 'sam':75, 'john':79} #student list

student_name = input('Enter student name: ') #input from user

if student_name in student_marks:
   print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Sorry, no marks found for {student_name}.") #if no name in list


print('\n')


#TASK 2 - Demonstrate List Slicing 

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('orignal list :',list)

first_five= list[:5]
print('Extracts the first five elements:', first_five)

reverse=first_five[::-1]
print("Reverses these extracted elements.:", reverse)

