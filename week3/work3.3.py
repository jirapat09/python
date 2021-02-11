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