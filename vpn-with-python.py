###############################################################
# Hacking Lab Commandline OpenVpn Client re-written in python #
# works alot better than the ruby version i had created the   #
#  only required files are this client and the ca.crt file    #                            #
# Zy0d0x, Email:zy0d0x@nullsecurity.net                       #
###############################################################

try:
    import getpass
    import pexpect
    import shutil
    import time
    import os
except ImportError:
    pass
  
def config():
    print '\n[+]Writing Configuration File'
    file=open("/tmp/config.ovpn", "w")
    file.write("client \n")
    file.write("dev tun \n")
    file.write("proto tcp \n")
    file.write("remote 212.254.246.102 443 \n")
    file.write("ns-cert-type server \n")
    file.write("resolv-retry infinite \n")
    file.write("nobind \n")
    file.write("persist-key \n")
    file.write("persist-tun \n")
    file.write("ca ca.crt \n")
    file.write("auth-user-pass \n")
    file.write("auth-nocache \n")
    file.write("verb 1")
    file.close()
    
def resolvconfhl():
    print '\n[+]Writing Resolv.conf'
    conf=open("/tmp/resolv.conf", "w")
    conf.write("domain hacking-lab.com \n")
    conf.write("search hacking-lab.com \n")
    conf.write("nameserver 192.168.200.193")
    conf.close()
    
def resolvori():
    print '\n[+]Writing Original Resolv.conf'
    ori=open("/tmp/resolv.conf.ori", "w")
    ori.write("nameserver 194.72.9.34 \n")
    ori.write("nameserver 194.74.65.68 \n")
    ori.write("nameserver 194.72.0.98 \n")
    ori.write("domain SSG-140 \n")
    ori.write("search SSG-140")
    ori.close()
    
    
def clean():
    print'\n[+]Cleaning Up Left Over Files'
    os.remove('/tmp/config.ovpn')
    os.remove('/tmp/resolv.conf')
    os.remove('/tmp/resolv.conf.ori')
    time.sleep(1)
    print'\n[-]Exiting Commandline Client'
   


try:
   if os.geteuid() != 0:
      print 'Hacking-Lab Commandline Client Is Not Running As Root, Please Re-run Client As A Root User...\n'
      sys.exit(1)
   else:
        print'''

    #     #                                            #                    
    #     #   ##    ####  #    # # #    #  ####        #         ##   #####  
    #     #  #  #  #    # #   #  # ##   # #    #       #        #  #  #    #
    ####### #    # #      ####   # # #  # #      ##### #       #    # #####  
    #     # ###### #      #  #   # #  # # #  ###       #       ###### #    #
    #     # #    # #    # #   #  # #   ## #    #       #       #    # #    #
    #     # #    #  ####  #    # # #    #  ####        ####### #    # #####
    '''  
        username = raw_input('\nPlease Enter You Hacking Lab Email Address:')
        if username == '':
           print '\n\n[-]No Username Entered'
        else:
             password=getpass.getpass('Password: ') 
             if password == '':
                print '\n\n[-]No Password Entered'
             else:
	          config()
                  resolvconfhl()
                  shutil.copy('/tmp/resolv.conf', '/etc/resolv.conf')
                  execute=pexpect.spawn('openvpn /tmp/config.ovpn')
                  execute.expect('Enter Auth Username:')
                  execute.sendline(username)
                  execute.expect('Enter Auth Password:')
                  execute.sendline(password)
                  execute.expect('Initialization Sequence Completed')
                  print'\n[+]Connected, Press Ctrl-C To Exit Client'
                  execute.interact()
                  resolvori()
                  shutil.copy('/tmp/resolv.conf.ori', '/etc/resolv.conf')
                  clean()
               
except KeyboardInterrupt:
    print '''\n\n[-]Exiting Hacking Lab Client...'''
