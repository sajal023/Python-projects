'''
score=input("enter the scores: ").split()
for i in range(0,len(score)):
    score[i]=int(score[i])
print(score)
max_score=score[0]
for i in range(0,len(score)):
    if max_score<score[i]:
        max_score=score[i]
print(f"the highest score is: {max_score}")
'''
# 2nd approach:-
score = input("enter the scores: ").split()
for i in range(0, len(score)):
    score[i] = int(score[i])
print(score)

print(max(score))
