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