import sys
import csv

def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)
        
add(['Anonymous', 'M', '54321', 'data@gmail.com'])