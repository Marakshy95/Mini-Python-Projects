# import random
# names = ["sameh", "samir", "ariel", "laila", "emad"]

# student_scores = {student:random.randint(1,100) for student in names}


# passed_students = {student:score for (student, score) in student_scores.items() if score >= 50}

# print(passed_students)

#=========================================
#list to dict

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {name:len(name) for name in sentence.split()}

print(result)





