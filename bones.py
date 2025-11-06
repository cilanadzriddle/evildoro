#!/usr/bin/env python3
# dependencies

import time
import argparse
import subprocess

def rest(rest_time, current_cycle, total_cycle):
    # subprocess.Popen(["play", "/home/denz/Music/SFX/a-real-boy.mp3", "-q"])
    while rest_time:
        hours, remainder = divmod(rest_time, 3600)
        mins, secs = divmod(remainder, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timeformat, " REST: [", current_cycle, "/", total_cycle, "]", end='\r')
        time.sleep(1)
        rest_time -= 1
    print("End!", end='\r')

def work(work_time, current_cycle, total_cycle):
    # subprocess.Popen(["play", "/home/denz/Music/Ringtones/The Third Sanctuary.mp3", "-q"])
    while work_time:
        hours, remainder = divmod(work_time, 3600)
        mins, secs = divmod(remainder, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timeformat, " WORK: [", current_cycle, "/", total_cycle, "]", end='\r')
        time.sleep(1)
        work_time -= 1
    print("End!", end='\r')

cycles = int(1)
pomodoro = str(input("Pomodoro? [Y/N] "))

if(pomodoro == "Y"):
    cycles = int(input("Enter number of cycles: "))
    work_time = int(input("Enter seconds of work: "))
    rest_time = int(input("Enter seconds of rest: "))
else:
    work_time = int(input("Enter seconds of work: "))

# subprocess.Popen(["hyprshade", "on", "grayscale"])
for i in range(1, cycles+1):
    work(work_time, i, cycles)
    if(pomodoro == "Y"):
        rest(rest_time, i, cycles)
    # else:
        # subprocess.Popen(["play", "/home/denz/Music/SFX/a-real-boy.mp3", "-q"])
# subprocess.Popen(["hyprshade", "off"])
