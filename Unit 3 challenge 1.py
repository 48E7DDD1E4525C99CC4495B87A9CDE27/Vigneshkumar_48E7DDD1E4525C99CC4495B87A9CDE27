# Program = Product Search
def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Provide a list of available products
available_products = ["apple", "banana", "orange", "apple", "grape", "apple"]

# Print the available products
print("Available products:", available_products)

# Ask the user for the target product
target_product = input("Enter the target product: ")

# Perform the linear search and get the indices
result = linear_search_product(available_products, target_product)

if result:
    print(f"The product '{target_product}' was found at indices: {result}")
else:
    print(f"The product '{target_product}' was not found.")
[24/09, 9:19 am] Asharika SNGC: # Program =Student Marksheet
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Function to input student details
def input_student_details():
    num_students = int(input("Enter the number of students: "))
    students = []

    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        roll_number = input(f"Enter roll number of student {i+1}: ")
        cgpa = float(input(f"Enter CGPA of student {i+1}: "))
        students.append(Student(name, roll_number, cgpa))

    return students

# Test the function

student_list = input_student_details()
sorted_students = sort_students(student_list)

# Print the sorted list of students
print("------STUDENTS MARKSHEET-------")
for student in sorted_students:
    print(f"Name: {student.name}\t Roll Number: {student.roll_number}\t CGPA: {student.cgpa}")
