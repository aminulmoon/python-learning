import csv

fields = ['Name', 'Branch', 'Year', 'CGPA']

file = open('countrycode.csv', 'a+', newline='')
write = csv.writer(file)
write.writerow(fields)
file.close()

