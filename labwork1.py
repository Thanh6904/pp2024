def number_of_student():
	return(int(input("What is the number of student ?")))

def student_information():
	id = input("What is the id of student")
	student = input("What is the name of student")
	DoB = input("What is the DoB of students? Please fill in form dd//mm/yyyy")
	students.append('id' = id,
                        'student' = student,
                         'DoB' = DoB) 

def number_course():
	return int(input("How many courses we have ?"))

def course_information():
	id = input("What is the id of course?")
	name = input("What is the name of course?")
	courses.append('id' = id, 
                       'name' = name)

def input_mark(): 
	course_id = input("What is the course you want to input mark")
	if course_id not in courses['id'] for course in courses: 
		print("This course does not exist")
	else: 
		course_mark = {}
		for student in students: 
			mark = float(input("Enter score of student has ID {students['id']}( name {students['student']}):" )) 
			course_mark[student['id']] = mark
		marks[course_id] = course_mark



def list_courses():
	for course in courses:
		print(course)

def list_students():
	for student in students:
		print(student)

def show_student_marks():
	course_id = input("Please fill course id you want to find")
	if course_id in marks:
		print(f"Mark for {course} is: ")
		for student_id, mark in marks[course_id].item():
			student_name = next(student['name'] for student in students if student['id'] == student_id)
			print(f"Student: {student_name}, ID: {student_id}, mark: {mark}")
	else:
		print("This course id is not exist")	 
courses = []
students = []
marks = {}

def main():
	number_course = number_course()
	for _ in range(number_course):
		course_information()

	number_student = number_of_student()
	for _ in range(number_student):
		student_information()	
	
	while True:
        print("\nOptions:")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            list_courses()
        elif choice == 2:
            list_students()
        elif choice == 3:
            input_marks()
        elif choice == 4:
            show_student_marks()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
	
