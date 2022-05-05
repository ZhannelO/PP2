# Implement two ways of inserting data into the PhoneBook.
# upload data from csv file
# entering user name, phone from console
import csv, psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5433,
    user='postgres',
    password='12345'
)

current = config.cursor()
arr = []

sql = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s);
'''

try:
    with open('a.csv') as f:
        reader = csv.reader(f, delimiter=',')
        
        for row in reader:
            # print(type(row))
            # print(row)
            row[0] = int(row[0])
            arr.append(row)
    for row in arr:
        current.execute(sql, row)    
except:
    sql = '''
    INSERT INTO phonebook
        VALUES (%s, %s, %s, %s);
    '''
    print("ID:")
    id = int(input())
    print("Username:")
    username = input()
    print("Phone number:")
    number = input()
    print("E-mail:")
    email = input()
    current.execute(sql, (id, username, number, email))
    pass

current.close()
config.commit()
config.close()