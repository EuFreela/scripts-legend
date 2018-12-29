#!/usr/bin/python
import os
import commands 

def banner():
    print "========================================================================"
    print "|       lll                                    dd                      |"
    print "|       lll   eee   gggggg   eee  nn nnn       dd  sss                 |"
    print "|       lll ee   e gg   gg ee   e nnn  nn  dddddd s                    |"
    print "|------------------------------------------------------------------>   |"
    print "|       lll eeeee  ggggggg eeeee  nn   nn dd   dd  sss                 |"
    print "|       lll  eeeee      gg  eeeee nn   nn  dddddd     s                |"
    print "|                   ggggg                          sss                 |"
    print "========================================================================"
    print "                                                              Spook v0.7"
    print "                                                                 Netstat"
    
    
def ntulp():
    r = commands.getoutput("netstat -ntulp")
    print "\n\n========================================================================"
    print r
    print "========================================================================"

    
    
os.system("clear")
banner()
ntulp()

print ("\nDefine port for anp ::")
port = raw_input()
print "\n---- search .."
print commands.getoutput("netstat -anp | grep "+port)
print commands.getoutput("cat /etc/services | grep "+port)

print "\n"

print ("Define IP (default 127.0.0.1) ::")
ip = raw_input()

if not ip:
    ip = "127.0.0.1"
    
r = commands.getoutput("netstat -anp | grep "+ip)
y = commands.getoutput("sudo nmap -sT "+ip)

if not r:
    print "\nanp Not success :(\n"
else:
    print r

print y

print "\n"

print "Chat on "+ip+" "+port
msgDefault = "Policia Juduciaria Federal! Tire as maos do teclado. Voce tem direito a um advogado pela assistencia juridica gratuita. Qualque coisa que venha a digitar apos o aviso pode ser usado contra voce no tribunal."
print (msgDefault)
print commands.getoutput("nc "+ip+" "+port)



