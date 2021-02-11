n = int(input("Please enter student : "))
print("-"*25)
stu = [0,0,0,0,0,0]
score = ["90-100 :","80-89  :","70-79  :","60-69  :","50-59  :","0-49   :"]
i=0
while (i<=n):
    x = int(input("Please enter score : "))
    if x >= 90 and x <= 100 :
        stu[0] += 1
    elif x >= 80 and x <= 89 :
        stu[1] += 1
    elif x >=70 and x <=79 :
        stu[2] += 1
    elif x >=60 and x <=69 :
        stu[3] += 1
    elif x >=50 and x <=59 :
        stu[4] += 1
    elif x >=0 and x <=49 :
        stu[5] += 1
    i+=1
i=0
while (i<6):
    print(score[i],"*"*stu[i])
    i+=1