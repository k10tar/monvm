#!/bin/bash

while :
do
   echo "--hostname-----datetime--loadavarage-----------------------------"
   virsh list | grep running | awk '{print $2}' | xargs -P 4 -I{} ssh {} 'uname -n | tr -d "\n" ;/usr/bin/uptime' | awk '{printf("%-15s %s %s %s %s\n",$1,$2,$11,$12,$13)}'

   sleep 3

done

