import sqlite3
import os
conn = sqlite3.connect(r'D:\Jirapat_python\week6\work6.db')
c = conn.cursor()

c.execute ('''CREATE TABLE students(id integer PRIMARY KEY AUTOINCREMENT,
    name varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    gender varchar(10) NOT NULL,
    old varchar(10) NOT NULL,
    year varchar(2) NOT NULL)''')

def menu():
    global choice
    print('---ระบบทะเบียนนักเรียน---\nเพิ่มนักเรียน[a]\nแสดงข้อมูล[s]\nแก้ไขข้อมูลนักเรียน[e]\nลบข้อมูลนักเรียน[d]\nออกจากโปรแกรม[x]')
    choice = input('กรุณาเลือกทำรายการ : ')

def add():
    s_name = input('ใส่ชื่อ-สกุล: ')
    s_email = input('ใส่อีเมลล์: ')
    s_gender = input('ใส่เพศ: ')
    s_old = input('ใส่อายุ: ')
    s_year = input('ใส่ชั้นปี: ')
    c.execute("""INSERT INTO students(name,email,gender,old,year)VALUES (?,?,?,?,?)""",
         (s_name,s_email,s_gender,s_old,s_year))
    conn.commit()
    print('เพิ่มข้อมูลเรียบร้อยแล้ว')

def show():
    print('{0: <10}{1: <20}{2: <20}{3: <15}{4: <15}{5: <1}'.format('ลำดับที่','ชื่อ-สกุล','อีเมลล์','เพศ','อายุ','ชั้นปี'))
    c.execute('''SELECT * FROM students''')
    result = c.fetchall()
    for x in result:
        print('{0: <7}{1: <17}{2: <18}{3: <15}{4: <15}{5: <1}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))

def edit():
    line = input('ใส่แถวที่จะแก้ไข: ')
    nname = input('ชื่อ-สกุลจะแก้ไข: ')
    nemail = input('ใส่อีเมลล์จะแก้ไข: ')
    ngender = input('ใส่เพศจะแก้ไข: ')
    nold = input('ใส่อายุจะแก้ไข: ')
    nyear = input('ใส่ชั้นปีจะแก้ไข: ')
    data = (nname,nemail,ngender,nold,nyear,line)
    c.execute('''UPDATE students SET name=?,email=?,gender=?,old=?,year=? WHERE id= ?''',data)
    print('แก้ไขเรียบร้อยแล้ว')
    conn.commit()

def delete():
    delete = input('ใส่เลขที่ต้องการลบ : ')
    c.execute('''DELETE FROM students WHERE id = ?''',delete)
    conn.commit()

while True:
    menu()
    if choice =='a':
        add()
    elif choice =='s':
        show()
    elif choice =='e':
        edit()
    elif choice =='d':
        delete()
    elif choice =='x':
        exitt = input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if exitt == 'y':
            conn.close()
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
        elif exitt == 'n':
            continue