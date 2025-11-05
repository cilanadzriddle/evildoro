#!/usr/bin/env python3

import time
import argparse
# from playsound import playsound

def rest(rest_time):
    while rest_time:
        mins, secs = divmod(rest_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        rest_time -= 1
    print("End!\r")

def work(work_time):
    while work_time:
        mins, secs = divmod(work_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        work_time -= 1
    print("End!\r")

cycles = int(1)
pomodoro = str(input("Pomodoro? "))

if(pomodoro == "Y"):
    cycles = int(input("Enter number of cycles: "))
    work_time = int(input("Enter seconds of work: "))
    rest_time = int(input("Enter seconds of rest: "))
else:
    work_time = int(input("Enter seconds of work: "))

for i in range(0, cycles):
    work(work_time)
    if(pomodoro == "Y"):
        rest(rest_time)
