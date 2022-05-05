import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port=5433,
    user='postgres',
    password='12345'
)

current = config.cursor()
sql1 = '''
 UPDATE phonebook SET username = 'ernar' WHERE id = '7'
'''
sql2 ='''
    UPDATE phonebook SET number = '7777858877' WHERE id = '21030793'
     '''
sql33 ='''
    SElECT username  FROM phonebook  WHERE id = '21030793';
     '''

sql3 ='''
    SElECT email  FROM phonebook  WHERE id = '88';
     '''
sql4 ='''
    SElECT number  FROM phonebook  WHERE id = '8';
     '''

current.execute(sql1)
# current.execute(sql33)
# current.execute(sql3)
# current.execute(sql4)



# final = current.fetchall()

# print(final)

current.close()
config.commit()
config.close()