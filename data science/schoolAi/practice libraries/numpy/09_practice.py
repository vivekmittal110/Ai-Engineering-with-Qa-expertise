import numpy as np
marks = np.array([
    [78, 82, 90, 67],
    [65, 72, 88, 70],
    [92, 95, 91, 89],
    [45, 56, 60, 52],
    [88, 76, 85, 90]
])
std_avg = marks.mean(axis=1)
sub_avg = marks.mean(axis=0)
print(np.ceil(std_avg))
print(np.ceil(sub_avg))

std_total = marks.sum(axis=1)
print(np.argmax(std_total))

sub_total = marks.sum(axis=0)
print(np.argmax(sub_total))
print(std_total)
print(sub_total)
