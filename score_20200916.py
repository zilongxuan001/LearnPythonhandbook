# score.py
score = eval(input("请输入成绩: "))
if score >= 60 and score < 70:
    grade = "D"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 80 and score <90:
    grade = "B"
elif score >= 90 and score <= 100:
    grade = "A"
else:
    grade = "0"
    print("请输入100以内的分数。")
    

print("输入成绩属于级别{}".format(grade))


