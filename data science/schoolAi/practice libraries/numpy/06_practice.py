import numpy as np
marks = np.array([45, 67, 89, 32, 90, 76, 55, 95, 61, 48])
mark_60 = marks[marks>=60]
mark_80 = marks[marks<80]
print(marks[(marks>=60) & (marks<80)])
print(marks[(marks>70) & (marks<90)])
print(marks[(marks<40) | (marks>90)])

marks[marks<40]=40
print(marks)

marks[marks<60] += 5
print(marks)