import numpy as n

student_name = input("Enter the name\n")

subject_scores = []

for i in range(0,6):
    subject_scores.append(int(input("Enter the number\n")))
    # subject_scores[i] = (int(input("Enter the number\n")))

total_score = sum(subject_scores)
average_score = total_score / 6



if average_score >= 50:
    print("pass")
elif average_score < 50:
    print("fail")    

# print(student_name)
print(subject_scores)
print(total_score)
print(average_score)
    