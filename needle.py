#!/usr/bin/python
import os
import commands 

success = []

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
    print "                                                      Needle Revamp v0.8"
    print "                                                                  Netcat"

def connect():
    r = commands.getoutput("nc -z -v "+str(ip)+" "+str(ports) )
    success.append(r)    


#==============================================================================#
#                                   NEEDLER                                    #
#==============================================================================#
os.system("clear")
banner()

print ("Number of ports (ex:1-10000) ::")
ports = raw_input()
print ("Define the IP for connection netcat (default 127.0.0.1) ::")
ip = raw_input()

if not (ports):
    ports = "1-10000"
if not (ip):
    ip = "127.0.0.1"
    
print ("Wait.. ("+str(ports)+")")
connect() 

print "----------------------------------------"

if success:
    print "Success, ports to conection.."
    print success
else:    
    print '\n Sorry, close ports :( \n'
    
print "----------------------------------------"
