student_a = {'name': 'a', 'age' : 16, 'course': 'Computer Science'}

lookup_name = str(input("Please enter the name: "))
lookup_age = int(input("Please enter the age: "))
lookup_course = str(input("Please enter the course: "))

all_keys = []

for key, value in student_a.items():
   if(value == lookup_name):
       all_keys.append(key)
       print(all_keys)
   elif(value == lookup_age):
       all_keys.append(key)
       print(all_keys)
   elif(value == lookup_course):
       all_keys.append(key)
       print(all_keys)
   else:
       print("Not Found")
