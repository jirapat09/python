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