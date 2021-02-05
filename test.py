import datetime
now = datetime.datetime.now()
data = {}
i=0
x=0
def menu():
    for i in range(n):
        name = input('ป้อนชื่อ : ')
        pts = float(input('คะแนน :'))
        time =float(input('ระยะเวลาที่ใช้ : '))
        hf = (pts/time)
        data[name] = '{0:<10}{1:<19}{2:<10}'.format(str(time),str(pts),'%.4f'%hf)

def show():
    print('Shotgun sunday training 2021')
    print('Condition : 1')
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print('{0: <10}{1: <10}{2: <10}{3: <15}{4: <15}{5: <15}{6: <10}'.format('No.','PTS','TIME','COMPETITER#Name','HIT FACTOR','STATE POINTS','STATE PERCENT'))
    for k,v in data.items():
        print('{0: <10}{1: <10}{2: <10}'.format(i+1,k,v))