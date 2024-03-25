from math import ceil

GRADE = {}
loop = [0, 40, 45, 50, 55, 60, 70, 101]
chars = "USEDCBA"

for i in range(1, len(loop)):
    for j in range(loop[i - 1], loop[i]):
        GRADE[j] = chars[i - 1]


def read_testscores(filename):
    with open(filename, "r") as f:
        f.readline()
        data = []
        for line in f:
            dict = {}
            line = line.strip().split(',')

            dict["class"] = line[0]
            dict["name"] = line[1]
          
            dict["overall"] = ceil((int(line[2])/30 * 15) + (int(line[3])/40 * 30)
                            + (int(line[4])/80 * 35) + (int(line[5])/30 * 20))
            dict["grade"] = GRADE[dict["overall"]]
          
            data.append(dict)
    return data


def analyze_grades(studentdata):
    analysis = {}
    for student in studentdata:
        if not student["class"] in analysis:
            analysis[student["class"]] = {chars[i]: 0 for i in range(len(chars))}
        analysis[student["class"]][student["grade"]] += 1
    return analysis