from user import *
from stockcode import *
username=input('Username=')
password=input('Password=')
newuser=user(username,password)
    
print('''==========WELCOME TO BULLS BOARD===============
Games available:
1.SABSE BADA KHILADI (all stocks)
2.BADI MACHLI (share price>Rs.1000)
3.THODA RISK < THODA ISHQ (share price-[100,999])
4.RISK HAI TOH ISHQ HAI (penny stocks<Rs.100)''')
u_ch=int(input('Whats your call?'))

class drivercode:
    def __init__(self,userobj,l_o_s,user_ch):
        self.userobj=userobj
        self.l_o_s=l_o_s
        self.user_ch=user_ch
        if self.user_ch==1:
            drivercode.gameone()
        elif self.user_ch==2:
            drivercode.gametwo()
        elif self.user_ch==3:
            drivercode.gamethree()
        elif self.user_ch==4:
            drivercode.gamefour()
    def gameone(self):
        print('''SABSE BADA KHILADI (all stocks)
        Intructions:
        1.Entry Fee Rs.2000
        2.Prize Money (1st.Rs.3500 2nd.Rs.2500 3rd. Rs.2000)
        3.Read all scheme related documents carefully''')
        


