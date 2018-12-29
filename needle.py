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
    print "                                                             Needle v0.7"
    print "                                                                  Netcat"

def wait():
    os.system("clear")
    banner()
    print ( "Wait... " + str(len (success)-1) + " ports" )
    
def connect():
  for x in xrange(int(ports)+1):    
    r = commands.getoutput("nc "+str(ip)+" "+str(x))
    if r.find("Connection refused"):
        success.append(r)
        wait()
    else:
        print 'Inject x = %d' % (x)




#==============================================================================#
#                                   NEEDLER                                    #
#==============================================================================#
os.system("clear")
banner()

print ("Number of ports for injection(defalut 333) ::")
ports = raw_input()
print ("Define the IP for connection netcat (default 127.0.0.1) ::")
ip = raw_input()    

if not (ports):
    ports = "333"
if not (ip):
    ip = "127.0.0.1"
    
connect() 

print "----------------------------------------"

for y in xrange(len(success)):
    success[y]
else:    
    print "IP "+ip+"; Ports: "+ports
    print '\n Not success :( \n'
    
print "----------------------------------------"





  

