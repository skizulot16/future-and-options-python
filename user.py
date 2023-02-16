import csv
class user:
    stocks=[]
    def __init__(self,username,passw):
        self.username=username
        self.passw=passw
        uf=open('new.csv','r')
        cr=csv.reader(uf)
        check=0
        for i in cr:
            if(i[0]==self.username):
                check+=1
                if(i[1]==self.passw):
                    check+=1
                    print("LOGINNED SUCCESFUULY")
            
        if(check==0):
            print('Username not found')
        if(check==1):
            print('Password invalid')
    def createuser(self):
        self.newuser=input('Username=')
        uf=open('new.csv','r')
        cr=csv.reader(uf)
        self.check=0
        for i in cr:
            if(i[0]==self.newuser):
                self.check+=1
        if(self.check==1):
            print('This username already exists')
            user.createuser(self)
        else:
            self.newpass=input('Password=')
            self.newbal=float(input("Initial balance="))
            uf=open('new.csv','a',newline='')
            cw=csv.writer(uf)
            cw.writerow([self.newuser,self.newpass,self.newbal])
        
u1=user('user2','pass2')
u1.createuser()