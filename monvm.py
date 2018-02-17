#!/usr/bin/env python

import curses
import time
import commands
import sys
import re


def get_vmlist():
    try:
        vmlist = commands.getoutput("virsh list | grep running | awk '{print $2 \n}'").split("\n")
    except:
        print("Error: Could not get vm list")

    #print vmlist
    return vmlist



if __name__=="__main__":
    #args = sys.argv
    #interval = args[1]
    
    
    try:

        stdscr = curses.initscr()
        curses.noecho()

        stdscr.clear()
        while 1:


            vmlist = get_vmlist()

            #for i,vm in enumerate(vmlist.split("\n")):
            for i,vm in enumerate(vmlist):
                req = "ssh "+vm+" 'uname -n  | tr -d \"\\n\" ; /usr/bin/uptime'"
                #print req

                stdscr.addstr(0,0,"host           time      load average")
                stdscr.addstr(1,0,"------------+--------+-----------------")

                try:
                    res = commands.getoutput(req)
                    #print req
                    #print res
                    item = res.split()
                    #disp = printf("%-11s %s %s %s %s",item[0],item[1],item[10],item[11],item[12])
                    disp = "%-12s %s %s %s %s" % (item[0],item[1],item[10],item[11],item[12])
                    stdscr.addstr(i+2,0,disp)
                except:
                    import traceback
                    #print("Error: Could not connect vm")
                    stdscr.addstr(i+2,0," Error: Could not connect vm")
                    traceback.print_exc()

                stdscr.refresh()
            time.sleep(3)
    except:
        print("Error: Screen error")

    finally:
        curses.echo()
        curses.endwin()

#while :
#do
#   echo "--hostname-----datetime--loadavarage-----------------------------"
#   virsh list | grep running | awk '{print $2}' | xargs -P 4 -I{} ssh {} 'uname -n | tr -d "\n" ;/usr/bin/uptime' | awk '{printf("%-15s %s %s %s %s\n",$1,$2,$11,$12,$13)}'
#
#   sleep 3
#
#done

