import csv
filename = open('indians-diabetes.data.csv' , 'r')
reader = csv.reader(filename, delimiter = ',')
lines = list(reader)
print("\n\nNo of rows:", len(lines), "\n\n")
print(lines)
for l in lines:
 print (l)