#####5.1
print('-'*25,'แนะนำตัว','-'*25)
name,sex,year,department,province = input('ชื่อ-สกุล:เพศ:ชั้นปี:สาขา:จังหวัด     ').split(':')
class nisit :
    def __init__(self,name,sex,year,department,province):
        self.name = name
        self.sex = sex
        self.year = year
        self.department = department
        self.province = province

    def showme(self):
        if sex == 'ชาย':
            print('สวัสดีครับ ผมชื่อ '+self.name,'นักศึกษาชั้นปีที่ '+self.year,'สาขา'+self.department,'จังหวัด'+self.province)
        elif sex == 'หญิง':
            print('สวัสดีค่ะ หนูชื่อ '+self.name,'นักศึกษาชั้นปีที่ '+self.year,'สาขา'+self.department,'จังหวัด'+self.province)

x = nisit(name,sex,year,department,province)
x.showme()
#####5.2
class price :
    def __init__(self,name,sinka,cost,num):
        self.name = name
        self.sinka = sinka
        self.cost = cost
        self.num = num

    def add(self):
        sinka = input('เพิ่มชื่อสินค้า :')
        cost = input('เพิ่มราคาสินค้า :')
        
    def menu(self):
        print('แสดงรายการสินค้า [a]\nเพิ่มรายการสินค้า [s]\nออกจากระบบ [x]')
        x =input('กรุณาเลือกคำสั่ง : ')
        if x == 'a':
            