from functools import total_ordering

#  é uma lista de números que representam os escores de estudantes.
student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# Ela armazenará a soma cumulativa dos escores.
sun = 0
for score in student_score:
    # sun = sun + score
    sun += score

print(sun)



# Retornando o maior número

student_score2 = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_score2))


# Retornando o maior numero e somando
student_score3 = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for score in student_score3:
    if score > max_score:
        max_score = score
        
print(max_score)