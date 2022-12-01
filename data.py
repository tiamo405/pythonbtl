
import pandas as pd
import csv
with open('questions.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
df = pd.read_csv("questions.csv", encoding='utf-8')
questions = []

df = df.sample(frac = 1)
for i in range(len(df)) :
    q = df['aws'][i]
    a1,a2,a3,a4 = df['A'][i], df['B'][i], df['C'][i], df['D'][i]
    questions.append([q, [a1, a2, a3, a4]])
print(questions)
