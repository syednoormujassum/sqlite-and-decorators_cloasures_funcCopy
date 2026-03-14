import sqlite3 as sq

connection=sq.connect("users_details.db")

cursor=connection.cursor()


cursor.execute('''
               
               create table if not exists users(
               user varchar(20),
               usrname varchar(20),
               team varchar(20),
               created_At TEXT DEFAULT (datetime('now','localtime'))
               )
               ''')


user_details_values=[
("Syed Noor Mujassum","snm","Data Engineering"),
("Amira","AM","Java script"),
("Niranjan","Nbhimavarapu","Cloud Engineering"),
("Shreya Bhargav","Sb","Data Analyst"),
("Pooja Jain","Pjain","Business Analyst")
]

for user_details_value in user_details_values:
    cursor.execute('''
               Insert into users (user,usrname,team)values(?,?,?)
               
               ''',user_details_value)


connection.commit()


cursor.execute('''
               select * from users
               ''')

for row in cursor.fetchall():
    print(row)

