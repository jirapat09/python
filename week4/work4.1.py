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