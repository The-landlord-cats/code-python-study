import tkinter as tk###加载交互式页面设计
from tkinter import messagebox###加载提示框
import math
import pymysql
import matplotlib.pyplot as plt
import re
from PIL import Image

def Loading(user,password,py,window):
    Load_user = user 
    Load_password = password
    f = open('load.txt','r')# 从账户文档中读取信息
    dataText = f.readlines()
    f.close()
    n = len(dataText)
    key = 0
    for j in range(0,n,1):# 对比输入信息与文档信息，若一致，则成功登陆，否则可破解登陆
        listTemp1 = dataText[j].split(' ')
        Txt_user = listTemp1[0]
        Txt_passwd = listTemp1[1].replace('\n','')
        if Load_user == Txt_user and Load_password == Txt_passwd:
            key = 1
    if key == 1:
        messagebox.askquestion(title='成功', message="欢迎登录虚拟基地信息可视化工程！")
        Child_window(window)
    else:
        messagebox.askquestion(title='失败', message="账号密码错误，正在进行破解！")
        n = len(dataText)
        key = 0
        for j in range(0,n,1):# 再次对比，若用户名输入有误，则提示无法破解
            listTemp1 = dataText[j].split(' ')
            Txt_user = listTemp1[0]
            Txt_passwd = listTemp1[1].replace('\n','')
            if Load_user == Txt_user:
                key = 1
                break  
        if key == 0:
            messagebox.askquestion(title='失败', message="账号错误，无法破解！")                  
        else:
            listNum = ['0','1','2','3','4','5','6','7','8','9']
            numpy = 0
            for i in listNum:
                for j in listNum:
                    for k in listNum:
                        py.insert(numpy, i+j+k)
                        numpy = numpy+1
                        if i+j+k == Txt_passwd:
                            messagebox.askquestion(title='成功', message="密码为"+i+j+k+"  欢迎登录虚拟基地信息可视化工程！") 
                            Child_window(window)

def getData():
    f=open('table.html', 'r')
    webdata=f.read()
    f.close()
    f = open('DataBase.txt', 'w')
    tables=re.findall(r'<table.*?>(.*?)</table>', webdata, re.S)
    for table in tables:
        rows = re.findall(r'<tr.*?>(.*?)</tr>', table, re.S)    
        for row in rows:
            tds = re.findall(r'<td.*?>(.*?)</td>', row, re.S)
            if '解放军' in tds[0] or '台湾' in tds[0] or '美军' in tds[0] or '地区' in tds[0]:
                continue
            else:
                f.write(','.join(tds))
                f.write(','+str(tables.index(table))+'\n')
    f.close()
    messagebox.askquestion(title='数据获取成功', message="数据获取成功，请打开DataBase.txt查看！")

def saveData():
    messagebox.askquestion(title='提示', message="数据保存前要先清空数据库，防止数据重复！")
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='base')
    cursor = conn.cursor()
    f = open('DataBase.txt','r')
    list1 = f.readlines()
    distance = 0
    for i in range(0, len(list1)):
        listTemp = list1[i].split(',')
        str1=''
        str2='\''
        distance = 6371*math.acos(math.cos(float(listTemp[2]))*math.cos(39)*math.cos(float(listTemp[1])-116)+math.sin(float(listTemp[2]))*math.sin(39))
        cursor.execute('INSERT INTO basic(Name,Longitude,Latitude,Distance,Type) VALUES(\''+listTemp[0]+'\',\''+listTemp[1]+'\',\''+listTemp[2]+'\',\''+str(distance)+'\',\''+listTemp[3].replace('\n','')+'\');')
        conn.commit()
    f.close()
    cursor.close()
    conn.close()
    messagebox.askquestion(title='数据保存成功', message="数据保存成功，可以进行加解密、操作、可视化！")

def cleanData():
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='base')
    cursor = conn.cursor()
    #cursor.execute('DELETE FROM basic;')
    #conn.commit()
    cursor.execute('truncate table basic;')#重置自增属性，让ID字段从1重新开始计数
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.askquestion(title='数据清空成功', message="数据清空成功，可以保存新数据！")

