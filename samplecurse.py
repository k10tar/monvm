#!/usr/bin/env python

import curses
import time

if __name__=="__main__":
    try:
        stdscr = curses.initscr()
        curses.noecho()

        for t in range(0,10):
            stdscr.clear()
            stdscr.addstr(
                0,0,'Program will be terminated after %s seconds' % (10 - t))
            stdscr.refresh()
            time.sleep(1)
    except:
        # Exception by Ctrl + c
        pass
    finally:
        curses.echo()
        curses.endwin()


