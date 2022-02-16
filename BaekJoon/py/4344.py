import sys

n = int(sys.stdin.readline())

for i in range(n):
    numlist = sys.stdin.readline().split(' ')
    student_count = int(numlist[0])
    ave_student = 0
    scoreList = []
    for j in range(1,len(numlist)):
        scoreList.append(int(numlist[j]))
    for j in scoreList:
        if j > (sum(scoreList) / student_count):
            ave_student += 1
    print('{0:.3f}%'.format((ave_student/student_count)*100))