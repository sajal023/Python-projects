stu_h = input("enter the height of students: ").split()
for i in range(0, len(stu_h)):
    stu_h[i] = int(stu_h[i])
print(stu_h)
sum_of_heights = sum(stu_h)
print(sum_of_heights)
avg = sum_of_heights / len(stu_h)
print(avg)
