this page is created by backtrack users (not by hacking-lab)

please watch vpn movie with backtrack

http://media.hacking-lab.com/movies/vpnbacktrack/

USER PROBLEMS WITH BACKTRACK

-> dns is not properly assigned
-> pls. test if /etc/resolv.conf points to 192.168.200.193 after vpn is established
-> without using dns names in HL most challenges won't work (virtual apache configs)

=========
Hi there, 

I’m new at your site , and I’m trying to get used to backtrack.
While the solution provided worked for me , my DNS settings kept changing back. 
i.e. the etc/resolv.conf file is overridden by the dhclient

This was bugging me , and I fixed it by editing /etc/dhclient.conf file and adding 
“Prepend domain-name-servers 192.168.200.193”

Don’t think this is the best solution  , but helps me out .

Maybe useful for other backtrack users as well .
Anayway keep up the good work !

Kind Regards,

Hermani
