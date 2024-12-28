####1
student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades={}
for i in student_scores:
    score= student_scores[i]
    if score>91:
        student_grades[i]="Outstanding"
    elif score>=81 and score<91:
        student_grades[i] = "Exceeds Expectation"
    elif score>=71 and score<81:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"
print(student_grades)


###2
travel_log=[
{
    "country":"France",
    "visits": 12,
    "cities": ["paris","lillie","dijon"]
},
{
    "country":"Germany",
    "visits": 5,
    "cities": ["Berlin","Hamburg","Stuttgart"]
},
]
def add_new_country(str,v,l):
    dic={}
    dic["country"]=str
    dic["visits"]=v
    dic["cities"]=l
    travel_log.append(dic)

add_new_country("Russia",2,["moscow", "saint petersburg"])
print(travel_log)