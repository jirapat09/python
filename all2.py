############################แบบฝึกหัด 2.1##########################
a = input('Input First Number \n')
b = input('Input Second Number\n')
print(a,'=',b ,':',a==b)
print(a,'>',b ,':',a>b)
print(a,'<',b ,':',a<b)
##################################################################
a = 60
b = 13
c = 0
c = a & b
print(c)
c = a | b
print(c)
c = a ^ b
print(c)
c = ~a
print(c)
c = a << 2
print(c)
c = a >> 2
print(c)
###########################แบบฝึก 2.2##############################
print('Day Converter Program')
a = int(input('Input number of Days -->'))
print(a,' Days --> Hour',a*24,'Hours')
print(a,' Days --> Minutes',a*1440,'Minutes')
print(a,' Days --> Seconds',a*86400,'Seconds') 
###################################################################
friend = ["jan","cream","phu","bam","aom","pee","bas","kong","da","james"]
friend[9] ="may"
friend[3] ="boat"
friend.append("dome")
friend.append("poondang")
friend.insert(1,"csa")
friend.insert(8,"ped")
friend.remove("aom")
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)

animal = {"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capibara","spider","wombat","penquin","cocodile"])
print(animal)
##########################แบบฝึก 2.3##################################
print("*"*25)
print("โปรแกรมหยิบของใส่ตะกร้า")
print("*"*25)
a=[]
for i in range(5) :
    b = input('สินค้าชิ้นที่ '+ str(i+1) +' คือ      ')
    a.append(b)
print("*"*25 ,"\n","สินค้าที่หยิบคือ")
print("*"*25)
print('1.',a[0])
print('2.',a[1])
print('3.',a[2])
print('4.',a[3])
print('5.',a[4])
print("*"*25)
#######################################################################
############################ แบบฝึก 2.4 ###############################
price = [25,30,45,55,60],[45,45,75,90,100],[60,70,110,130,140]
car = ["รถยนต์ 4 ล้อ","รถยนต์ 6 ล้อ","รถยนต์มากกว่า 6 ล้อ"]
print("โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์")
print("รถยนต์ 4 ล้อ        กด 1")
print("รถยนต์ 6 ล้อ        กด 2")
print("รถยนต์มากกว่า 6 ล้อ  กด 3")
a = int(input("เลือกประเภทยานภาหนะ :"))
print(car[a-1])
print("ลาดกระบัง --> บางบ่อ..."+str(price[a-1][0])+"...บาท")
print("ลาดกระบัง --> บางประกง..."+str(price[a-1][1])+"...บาท")
print("ลาดกระบัง --> พนัสนิคม..."+str(price[a-1][2])+"...บาท")
print("ลาดกระบัง --> บ้านบึง..."+str(price[a-1][3])+"...บาท")
print("ลาดกระบัง --> บางพระ..."+str(price[a-1][4])+"...บาท")
#######################################################################