def seeData():
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='base')
    cursor = conn.cursor()
    sql = 'select * from basic'
    cursor.execute(sql)
    records = cursor.fetchall()
    conn.commit()
    cursor.close() 
    conn.close()
    img = plt.imread("china.jpg")#读取图像
    fig,ax = plt.subplots()#它是用来创建总画布/figure“窗口”的，有figure就可以在上边（或其中一个子网格/subplot上）作图了，（fig：是figure的缩写）。
    ax.imshow(img,extent=[60,160,0,60])
    Base = []
    for record in records:
        temp = []
        temp.append(record[2])#经度
        temp.append(record[3])#纬度
        temp.append(record[5])#基地类型
        Base.append(temp)
    for base in Base:
        if int(base[2]) == 0:
            plt.plot(base[0],base[1],'ro')
        elif int(base[2]) == 1:
            plt.plot(base[0],base[1],'bo')
        elif int(base[2]) == 2:
            plt.plot(base[0],base[1],'go')
    
    plt.scatter(116,39,marker='p',s=300,c='yellow') 
    plt.show()        

def gcd(x,y):
    if x<y:
        x,y=x,y
    R=x%y
    while R!=0:
        x=y
        y=R
        R=x%y
    return y

def encryptionData():
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='base')
    cursor = conn.cursor()
    sql = 'select * from basic'
    cursor.execute(sql)
    records = cursor.fetchall()
    conn.commit()
    cursor.close() 
    conn.close()
    f = open('EDData.txt', 'w')
    for record in records:
        keyData = gcd(int(record[2]),int(record[3]))
        keyX = int(int(record[2])/keyData)
        keyY = int(int(record[3])/keyData)
        f.write(str(keyData)+' '+str(keyX)+' '+str(keyY))
        f.write('\n')
    f.close()
    messagebox.askquestion(title='数据加密（公约数）成功', message="数据加密（公约数）成功，请查看EDData.txt文档！")

def back(x,y,z):
    num1 = x*y
    num2 = x*z
    return num1,num2

def decryptionData():
    f = open('EDData.txt','r')
    dataText = f.readlines()
    f.close()
    n = len(dataText)
    f = open('EDData.txt', 'w')
    for j in range(0,n,1):
        listTemp1 = dataText[j].split(' ')
        x = int(listTemp1[0])
        y = int(listTemp1[1])
        z = int(listTemp1[2].replace('\n',''))
        a,b = back(x,y,z)
        f.write(str(a)+' '+str(b))
        f.write('\n')
    f.close()
    messagebox.askquestion(title='数据解密（公约数）成功', message="数据解密（公约数）成功，请查看EDData.txt文档！")

def encod2dec(s):
    a = []
    for i in s:
        by = bytes(i, encoding='utf8') #b'\xe6\x98\x8e'
        for j in by:      
            a = a + [j]
    return a
def images(t,Ttype):
    img = Image.open("歼20."+Ttype).convert("RGB")
    #img.putpixel((0,0),(len(t),0,0))
    img.putpixel((0,0),(100,0,0))
    #print(len(t))
    #for i in range(len(t)):
    for i in range(100):
        img.putpixel((1,i),(t[i],0,0))   
    img.convert('RGB')
    img.save("test."+Ttype)

def encryptionData_png(Ttype):
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='base')
    cursor = conn.cursor()
    sql = 'select * from basic'
    cursor.execute(sql)
    records = cursor.fetchall()
    conn.commit()
    cursor.close() 
    conn.close()
    s = ''
    for record in records:
        for i in range(1,len(record)):
            s = s+str(record[i])+' '
        s = s+'\n'
    t = encod2dec(s)
    images(t,Ttype)
    img1 = Image.open("歼20."+Ttype).convert("RGB")
    img2 = Image.open("test."+Ttype).convert("RGB")
    plt.subplot(121), plt.imshow(img1)
    plt.title('old Image')
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.title('new Image')
    plt.show()

def dec2encod(s):
    t = b''
    for i in s:
        t = t + bytes([i[0]])
    return t.decode('utf8')  

