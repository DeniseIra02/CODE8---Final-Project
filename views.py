import sys
import csv

#add a data
def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

#dummydata        
add(['Anonymous', 'M', '54321', 'data@gmail.com'])

#view data/show data
def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)

view()