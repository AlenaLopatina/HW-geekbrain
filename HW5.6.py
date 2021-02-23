import re

subj = {}
with open("subject.txt", 'r', encoding='utf-8') as f_sub:
    for line in f_sub:
        subject, lecture, practice, lab = line.split()
        templec = re.findall(r'\d+', lecture)
        res1 = list(map(int, templec))
        tempprac = re.findall(r'\d+', practice)
        res2 = list(map(int, tempprac))
        templab = re.findall(r'\d+', lab)
        res3 = list(map(int, templab))
        sumsub = res1 + res2 + res3
        subj[subject] = sum(sumsub)
print(subj)
