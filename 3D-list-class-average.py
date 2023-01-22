written1 = []
num_of_rows1 = 3
num_of_columns1 = 5
print("Enter the Answers in Exam 1: ")
for row in range(num_of_rows1):
    written1.append([])
    print("Enter the answers of student ", row + 1)
    for column in range(num_of_columns1):
        value = input("enter an answer")
        written1[row].append(value)
print(written1)

print("Enter the Answers in Exam 2: ")
written2 = []
num_of_rows2 = 3
num_of_columns2 = 5
for row in range(num_of_rows2):
    written2.append([])
    print("Enter the answers of student ", row + 1)
    for column in range(num_of_columns2):
        value = input("enter an answer")
        written2[row].append(value)
print(written2)

key1 = ['A', 'C', 'A', 'E', 'A']

scorelst1 = []
for row in range(len(written1)):
    score1 = 0
    for col in range(len(written1[row])):
        if written1[row][col] == key1[col]:
            score1 += 20
    scorelst1.append(score1)
print(scorelst1)

key2 = ['B', 'B', 'C', 'A', 'E']

scorelst2 = []
for row in range(len(written2)):
    score2 = 0
    for col in range(len(written2[row])):
        if written2[row][col] == key2[col]:
            score2 += 20
    scorelst2.append(score2)
print(scorelst2)

scorelst = []
for i in range(len(scorelst1) + len(scorelst2)):
    if i % 2 == 0:
        scorelst.append(scorelst1[i // 2])
    else:
        scorelst.append(scorelst2[i // 2])
print(scorelst)

lab1 = []
num_of_rows3 = 3
num_of_columns3 = 3
print("Enter the marks of Lab 1: ")
for row in range(num_of_rows3):
    lab1.append([])
    print("Enter the mark of student ", row + 1)
    for column in range(num_of_columns3):
        value = input("enter an answer")
        lab1[row].append(value)
print(lab1)
lablst1 = []
for i in range(len(lab1)):
    sumlab1 = 0
    for j in range(len(lab1[0])):
        sumlab1 += int(lab1[i][j])
    labav1 = sumlab1 / len(lab1[0])
    lablst1.append(labav1)
print(lablst1)

lab2 = []
num_of_rows4 = 3
num_of_columns4 = 3
print("Enter the marks of Lab 2: ")
for row in range(num_of_rows4):
    lab2.append([])
    print("Enter the mark of student ", row + 1)
    for column in range(num_of_columns4):
        value = input("enter an answer")
        lab2[row].append(value)
print(lab2)
lablst2 = []
for i in range(len(lab2)):
    sumlab2 = 0
    for j in range(len(lab2[0])):
        sumlab2 += int(lab2[i][j])
    labav2 = sumlab2 / len(lab2[0])
    lablst2.append(labav2)
print(lablst2)

lablst = []
for i in range(len(lablst1) + len(lablst2)):
    if i % 2 == 0:
        lablst.append(lablst1[i // 2])
    else:
        lablst.append(lablst2[i // 2])
print(lablst)

classsum = []
num_of_rows5 = 3
num_of_columns5 = 2

for row in range(num_of_rows5):
    classsum.append([])
    for column in range(num_of_columns5):
        classsum[row].append([])
        for k in range(num_of_columns5):
            if row == 0:
                if k == 0:
                    classsum[row][column].append(scorelst[column])
                else:
                    classsum[row][column].append(lablst[column])
            else:
                if k == 0:
                    classsum[row][column].append(scorelst[(2 ** row) + column])
                else:
                    classsum[row][column].append(lablst[(2 ** row) + column])

print(classsum)

# classsum = [[[80, 60], [60, 70]], [[90, 40], [30, 80]], [[100, 40], [90, 80]]]
studnotes = []
for row in range(len(classsum)):
    examsum = 0
    labsum = 0
    for column in range(len(classsum[row])):
        for k in range(len(classsum[row][column])):
            if k % 2 == 0:
                examsum += classsum[row][column][k]
            else:
                labsum += classsum[row][column][k]
    studav = (0.7 * examsum) / 2 + (0.3 * labsum / 2)
    studnotes.append(studav)
    print("student ", row + 1, " scored ", studav)
classav = 0
mn = studnotes[0]
mx = studnotes[0]
for i in range(len(studnotes)):
    classav += studnotes[i]
    if studnotes[i] < mn:
        mn = studnotes[i]
    elif studnotes[i] > mx:
        mx = studnotes[i]
print("Average of the class is ", classav / 3)
print("the maximum score in the class is ", mx)
print("the minimum score of the class is ", mn)
