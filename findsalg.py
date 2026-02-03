import csv

def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    return dataset

attributes = ['Sky', 'Temp', 'Humidity', 'Wind', 'Water', 'Forecast']
print('Attributes =', attributes)

num_attributes = len(attributes)
filename = "finds.csv"
dataset = loadCsv(filename)

print("\nDataset:")
for row in dataset:
    print(row)

hypothesis = ['0'] * num_attributes
print("\nInitial Hypothesis:")
print(hypothesis)

print("\nThe Hypotheses are:")
for i in range(1, len(dataset)):
    target = dataset[i][-1]
    if target == 'Yes':
        for j in range(num_attributes):
            if hypothesis[j] == '0':
                hypothesis[j] = dataset[i][j]
            elif hypothesis[j] != dataset[i][j]:
                hypothesis[j] = '?'
        print(i, '=', hypothesis)

print("\nFinal Hypothesis:")
print(hypothesis)
