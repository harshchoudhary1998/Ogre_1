import csv
import pandas as pd

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Col1', 'Col2', 'Col3'])
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

data_frame = pd.read_csv('employee_file.csv', delimiter=',')
data = data_frame[['Col1', 'Col2', 'Col3']]
for line in data:
    print(line)
