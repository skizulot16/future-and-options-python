from user import *
from stockcode import *
username=input('Username=')
password=input('Password=')
newuser=user(username,password)




class drivercode:
    list_of_players={}
    def __init__(self,userobj,l_o_s):
        print('''==========WELCOME TO BULLS BOARD===============
Games available:
1.SABSE BADA KHILADI (all stocks)
2.BADI MACHLI (share price>Rs.1000)
3.THODA RISK < THODA ISHQ (share price-[100,999])
4.RISK HAI TOH ISHQ HAI (penny stocks<Rs.100)''')
        self.user_ch=int(input('Whats your call?'))
        self.userobj=userobj
        self.l_o_s=l_o_s
        if self.user_ch==1:
            drivercode.gameone(self)
        elif self.user_ch==2:
            pass
            #drivercode.gametwo()
        elif self.user_ch==3:
            pass
            #drivercode.gamethree()
        elif self.user_ch==4:
            pass
            #drivercode.gamefour()
    def gameone(self):
        print('''SABSE BADA KHILADI (all stocks)
        Intructions:
        1.Entry Fee Rs.2000
        2.Prize Money (1st.Rs.3500 2nd.Rs.2500 3rd. Rs.2000)
        3.Read all scheme related documents carefully
        To join, press 1, or any other key to go back''')
        self.user_ch=int(input('Choice='))
        if(self.user_ch==1):
            if(self.userobj.getbalance()<2000):
                print('Insufficient Funds! Add money now? 1.addMoney 2.Exit ')
                self.option=int(input('Enter Choice='))
                if(self.option==1):
                    self.addmoney=float(input('Amount='))
                    self.userobj.changebal(self.addmoney)
                    drivercode.gameone(self)
                else:
                    exit()
            else:
                self.userobj.changebal(-2000)
                self.bullchips=10000
                for stock in self.l_o_s:
                    print(stock.name,stock.iprice)
                print('BULLCHIPS OWNED:',self.bullchips)
                self.counter=True
                while(self.counter==True):
                    self.sname=input("Enter stock name you wish to buy=")
                    self.sqty=int(input('Enter No. of stocks='))
                    for i in self.l_o_s:
                        if(i.name==self.sname):
                            if(i.iprice*self.sqty<=self.bullchips):
                                print('stock purchased')
                                self.bullchips-=i.iprice*self.sqty
                                if self.userobj.username in drivercode.list_of_players:
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                else:
                                    drivercode.list_of_players[self.userobj.username]=[]
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                print('BULLCHIPS REMAINING:',self.bullchips)
                            else:
                                print('BULLCHIPS INsUFFIcient')
                    self.cont=int(input('1.Finish portfolio or 2.buy more'))
                    if(self.cont==1):
                        
                        break
                for i in drivercode.list_of_players[self.userobj.username]:
                    print(i)
        else:
            drivercode.__init__(self,self.userobj,self.l_o_s)

    def simulator_run(self):
        self.countee=0
        while(self.countee<25200):
            for i in self.l_o_s:
                i.change()
            self.countee+=1
        for i in self.l_o_s:
                print(i.name,round(i.iprice,2))
    def updated_portfolio(self):
        for i in drivercode.list_of_players[self.userobj.username]:
                    for j in self.l_o_s:
                        if(j.name==i[0]):
                            self.bullchips+=j.iprice*i[1]
        print(round(self.bullchips),2)

        
maingame=drivercode(newuser,list_of_stocks)
maingame.simulator_run()
maingame.updated_portfolio()