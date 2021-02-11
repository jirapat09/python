num = 0
sinka = []
cost = []
class shop:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def showshop(self):
        print(i+1,".",self.name,self.price,"บาท")
    def show():
        print('{0:*<10}{1:*<10}{2:*<10}'.format('*',"ครัวฟ้าผ่า","*"))
        print("    แสดงรายการสินค้า [a]\n    เพิ่มรายการสินค้า[s]\n    ออกจากระบบ[x]\n"+'*'*27)

while True:
    shop.show()
    menu = input("กรุณาเลือกคำสั่ง:  ")
    if menu == 'a':
        for i in range(num):
            x = shop(sinka[i],cost[i])
            x.showshop()
    if menu == 's':
        while True:
            print("เพิ่มรายการสินค้าหากต้องการยกเลิกกรอก exit")
            n = input("เพิ่มชื่อสินค้า:  ")
            if n == 'exit':
                shop.show()
            else:
                sinka.append(n)
                c = input("เพิ่มราคาของ"+n+" :  ")
                cost.append(c)
                print("ทำรายการเสร็จสิน")
                num +=1
                choose = input("ต้องการเพิ่มสินค้าอีกหรือไม่(y/n): ")
                if choose == 'n':
                    break
    if menu == 'x':
        choose = input("ต้องการเพิ่มสินค้าอีกหรือไม่(y/n): ")
        if choose == 'y':
            break
        else:
            continue