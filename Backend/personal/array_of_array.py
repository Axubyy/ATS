N = input()
d = {}
for i in range(int(N)):
    score = input()
    name = input()

    d[name] = score
    sorted_scores = sorted(list(set(d.values())))
    second_lowest = sorted_scores[1]
    student_names = []
    for key, value in d:
        if second_lowest == value:
            student_names.append(key)
    main_name = sorted(student_names)[0]

    print(main_name)


python_students = []
second_lowest_names = []
scores = []


scores.append(score)
names = []
python_students = [[name, score]]
lowest_score = sorted(scores)[i]
for k, v in python_students:
    if lowest_score == v:
        names.append(k)
for i in sorted(names):
    print(i, end="\n")
