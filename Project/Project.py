import os
import sqlite3
import datetime
import time
import webbrowser
from datetime import date

conn = sqlite3.connect(r"D:\Jirapat_python\Project\Project.db")
money_d = [1000,5000,10000,50000]

def inputdata():
    while(True):
        os.system('cls')
        print("{0:*<25}".format('*'))
        print("|    กรุณากรอกข้อมูลต่อไปนี้  |\n|   ***ข้อมูลจริงเท่านั้น***  |")
        print("{0:*<25}".format('*'))
        users =input("กรุณาตั้งUsername:")
        code  =input("กรุณาตั้งPassword:")
        code1 =input("ยืนยันPassword  :")
        if (code1 == code):
            clear = lambda: os.system('cls')
            clear()
            print("{0:*<25}".format('*'))
            print("|     คุณกรอกรหัสถูกต้อง!   |\n" + "{0:*<25}".format('*')+"\n|  กรุณากรอกข้อมูลดังต่อไปนี้  |")
            print("{0:*<25}".format('*'))
            name = input("ชื่อ-นามสกุล  :")
            address_n = input("บ้านเลขที่    :")
            address_sw = input("หมู่         :")
            district_t = input("ตำบล       :")
            district_o = input("อำเภอ      :")
            city = input("จังหวัด      :")
            postal = input("รหัสไปรษณีย์  :")
            tel = input("เบอร์โทรศัพท์ :")
            c = conn.cursor()
            data = (users,code,name,address_n+"/"+address_sw+" ตำบล "+district_t+" อำเภอ "+district_o+" จังหวัด "+city+postal,tel,0,0,0,0)
            c.execute('INSERT INTO loan (Users,Pass,Name,Address,Tel,Year,Month,Day,Money) VALUES (?,?,?,?,?,?,?,?,?)',data)
            conn.commit()
            c.close()
            break;
        else:
            print("คุณกรอกรหัสผ่านไม่ถูกต้อง!\nกรุณากรอกใหม่อีกครั้ง")
            time.sleep(1.5)

def login():
    while(True):
        lcode = input("password: ")
        c = conn.cursor()
        c.execute(' SELECT * FROM loan WHERE Users = ?',lusers_l)
        result = c.fetchall()
        for x in result :
            if lcode == x[1]:
                while(True):
                    money = ["1,000","5,000","10,000","50,000"]
                    print('อ่านให้ระเอียดก่อนกู้ด้วยนะครับ\nรายการการกู้มีดังนี้\nกด1.1,000บาท\nกด2.5,000บาท\nกด3.10,000บาท\nกด4.50,000บาท\nกด5.ดูข้อมูลของคุณ')
                    num = int(input('กรุณาเลือก:'))
                    for i in range(5):
                        if num == i:
                            c = conn.cursor()
                            c.execute(' SELECT * FROM loan WHERE Users = ?',lusers_l)
                            ok = c.fetchall()
                            for x in ok:
                                if x[7] == 0:
                                    os.system('cls')
                                    print(" คุณได้เลือกกู้เงิน "+money[num-1]+"\n คุณจะเสียดอกเบี้ยร้อยละ "+str(num+1)+"%ต่อเดือน")
                                    lcode = input('กรุณาใส่ของคุณ password: ')
                                    c.execute(' SELECT * FROM loan WHERE Users = ?',lusers_l)
                                    result = c.fetchall()
                                    for x in result :
                                        if lcode == x[1]:
                                            yn = input("คุณต้องการกู้เงินจำนวน"+money[num-1]+"ใช่หรือไม่(y/n):")
                                            if yn == 'y':
                                                print("ระบบได้ทำการบันทึกเรียบร้อย\nจะมีทีมงานติดต่อท่านไป!")
                                                now = datetime.datetime.now()
                                                Y = "%d" % now.year
                                                M = "%d" % now.month
                                                D = "%d" % now.day
                                                data = (int(Y),int(M),int(D),money_d[num-1],lusers,)
                                                c.execute('''UPDATE loan SET Year = ?,Month = ?,Day = ?,Money = ? WHERE Users = ?''',data)
                                                conn.commit()
                                                c.close()
                                        else:
                                            print("รหัวผ่านคุณไม่ถูกต้องกรุณากรอกใหม่อีกครั้ง")
                                else:
                                    for i in range(4):
                                        c = conn.cursor()
                                        c.execute(' SELECT * FROM loan WHERE Users = ?',lusers_l)
                                        result = c.fetchall()
                                        for x in result :
                                            if money_d[i] == x[7]:
                                                f_date = date(x[4],x[5],x[6])
                                                l_date = l_date = date.today()
                                                delta = l_date - f_date
                                                numday = delta.days
                                                sum_1 = x[7]+((x[7]*(i+2)*numday)/30)
                                    print("คุณมีหนีในระบบจำนวน"+str(sum_1)+"บาท และไม่สามารถกู้ได้")
            else:
                print('รหัสผ่านไม่ถูกต้อง')
                

print("{0:*<25}".format('*'))
print("|   โปรแกรมพอมเจมส์เงินกู้   |\n|  กรุณาเลือกกดตัวเลขต่อไปนี้  |")
print("{0:*<25}".format('*'))
print("|     กด 1 สมัคร          |\n|     กด 2 ล็อกอิน         |\n|     กด 3 ออกจากโปรแกรม |")
print("{0:*<25}".format('*'))
yn = int(input('พิมพ์หมายเลข : '))
if yn == 1:
    inputdata()
elif yn == 2:
    while(True):
        lusers = input("Usersname: ")
        lusers_l = (lusers,)
        c = conn.cursor()
        c.execute(' SELECT * FROM loan WHERE Users = ? ',lusers_l)
        if c.fetchone():
            login()
            break;
        else:
            print("ไม่พบ Users ของคุณ")