import csv
class user:
    stocks=[]
    def __init__(self):
        self.username=input('Username=')
        self.passw=input('password=')
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
            self.temp=0
            print('Do you want to 1.create new user or 2.try again? or 3.Exit')
            self.temp=int(input('Choice='))
            if(self.temp==1):
                user.createuser(self)
                
            elif(self.temp==2):
                user.__init__(self)
            else:
                print("THEEK HAI BHAI")
                exit()
        if(check==1):
            print('Password invalid Try again?')
            self.temp=(input('Choice(yes/no)='))
            if(self.temp=='yes'):
                user.__init__(self)
            else:
                print("THEEK HAI BHAI")
                exit()
            
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
            
#u1=user('user2','pass2')
#u1.createuser()