from datetime import datetime
import os.path
import requests
import slack_sdk
import os

current_datetime = datetime.now()
day=current_datetime.day
month=current_datetime.month
year=current_datetime.year
hour=current_datetime.hour
minute=current_datetime.minute


if day<=9:
    day="0"+str(day)
if month<=9:
    month="0"+str(month)

file="log-"+str(year)+"-"+str(month)+"-"+str(day)+".txt"
print(file)

p0=[]
p=[]
buf_desk=[]
n=0

def send_message(wh,message):
    payload = {'text': message,}
    r = requests.post(wh,json=payload)
    
def clean():
    if (int(hour)==0):
        if (int(minute)>0&int(minute)<2):
            if int(day)<=9:
                dayet=int(day)-1
                dayet="0"+str(dayet)
            if (os.path.exists("outlog"+str(dayet)+".txt")==1):
                os.remove("outlog"+str(dayet)+".txt")

            #for cleaning you should add name of machines there!
            os.remove("000006303_1.txt")
            os.remove("000006303_2.txt")
            os.remove("000006303_3.txt")
            os.remove("000006303_4.txt")
            os.remove("000006303_5.txt")
            os.remove("000006303_6.txt")
            os.remove("000006303_7.txt")
            
            
            
            print('Clean Ok')

def desktop_number(e):
    buf=str(e)
    e=str(e)
    e=e.split(' ')[3]
    if (os.path.exists(str(e)+".txt")!=1):
        desk_number=open(str(e)+".txt","x")
        buf_desk.append(str(e))
    f=open(str(e)+".txt", "a")

            #you should change webhook there!
    if (str(e)=="000006303_1"):
        if str(buf).find('закрыл')==-1:
            addr='https://'
            send_message(addr,(str(buf).split(" ",1)[1]).split("000006303_1")[0])
    elif (str(e)=="000006303_2"):
        if str(buf).find('закрыл')==-1:
            addr='https://'
            send_message(addr,(str(buf).split(" ",1)[1]).split("000006303_2")[0])
    elif (str(e)=="000006303_3"):
        if str(buf).find('закрыл')==-1:
            addr='https://'
            send_message(addr,(str(buf).split(" ",1)[1]).split("000006303_3")[0])
    elif (str(e)=="000006303_4"):
        if str(buf).find('закрыл')==-1:
            addr='https://'
            send_message(addr,(str(buf).split(" ",1)[1]).split("000006303_4")[0])
    elif (str(e)=="000006303_5"):
        if str(buf).find('закрыл')==-1:
            addr='https://'
            send_message(addr,(str(buf).split(" ",1)[1]).split("000006303_5")[0])
    elif (str(e)=="000006303_6"):
        if str(buf).find('закрыл')==-1:
            addr='https://'
            send_message(addr,(str(buf).split(" ",1)[1]).split("000006303_6")[0])
    elif (str(e)=="000006303_7"):
        if str(buf).find('закрыл')==-1:
            addr='https://'
            send_message(addr,(str(buf).split(" ",1)[1]).split("000006303_7")[0])
    
    f.write(buf+'\n')
    f.close()


def updating_0():
    with open(outflog, "r") as flopen: #open outlog and put them to p0
        line1=flopen.readline()
        while line1:
            p0.append(line1)
            line1=flopen.readline()
    np=0
    np0=0
    for elements in p:
        np=np+1
    for elements in p0:
        np0=np0+1
    compare = np-np0 #compare p and p0
    if (compare!=0):
        for (elements) in p:
            if (p.index(elements)+1)>=np0: #founded new elements
                print(elements)
                #write this to desktop№.txt
                elem=elements
                desktop_number(elem)#function
                with open(outflog, "w") as flopen: 
                    for element in p: #write this to outlog.txt
                        flopen.write(str(element))
                        flopen.write("\n")
        print('Updated successfully')

def updating():
    with open(outflog, "r") as flopen: #open outlog and put them to p0
        line1=flopen.readline()
        while line1:
            p0.append(line1)
            line1=flopen.readline()
    np=0
    np0=0
    for elements in p:
        np=np+1
    for elements in p0:
        np0=np0+1
    compare = np-np0 #compare p and p0
    if (compare!=0):
        for (elements) in p:
            if (p.index(elements)+1)>np0: #founded new elements
                print(elements)
                #write this to desktop№.txt
                elem=elements
                desktop_number(elem)#function
                with open(outflog, "w") as flopen: 
                    for element in p: #write this to outlog.txt
                        flopen.write(str(element))
                        flopen.write("\n")
        print('Updated successfully')
        

with open(file, "r") as fopen: #parce
    line=fopen.readline()
    while line:
        if ((line.find('[DesktopTracker] User')!=-1)and(line.find('000006303')!=-1)): #filters
            line=line.split('User')[1]
            line=line.split(' at ')[0]
            line=line.split(' for desktop')[0]
            line=line.split('\\')[1]
            if (line.find(' connected')!=-1):
                part1, part2=line.split('connected to machine')
                line=part1+'подключился'+part2
            elif (line.find(' disconnected')!=-1):
                part1, part2=line.split('disconnected from machine')
                line=part1+'закрыл'+part2
            elif (line.find(' logged off')!=-1):
                part1, part2=line.split('logged off from machine')
                line=part1+'отключился'+part2
            line=str(n)+". "+line
            p.append(line)
            n+=1
        line=fopen.readline()
outflog="outlog"+str(day)+".txt"

if (os.path.exists(outflog)!=1): #if file outlogday is not exist -
    outlog=open("outlog"+str(day)+".txt","x")#create file outlog+day.txt
    with open(outflog, "w") as flopen: #and write to them lines from file logdate.txt
        for element in p:
            flopen.write(str(element))
    print('Hello! Im created your file!')
    updating_0()
else: #file was created early and its no empty
    updating()
    


clean()
