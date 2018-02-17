# how to monitor vm

visrh list | grep running | awk '{print $2}' | xargs -P 4  -I{} ssh {} '/usr/bin/uptime'


virsh list | grep running | awk '{print $2 }' | xargs -P 4 -I{} ssh {}  'uname -n |tr -d "\n" ;/usr/bin/uptime' | awk '{printf("%-15s %s %s", $1,$2,$11)j}' 

