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