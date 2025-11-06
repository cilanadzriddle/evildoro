#!/usr/bin/env python3

import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("WHORE!")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
