#Hacking Lab Command Line Client Login 
# by ZeroCold http://zerocold.co.uk


def connect
print(banner)
print("\n\n Please Login With You Email Address & Password That You Registered With\n\n")
system(" cp /etc/resolv.conf resolv.conf.ori && cp resolv.conf.hacking-lab /etc/resolv.conf")
print("Enter Auth Username: ")
username = gets.chomp 
print("Enter Auth Password: ")
password = gets.chomp
system("echo \"#{username}\" > password.txt")
system("echo \"#{password}\" >> password.txt")
system("screen -dmSL -s  openvpn  password.ovpn")
print("Connecting Please Wait\n")
sleep(10)
system("cat ~/openvpn/screenlog.* |grep 'Initialization Sequence Completed'")
sleep(3)
menu
end

def disconnect
print("Stopping Open Vpn")
sleep(2)
system("cp ~/openvpn/resolv.conf.ori /etc/resolv.conf")
system("killall openvpn")
system("rm ~/openvpn/password.txt ~/openvpn/screenlog.*")
menu
end

def menu #main menu
print(banner)
STDOUT.print <<-EOF
 
         
 
        1. Start Client
        2. Stop Client
        3. Exit
 
 
EOF
 
print(%q{Enter number:})
mainmen = gets.chomp
 
case mainmen
when "1" then connect
when "2" then disconnect
when "3" then Process.exit!(true)
 
else print("No Option Selected")
     sleep(1)
     menu
  end
end





def banner()
print ("\e[H\e[2J")
print("
#     #                                            #                     
#     #   ##    ####  #    # # #    #  ####        #         ##   #####  
#     #  #  #  #    # #   #  # ##   # #    #       #        #  #  #    # 
####### #    # #      ####   # # #  # #      ##### #       #    # #####  
#     # ###### #      #  #   # #  # # #  ###       #       ###### #    # 
#     # #    # #    # #   #  # #   ## #    #       #       #    # #    # 
#     # #    #  ####  #    # # #    #  ####        ####### #    # #####  
                                    
                       OpenVpn Command Line Client                                     
")
end
if ARGV.length == 0
   menu
end
