import random
class stocks:
    stock_dic={('TCS','HDFC Bank','Hindustan Uniliever','M&M'):'big',('Infinity inc.','Wipro','ITC','SBI','NTPC','Tata steel'):'medium',('JPpower','Suzlon energy','Yes Bank','IRFC','Reliance Power'):'penny'}
    def __init__(self,name,iprice):
        self.name=name
        self.iprice=iprice
    def change(self):
        for i in stocks.stock_dic:
            if self.name in i:
                if(stocks.stock_dic[i]=='big'):
                    self.iprice+=random.uniform(self.iprice*-0.0001,self.iprice*0.0001)
                elif(stocks.stock_dic[i]=='medium'):
                    self.iprice+=random.uniform(self.iprice*-0.0003,self.iprice*0.0003)
                else:
                    self.iprice+=random.uniform(self.iprice*-0.0005,self.iprice*0.0005)



list_of_stocks=[stocks('Infinity inc.',570),stocks('TCS',3501),stocks('HDFC Bank',1655),stocks('Wipro',406),stocks('ITC',383),stocks('Hindustan Uniliever',2515),stocks('SBI',531),stocks('M&M',1341),stocks('NTPC',168),stocks('Tata steel',112),stocks('JPpower',6.8),stocks('Suzlon energy',8.9),stocks('Yes Bank',16.1),stocks('IRFC',28.75),stocks('Reliance Power',11.05)]
'''counter=0
while(counter<5050):
    for i in list_of_stocks:
        i.change()
    counter+=1
for i in list_of_stocks:
    print('name=',i.name,'price=',round(i.iprice,2)'''