import os
import sqlite3
import datetime
from datetime import date
import time
import webbrowser

conn = sqlite3.connect(r"D:\Jirapat_python\Project\Project.db")
money_d = [1000,5000,10000,50000]

def forget():
    print("กรุณาติดต่อไปที่ เฟสบุ๊ค -->EDcom17สุดหล่อ<--")
    time.sleep(5)
    webbrowser.open('https://www.facebook.com/100555015146142/photos/a.100590178475959/243002877568021/')

def pay():
    os.system('cls')
    while(True):
        print("{0:*<25}".format('*'))
        print("|        💸จ่ายหนี้         |\n"+"{0:*<25}".format('*')+"\n กด 1 จ่ายต้นจ่ายดอก\n กด 2 จ่ายดอก\n กด 3 ออก")
        print("{0:*<25}".format('*'))
        pay_n = int(input("พิมพ์หมายเลข:"))
        if pay_n == 1:
            c = conn.cursor()
            c.execute(' SELECT * FROM loan WHERE Users = ? ',lusers_l)
            result = c.fetchall()
            for x in result:
                if x[7]!=0:
                    for i in range(4):
                        if money_d[i] == x[7]:
                            f_date = date(x[4],x[5],x[6])
                            l_date = l_date = date.today()
                            delta = l_date - f_date
                            numday = delta.days
                            sum_1 = x[7]+((x[7]*(i+2)*numday)/30)
                            print("จำนวนเงินที่คุณต้องจ่ายคือ "+"%.2f"%sum_1+"บาท")
                            comfirm = input("หากต้องการจ่ายกรุณาพิมพ์คำว่า-->ยืนยัน<--: ")
                            if comfirm == "ยืนยัน":
                                print("กรุณาโอนเงินมาที่พร้อมเพร์ 0927403227\nเมื่อโอนแล้วกรุณาเก็บหลักฐานแล้วส่งมาที่เฟสบุ๊กEDcom17สุดหล่อ")
                                time.sleep(6)
                                webbrowser.open('https://www.facebook.com/EDcom17%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%AB%E0%B8%A5%E0%B9%88%E0%B8%AD-100555015146142/')
                                print("ถ้าแอดมินตรวจสอบเสร็จแล้วจะมี sms ส่งไปถึงคุณ")
                                break;
                            else:
                                print("คุณพิมพ์ไม่ถูกต้อง!")
                else:
                    print("คุณไม่มีหนี้ครับ -_-")
        elif pay_n == 2:
            c = conn.cursor()
            c.execute(' SELECT * FROM loan WHERE Users = ? ',lusers_l)
            result = c.fetchall()
            for x in result:
                if x[7]!=0:
                    for i in range(4):
                        if money_d[i] == x[7]:
                            f_date = date(x[4],x[5],x[6])
                            l_date = l_date = date.today()
                            delta = l_date - f_date
                            numday = delta.days
                            sum_p =(x[7]*(i+2)*numday)/30
                            print("จำนวนเงินที่คุณต้องจ่ายคือ "+"%.2f"%sum_p+"บาท")
                            comfirm = input("หากต้องการจ่ายกรุณาพิมพ์คำว่า-->ยืนยัน<--: ")
                            if comfirm == "ยืนยัน":
                                print("กรุณาโอนเงินมาที่พร้อมเพร์ 0927403227\nเมื่อโอนแล้วกรุณาเก็บหลักฐานแล้วส่งมาที่เฟสบุ๊กEDcom17สุดหล่อ")
                                time.sleep(6)
                                webbrowser.open('https://www.facebook.com/EDcom17%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%AB%E0%B8%A5%E0%B9%88%E0%B8%AD-100555015146142/')
                                print("ถ้าแอดมินตรวจสอบเสร็จแล้วจะมี sms ส่งไปถึงคุณ")
                                break;
                            else:
                                print("คุณพิมไม่ถูกต้อง!")
                                break
                else:
                    print("คุณไม่มีหนี้ครับ -_-")
        else:
            break

def show():
    c = conn.cursor()
    c.execute(' SELECT * FROM loan WHERE Users = ? ',lusers_l)
    result = c.fetchall()
    print("{0:*<25}".format('*'))
    print("{0: <30}{1}".format('|  ข้อมูลส่วนตัวของคุณ','|'))
    print("{0:*<60}".format('*'))
    for x in result:
        print("Usersname :"+x[0]+"\nPassword  :"+x[1]+"\nชื่อ-นามสกุล :"+x[2]+"\nที่อยู่       :"+x[3]+"เบอร์โทรศัพท์ :"+x[8])
        
        print("{0:*<60}".format('*'))
        if x[7]!=0:
            for i in range(4):
                if money_d[i] == x[7]:
                    f_date = date(x[4],x[5],x[6])
                    l_date = l_date = date.today()
                    delta = l_date - f_date
                    numday = delta.days
                    sum_1 = x[7]+((x[7]*(i+2)*numday)/30)
                    sum_2 = (x[7]*(i+2)*numday)/30
            print("|คุณติดหนีสินทั้งหมด"+"%.2f"%sum_1+"บาท   |\n|เงินต้นจำนวน:"+str(x[7])+"บาท        |\n|เงินดอกเบี้ยจำนวน:"+"%.2f"%sum_2+"บาท |")
            print("{0:*<27}".format('*'))
            yn = input("คุณต้องการใช้หนึหรือไม่(y/n):")
            if yn == 'y':
                pay()
        else:
            print("{0:*<25}".format('*'))
            print("{0:*<30}{1}".format('|********คุณไม่มีหนี้','|'))
            print("{0:*<25}".format('*'))

