import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
db_info = '''CREATE TABLE informations (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            firstname   varchar(255),
            middlename  varchar(255),
            lastname    varchar(255),
            email       varchar(255),
            dob         date,
            gender      varchar(255),
            phonenumber varchar(255),
            address     varchar(255),
            soo         varchar(255),
            lga         varchar(255),
            nok         varchar(255) ,
            jambscore    integer,
            admissionstatus   varchar(255),
            filename          text
            );
            '''
conn.execute(db_info)
print ("Table created successfully")
conn.close()