def decryptionData_png(Ttype):
    img = Image.open("test."+Ttype)
    c = []
    n = img.getpixel((0,0))
    for i in range(n[0]):
        c.append(img.getpixel((1,i)))
    messagebox.askquestion(title='数据解密成功'+Ttype, message="数据解密成功！\n"+dec2encod(c))

def FindData(name):
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='base')
    cursor = conn.cursor()
    sql = 'select * from basic'
    cursor.execute(sql)
    records = cursor.fetchall()
    conn.commit()
    cursor.close() 
    conn.close()
    for record in records:
        if name == record[1]:
            messagebox.askquestion(title='查找成功', message="数据查找成功！\n"+str(record))
            return
    messagebox.askquestion(title='查找失败', message="数据查找失败！")

def SortData():
    conn = pymysql.connect(host='localhost',user='root',passwd='root',db='base')
    cursor = conn.cursor()
    sql = 'select * from basic'
    cursor.execute(sql)
    records = cursor.fetchall()
    conn.commit()
    cursor.close() 
    conn.close()
    records = list(records)
    k = -1
    for i in range(0,len(records),1):
        if records[i][5] == 0:
            continue
        else:
            k = i
            break
    records = records[k:]           
    n = len(records)
    for i in range(k,n-1,1):         
        for j in range(0,n-1-i,1):   
             if records[j][4]>records[j+1][4]:
                 records[j],records[j+1]=records[j+1],records[j]
    f = open('SordData.txt', 'w')
    for record in records:
        f.write(str(record))
        f.write('\n')
    f.close()
    messagebox.askquestion(title='数据排序成功', message="数据排序成功，请查看SortData.txt文档！")

def destroy(window):
    window.destroy()

def EDData():
    EDData_window = tk.Tk()
    EDData_window.title('虚拟基地信息可视化工程')
    EDData_window.geometry("1000x200")          
    tk.Label(EDData_window, text='虚拟基地信息可视化工程--信息加解密', font=('黑体', 20)).place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    btn1 = tk.Button(EDData_window, text='加密数据-公约数', font=('黑体', 15), width=15, height=1, command=encryptionData)
    btn1.place(relx=0.12, rely=0.4, anchor=tk.CENTER)
    btn2 = tk.Button(EDData_window, text='解密数据-公约数', font=('黑体', 15), width=15, height=1, command=decryptionData)
    btn2.place(relx=0.37, rely=0.4, anchor=tk.CENTER)
    btn3 = tk.Button(EDData_window, text='加密数据-png', font=('黑体', 15), width=15, height=1, command=lambda:encryptionData_png('png'))
    btn3.place(relx=0.62, rely=0.4, anchor=tk.CENTER)
    btn4 = tk.Button(EDData_window, text='解密数据-png', font=('黑体', 15), width=15, height=1, command=lambda:decryptionData_png('png'))
    btn4.place(relx=0.87, rely=0.4, anchor=tk.CENTER)
    btn5 = tk.Button(EDData_window, text='加密数据-jpg', font=('黑体', 15), width=15, height=1, command=lambda:encryptionData_png('jpg'))
    btn5.place(relx=0.12, rely=0.7, anchor=tk.CENTER)
    btn6 = tk.Button(EDData_window, text='解密数据-jpg', font=('黑体', 15), width=15, height=1, command=lambda:decryptionData_png('jpg'))
    btn6.place(relx=0.37, rely=0.7, anchor=tk.CENTER)
    btn7 = tk.Button(EDData_window, text='退出加解密', font=('黑体', 15), width=15, height=1, command=lambda:destroy(EDData_window))
    btn7.place(relx=0.62, rely=0.7, anchor=tk.CENTER)
    EDData_window.mainloop()

