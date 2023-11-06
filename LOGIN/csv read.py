import csv

with open('login.csv','r') as file:
    data = csv.reader(file)
    for row in data:
        username = row[2]
        password = row[3]
print(username,password)