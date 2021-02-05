
import os
choice = 0
fillename =''

def menu():
    global choice
    print('Menu \n 1.Open Calculator\n 2.Open Notepad\n 3.Exit ')
    choice = input('Select Menu : ')

def opentnotepad():
    filename = 'C:\\Windows\\SysWOW64\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\SysWOW64\\calc.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

while True:
    menu()
    if choice =='1':
        opencalculator()
    elif choice =='2':
        opentnotepad()
    else:
        break
 #############################แบบฝึกหัด 4.1############################################
from os import system,name
print('โปรแกรมร้านค้าออนไลน์')
print('-'*25)
choice = 0
sinka =[]
item = ['1.ยาHP ราคา 10 บาท','2.ยาMP ราคา 20 บาท','3.ยาชุบ ราคา 30 บาท','4.ยาม้า ราคา 40 บาท','5.เพิ่ม exp ราคา 50 บาท']
price =[10,20,30,40,50]
product =[0,0,0,0,0]
i = 0
x=1
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _=system('clear')
def menu():
    global choice
    print('1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.แสดงรายจำนวนสินค้าและราคาของสินค้าที่หยิบ\n4.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ :')
def opensinka():
    for i in range(5):
        x = int(input('เลือกไอเทม : '))
        if x == '1' or x==1:
            sinka.append('ยาHP')
        elif x == '2' or x== 2:
            sinka.append('ยาMP')
        elif x == '3' or x==3:
            sinka.append('ยาชุบ')
        elif x == '4' or x==4:
            sinka.append('ยาม้า')
        elif x == '5' or x==5:
            sinka.append('ยาเพิ่ม exp')
        i += 1
    print('')
def openlist():
    print('*'*25)
    print('รายการสินค้า')
    print('-'*25)
    for i in range(5):
        print(item[i])
    print('')
def showall():
    for i in sinka:
            if i =='ยาHP':
                product[0] +=1
            elif i =='ยาMP':
                product[1] +=1
            elif i =='ยาชุบ':
                product[2] +=1
            elif i =='ยาม้า':
                product[3] +=1
            elif i =='ยาเพิ่ม exp':
                product[4] +=1 
    productt = product[0]+product[1]+product[2]+product[3]+product[4]
    pricee = product[0]*10 +product[1]*20 +product[2]*30 +product[3]*40 +product[4]*50
    print('ไอเทมที่หยิบไปมีดังนี้')
    print('สินค้า-------จำนวน------ราคา')
    if product[0]!=0:
        print('1.ยาHP'+'       '+str(product[0])+'          '+str(product[0]*10))
    if product[1]!=0:
        print('2.ยาMP'+'       '+str(product[1])+'          '+str(product[1]*20))
    if product[2]!=0:
        print('3.ยาชุบ'+'       '+str(product[2])+'          '+str(product[2]*30))
    if product[3]!=0:
        print('4.ยาม้า'+'       '+str(product[3])+'          '+str(product[3]*40))
    if product[4]!=0:
        print('5.ยาเพิ่ม exp'+'  '+str(product[4])+'          '+str(product[4]*50))
    print('')
    print("รวม",'        ',str(productt),'      ',str(pricee))
    print('')
while True:
    menu()
    print('')
    if choice == "1":
        openlist()
    elif choice == "2":
        opensinka()
    elif choice == "3":
        showall()
    elif choice == "4":
        exit = input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n \n')
        if exit == 'y':
            break
        elif exit == 'n':
            continue
################################################################################
################################แบบฝึกหัด4.2#####################################
Dictionary = {
    'ability':'{0:<15}{1:<15}'.format('n.','ความสารมารถ'),
    'abroad' :'{0:<15}{1:<15}'.format('adv.','ต่างประเทศ'),
    'absent' :'{0:<15}{1:<15}'.format('adj.','ขาด'),
    'accept' :'{0:<15}{1:<15}'.format('v.','ยอมรับ'),
    'account':'{0:<15}{1:<15}'.format('n.','บัญชี'),
}
i = 5
def menu():
    global choice
    print('\nพจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม')
    choice = input('input choice : ')
def addword():
    word = input('พิมพ์คำศัพท์     : ')
    types = input('ชนิดของคำศัพท์(n.,v.,adj.,adv.): ')
    mean = input('ความหมาย     : ')
    Dictionary[word] = '{0:<15}{1:<15}'.format(types,mean)
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')
def showwords():
    print('-'*43,'\n         มีคำศัพท์ทั้งหมด',i,'คำ\n'+'-'*43)
    print('{0: <15}{1: <15}{2: <15}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for k,v in Dictionary.items():
        print('{0:<15}{1:<15}'.format(k,v))
def deleteword():
    remove = input('พิมพ์คำศัพท์ที่ต้องการลบ : ')
    x = input('ต้องการลบ '+remove+' ใช่หรือไม่ (y/n) :')
    if x == 'y':
        Dictionary.pop(remove)
        print('ลบ',remove,'เรียบร้อยแล้ว')
    elif x == 'n':
        print('')
while True:
    menu()
    if choice == "1":
        addword()
        i +=1
    elif choice == "2":
        showwords()
    elif choice == '3':
        deleteword()
        i -=1
    else:
        exitt = input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if exitt == 'y':
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
        elif exitt == 'n':
            continue
############################################################################################
##################################แบบฝึกหัด 4.3#############################################
import datetime
now = datetime.datetime.now()
name_s = []
pts_s = []
time_s = []
ht = []
def menu():
    for i in range(num):
        name = input('ป้อนชื่อ : ')
        pts = float(input('คะแนน :'))
        time =float(input('ระยะเวลาที่ใช้ : '))
        ht.append(pts/time)
        name_s.append(name)
        pts_s.append(pts)
        time_s.append(time)
    for i in range(num):
        j = i
        for j in range(num):
            if ht[i] > ht[j]:
                a,b,c,d = ht[i],name_s[i],pts_s[i],time_s[i]
                ht[i],name_s[i],pts_s[i],time_s[i] = ht[j],name_s[j],pts_s[j],time_s[j]
                ht[j],name_s[j],pts_s[j],time_s[j] = a,b,c,d

def show():
    print('Shotgun sunday training 2021')
    print('Condition : 1')
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print('{0: <10}{1: <10}{2: <10}{3: <16}{4: <15}{5: <15}{6: <10}'.format('No.','PTS','TIME','COMPETITER#Name','HIT FACTOR','STATE POINTS','STATE PERCENT'))
    for i in range(num):
        SPS = ht[i]/ht[0]*50
        SPT = SPS/(ht[0]/ht[0]*50)*100
        print('{0: <10}{1: <10}{2: <10}{3: <16}{4: <15}{5: <15}{6: <10}'.format(i+1,int(pts_s[i]),'%.2f'%time_s[i],name_s[i],'%.4f'%ht[i],'%.4f'%SPS,'%.2f'%SPT))

num = int(input("จำนวนคนยิง:"))
menu()
show()
##############################################################################################