def OpData():
    OpData_window = tk.Tk()
    OpData_window.title('虚拟基地信息可视化工程')
    OpData_window.geometry("1000x200")         
    tk.Label(OpData_window, text='虚拟基地信息可视化工程--数据操作', font=('黑体', 20)).place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    tk.Label(OpData_window, text='基地名称：  ', font=('黑体', 15)).place(relx=0.2, rely=0.45, anchor=tk.CENTER)
    name = tk.Entry(OpData_window, font=17, width=15)
    name.place(relx=0.4, rely=0.45, anchor=tk.CENTER)  
    btn1 = tk.Button(OpData_window, text='按名字查找', font=('黑体', 15), width=15, height=1, command=lambda:FindData(name.get()))
    btn1.place(relx=0.6, rely=0.45, anchor=tk.CENTER)
    btn2 = tk.Button(OpData_window, text='按距离排序', font=('黑体', 15), width=15, height=1, command=SortData)
    btn2.place(relx=0.85, rely=0.45, anchor=tk.CENTER)
    btn7 = tk.Button(OpData_window, text='退出数据操作', font=('黑体', 15), width=15, height=1, command=lambda:destroy(OpData_window))
    btn7.place(relx=0.2, rely=0.7, anchor=tk.CENTER)
    OpData_window.mainloop()


def Main_window():
    window = tk.Tk()####设定主窗口
    window.title('虚拟基地信息可视化工程')####设定主窗口名称（交互式页面左上角）
    window.geometry("800x200")#####设定软件窗口大小800*200像素
    ####font为字体设置，黑子，20号字，place设置位置
    ####relx为控件中心点在整体页面横坐标的百分比，rely为控件中心点在整体页面纵坐标的百分比
    ####anchor设置控件显示为居中
    ####Label为文本           
    tk.Label(window, text='虚拟基地信息可视化工程', font=('黑体', 20)).place(relx=0.35, rely=0.1, anchor=tk.CENTER)
    tk.Label(window, text='用户名：', font=('黑体', 15)).place(relx=0.2, rely=0.35, anchor=tk.CENTER)
    tk.Label(window, text='密码：  ', font=('黑体', 15)).place(relx=0.2, rely=0.55, anchor=tk.CENTER)
    ####Entry为输入框
    user = tk.Entry(window, font=17, width=15)
    user.place(relx=0.4, rely=0.35, anchor=tk.CENTER)
    password = tk.Entry(window, font=17, width=15)
    password.place(relx=0.4, rely=0.55, anchor=tk.CENTER)
    ####Listbox为信息显示框
    py = tk.Listbox(window, font=15, width=20, height=8)
    py.place(relx=0.80, rely=0.50, anchor=tk.CENTER)
    ####Button为按钮
    ####text为按钮上的文字，width为按钮宽度，height为按钮高度，command为按钮的触发函数
    btn1 = tk.Button(window, text='登  录', font=('黑体', 15), width=11, height=1, command=lambda:Loading(user.get(),password.get(),py,window))
    btn1.place(relx=0.2, rely=0.86, anchor=tk.CENTER)
    window.mainloop()

def Child_window(window):
    window.destroy()
    Child_window = tk.Tk()
    Child_window.title('虚拟基地信息可视化工程')
    Child_window.geometry("1000x200")       
    tk.Label(Child_window, text='虚拟基地信息可视化工程', font=('黑体', 20)).place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    btn1 = tk.Button(Child_window, text='获取数据', font=('黑体', 15), width=11, height=1, command=getData)
    btn1.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
    btn2 = tk.Button(Child_window, text='保存数据', font=('黑体', 15), width=11, height=1, command=saveData)
    btn2.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
    btn3 = tk.Button(Child_window, text='加解密数据', font=('黑体', 15), width=11, height=1, command=EDData)
    btn3.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
    btn4 = tk.Button(Child_window, text='操作数据', font=('黑体', 15), width=11, height=1, command=OpData)
    btn4.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
    btn5 = tk.Button(Child_window, text='清空数据', font=('黑体', 15), width=11, height=1, command=cleanData)
    btn5.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
    btn6 = tk.Button(Child_window, text='数据可视化', font=('黑体', 15), width=11, height=1, command=seeData)
    btn6.place(relx=0.4, rely=0.8, anchor=tk.CENTER)
    btn7 = tk.Button(Child_window, text='退出程序', font=('黑体', 15), width=11, height=1, command=lambda:destroy(Child_window))
    btn7.place(relx=0.6, rely=0.8, anchor=tk.CENTER)
    Child_window.mainloop()

Main_window()
