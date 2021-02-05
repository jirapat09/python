"""
print("เลือกเมนูเพื่อทำรายการ")
print("#"*25)
print("กด 1 เลือกเหมาจ่าย")
print("กด 2 เลือกจ่ายเพิ่ม")
choose = int(input(" "))
d = int(input("กรุณากรอกระยะทาง \n"))
if choose == 1 :
    if d <= 25 :
        print("ค่าใช้จ่าย รวมทั้งหมด 25 บาท")
    else :
        print("ค่าใช้จ่าย รวมทั้งหมด 55 บาท")
if choose == 2 :
    if d <= 25 :
        print("ค่าใช้จ่าย รวมทั้งหมด 25 บาท")
    else :
        print("ค่าใช้จ่าย รวมทั้งหมด 80 บาท")

n = int(input("กรอกจำนวนครั้งที่รับค่า \n"))
i =1
a =0
while(i<=n) :
    N =int(input("กรอกตัวเลข  "))
    i +=1
    a=a+N
print("ผลรวมทั้งหมด "+str(a))

print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
print("*"*25)
i = 1
a = []
x = 0
while(True):
    b = str(input("อาหารโปรดลำดับที่ "+str(i)+"ของคุณคือ  "))
    if (b == "exit"):
        break
    a.append(b)
    i+=1
print("อาหารสุดโปรดของคุณมีดังนี้ " ,end="\n")
while(True):
    print(str(x+1)+".",a[x]+ " ",end="\n")
    x += 1

a=[]
while True:
    b = input('---ครัวว้าวซ่าแซ่บ---\n เพิ่ม [a]\n แสดง[s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b=='a':
        c = input('ป้อนรายการลูกค้า(โต๊ะ:ชื่อ:เบอร์โทร)\n')
        a.append(c)
        print('\n****ข้อมูลได้เข้าสู่ระบบแล้ว****\n')
    elif b=='s':
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('โต๊ะ','ชื่อ','เบอร์โทร'))
        for d in a:
            e=d.split(":")
            print('{0[0]:<6} {0[1]:<10} {0[2]:<10}'.format(e))
            continue
    elif b=='x':
        break
print('ทำคำสั่งถัดไป')

n = int(input("Please enter student : "))
print("-"*25)
stu = [0,0,0,0,0,0]
score = ["90-100 :","80-89  :","70-79  :","60-69  :","50-59  :","0-49   :"]
i=0
while (i<=n):
    x = int(input("Please enter score : "))
    if x >= 90 and x <= 100 :
        stu[0] += 1
    elif x >= 80 and x <= 89 :
        stu[1] += 1
    elif x >=70 and x <=79 :
        stu[2] += 1
    elif x >=60 and x <=69 :
        stu[3] += 1
    elif x >=50 and x <=59 :
        stu[4] += 1
    elif x >=0 and x <=49 :
        stu[5] += 1
    i+=1
i=0
while (i<6):
    print(score[i],"*"*stu[i])
    i+=1
"""