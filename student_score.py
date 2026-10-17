student_score = ("Alice", 78), ("Bob", 45), ("Charlie", 90), ("Diana", 62), ("Kent", 30)

#student = tuple(student_score)
#
#print(student)

for name, score in student_score:
      print("Name: ", name)
      print("Score: ", score)
      
for name, score in student_score:
      if score >= 50:
            print("Name: ", name)
#            print("Score: ", score)
            
count = 0
for name, score in student_score:
      if score >= 50:
            count += 1
print("Student passed: ", count)
