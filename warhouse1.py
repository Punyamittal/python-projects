import pickle
def write():
    f=open('Warehouse_management.dat','wb')
    record=[]
    while True:
        Gid=int(input('Enter goods ID'))
        Gname=input('Enter goods name')
        Gamount=int(input('Enter goods amount'))
        Gcost=int(input('Enter goods cost'))
        Section=input('Enter your section')
        Gtime=input('Time the item will be stored in the warehouse')
        data=[Gid,Gname,Gamount,Gcost,Section,Gtime]
        ch=input('Do you want to enter another record :')
        if ch in 'nN':
            break
        pickle.dump(record,f)
        f.close()
def read():
    print('contents in a file')
    f=open('Warehouse_management.dat','rb')
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                print(i)
    except EOFError:
        f.close()
def append():
    f=open('Warehouse_management','rb+')
    rec=pickle.load(f)
    while True:
        Gid=int(input('Enter goods ID'))
        Gname=input('Enter goods name')
        Gamount=int(input('Enter goods amount'))
        Gcost=int(input('Enter goods cost'))
        Section=input('Enter your section')
        Gtime=input('Time the item will be stored in the warehouse')
        data=[Gid,Gname,Gamount,Gcost,Section,Gtime]
        ch=input('Do you want to enter another record :')
        if ch in 'nN':
            break
        f.seek(0)
        pickle.dump(rec,f)
        f.close
def search():
    def Gidsearch():
        f=open('Warehouse_management.dat','rb')
        s=pickle.load(f)
        print(s)
        found=0
        Gid=int(input('Enter the Gid to be searched'))
        for i in s:
            if i[0]==Gid:
                print(i)
                found=1
            if found==0:
                print('Record not found')
        f.close()
    def Gnamesearch():
        f=open('Warehouse_management.dat','rb')
        s=pickle.load(f)
        print(s)
        found=0
        nm=input('Enter the name to be searched')
        for i in s:
            if i[1]==nm:
                print(i)
                found=1
            if found==0:
                print('Record not found')
        f.close()
    def Sectionsearch():
        f=open('Warehouse_management.dat','rb')
        s=picle.load(f)
        print(s)
        found=0
        ss=input('Enter section name to be searched')
        for i in s:
            if i[4]==ss:
                print(i)
                found=1
            if found==0:
                print('Record not found')
            f.close()
    print('What do you want to search--(Gid,Gname,Section)')
    y=input()
    if y=='Gid':
        Gidsearch()
    if y=='Gname':
        Gnamesearch()
    if y=='Section':
        Sectionsearch()
def update():
    def updateGid():
        f=open('Warehouse_management','rb+')
        s=pickle.load(f)
        print(s)
        print()
        found=0
        Gid=int(input('Gid'))
        for i in s:
            if (i[0]==Gid):
                print(i)
                print('current ID is',i[0])
                i[0]=input('Enter new ID')
                found=1
                print(i)
            elif found==0:
                print('Record not found')
            else:
                f.seek(0)
                pickle.dump(s,f)
        f.close()
    def updateGname():
        f=open('Warehouse_management','rb+')
        s=pickle.load(f)
        print(s)
        print()
        found=0
        Gid=input('Gid')
        for i in s:
            if (i[0]==Gid):
                print(i)
                print('Current name is',i[1])
                i[1]=input('Enter new name')
                found=1
                print(i)
            elif found==0:
                print('Record not found')
            else:
                f.seek(0)
                pickle.dump(s,f)
        f.close()
    def updateGamount():
        f=open('Warehouse_management','rb+')
        s=pickle.load(f)
        print(s)
        print()
        found=0
        Gid=int(input('Gid'))
        for i in s:
            if (i[0]==Gid):
                print(i)
                print('current Gamount is',i[2])
                i[2]=input('Enter new Gamount')
                found=1
                print(i)
            elif found==0:
                print('Record not found')
            else:
                f.seek(0)
                pickle.dump(s,f)
        f.close()
    def updateGcost():
        f=open('Warehouse_management','rb+')
        s=pickle.load(f)
        print(s)
        print()
        found=0
        Gid=int(input('Gid'))
        for i in s:
            if (i[0]==Gid):
                print(i)
                print('current Cost is',i[3])
                i[3]=input('Enter new cost')
                found=1
                print(i)
            elif found==0:
                print('Record not found')
            else:
                f.seek(0)
                pickle.dump(s,f)
        f.close()         
    def updateSection():
        f=open('Warehouse_management','rb+')
        s=pickle.load(f)
        print(s)
        print()
        found=0
        Gid=int(input('Gid'))
        for i in s:
            if (i[0]==Gid):
                print(i)
                print('current Section is',i[4])
                i[4]=input('Enter new section')
                found=1
                print(i)
            elif found==0:
                print('Record not found')
            else:
                f.seek(0)
                pickle.dump(s,f)
        f.close()
    def updateGtime():
        f=open('Warehouse_management','rb+')
        s=pickle.load(f)
        print(s)
        print()
        found=0
        Gid=int(input('Gid'))
        for i in s:
            if (i[0]==Gid):
                print(i)
                print('current time is',i[5])
                i[5]=input('Enter new time')
                found=1
                print(i)
            elif found==0:
                print('Record not found')
            else:
                f.seek(0)
                pickle.dump(s,f)
        f.close()
    print('''What do you want to update
             1...Id
             2...Name
             3...Amount
             4...Cost
             5...Section
             6...Time''')
    z=int(input('Choose Option'))
    if z==1:
        updateGid()
    elif z==2:
        updateGname()
    elif z==3:
        updateGamount()
    elif z==4:
        updateGcost()
    elif z==5:
        updateSection()
    elif z==6:
        updateGtime()
    else:
        print('Invaild option')
    
        

        
        
        
