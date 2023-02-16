import csv
f=open('new.csv','r')
cr=csv.reader(f)
pas='pass1'
for i in cr:
    if(i[1]=='pass1'):
        print(i[0])