def inputdata():
    while(True):
        os.system('cls')
        print("{0:*<25}".format('*'))
        print("|  📝กรุณากรอกข้อมูลต่อไปนี้  |\n|   ***ข้อมูลจริงเท่านั้น***  |")
        print("{0:*<25}".format('*'))
        users =input("กรุณาตั้งUsername:")
        users_l = (users,)
        c = conn.cursor()
        c.execute(' SELECT * FROM loan WHERE Users = ? ',users_l)
        if c.fetchone():
            print("Username นี้มีผู้ใช้แล้ว!")
            time.sleep(1)
        else:
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
                try:
                    tel = int(input("เบอร์โทรศัพท์ :"))        
                except :
                    print('หมายเลขโทรศัพท์ห้ามกรอกตัวอักษร')
                    time.sleep(1.5)
                    continue
                c = conn.cursor()
                data = (users,code,name,address_n+"/"+address_sw+" ตำบล "+district_t+" อำเภอ "+district_o+" จังหวัด "+city+postal,"0"+str(tel),0,0,0,0)
                c.execute('INSERT INTO loan (Users,Pass,Name,Address,Tel,Year,Month,Day,Money) VALUES (?,?,?,?,?,?,?,?,?)',data)
                conn.commit()
                c.close()
                print('สมัครเสร็จสิ้น')
                break
            else:
                print("คุณกรอกรหัสผ่านไม่ถูกต้อง!\nกรุณากรอกใหม่อีกครั้ง")
                time.sleep(1.5)

def login():
    pomm = 0
    while(pomm == 0):
        lcode = input("password: ")
        c = conn.cursor()
        c.execute(' SELECT * FROM loan WHERE Users = ?',lusers_l)
        result = c.fetchall()
        for x in result :
            if lcode == x[1]:
                while(pomm == 0):
                    money = ["1,000","5,000","10,000","50,000"]
                    print("{0:*<26}".format('*'))
                    print('|อ่านให้ระเอียดก่อนกู้ด้วยนะครับ |\n' +"{0:*<26}".format('*')+'\n| รายการการกู้มีดังนี้ \t\t|\n| กด 1.1,000บาท \t  |\n| กด 2.5,000บาท \t  |\n| กด 3.10,000บาท \t  |\n| กด 4.50,000บาท\t  |')
                    print("{0:*<26}".format('*'))
                    print('| กด 5.ดูข้อมูลของคุณ  \t      |\n| กด 6.logout  \t\t  |')
                    print("{0:*<26}".format('*'))
                    num = int(input('กรุณาเลือก:'))
                    for i in range(5):
                        if num == i:
                            c = conn.cursor()
                            c.execute(' SELECT * FROM loan WHERE Users = ?',lusers_l)
                            ok = c.fetchall()
                            for x in ok:
                                if x[7] == 0:
                                    os.system('cls')
                                    print("{0:*<29}".format('*'))
                                    print("|     คุณได้เลือกกู้เงิน "+money[num-1]+"    |"+"\n|คุณจะเสียดอกเบี้ยร้อยละ "+str(num+1)+"%ต่อเดือน|")
                                    print("{0:*<29}".format('*'))
                                    lcode = input('กรุณาใส่ password ของคุณ :')
                                    print("{0:*<29}".format('*'))
                                    c.execute(' SELECT * FROM loan WHERE Users = ?',lusers_l)
                                    result = c.fetchall()
                                    for x in result :
                                        if lcode == x[1]:
                                            yn = input("คุณต้องการกู้เงินจำนวน"+money[num-1]+"ใช่หรือไม่\n(y/n):")
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
                                                time.sleep(5)
                                        else:
                                            print("รหัสผ่านคุณไม่ถูกต้องกรุณากรอกใหม่อีกครั้ง")
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
                                    print("คุณมีหนีในระบบจำนวน"+"%.2f"%sum_1+"บาท และไม่สามารถกู้เพิ่มได้")
                                    yn = input("คุณต้องการใช้หนึหรือไม่(y/n):")
                                    if yn == 'y':
                                        pay()
                                        pomm = 1
                    if num == 5:
                        show()
                    elif num == 6:
                        yn = input("คุณต้องการออกใช่หรือไม่(y/n): ")
                        if yn == "y":
                            pomm = 1
            else:
                print('รหัสผ่านไม่ถูกต้อง')
                yn = input("คุณลืมรหัสผ่านหรือใช่หรือไม่(y/n): ")
                if yn == 'y':
                    forget()
                    pomm = 1
 
while(True):
    print("{0:*<25}".format('*'))
    print("| 😀โปรแกรมพอมเจมส์เงินกู้😀 |\n|  กรุณาเลือกกดตัวเลขต่อไปนี้  |")
    print("{0:*<25}".format('*'))
    print("|  📝กด 1 สมัคร           |\n|  🔐กด 2 ล็อกอิน          |\n|  ❌กด 3 ออกจากโปรแกรม  |")
    print("{0:*<25}".format('*'))
    yn = int(input('พิมพ์หมายเลข : '))
    if yn == 1:
        inputdata()
    elif yn == 2:
        while(True):
            os.system('cls')
            print("{0:*<25}".format('*'))
            print("|       🔐login          |")
            print("{0:*<25}".format('*'))
            lusers = input("Usersname: ")
            lusers_l = (lusers,)
            c = conn.cursor()
            c.execute(' SELECT * FROM loan WHERE Users = ? ',lusers_l)
            if c.fetchone():
                login()
                break
            else:
                print("ไม่พบ Users ของคุณ")
    else:
        k = input("คุณต้องการออกใช่หรือไม่(y/n): ")
        if k == 'y':
            break