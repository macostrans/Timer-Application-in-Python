import time
import sys
import os
import pygame
try:
    timer_minutes = int(input("No of Minutes You want to set the Timer For: "))
    timer_seconds = int(input("No of seconds you want to set the Timer For: "))

    if (timer_minutes < 0) or (timer_seconds < 0):
        sys.exit()
    time_start = time.time()
    seconds = 0
    minutes = 0
    ptimer_minutes = timer_minutes
    ptimer_seconds = timer_seconds

    while ((timer_minutes*60+timer_seconds)-(minutes*60+seconds))>=0:
        try:
            sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=ptimer_minutes, seconds=ptimer_seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            ptimer_minutes = int(((timer_minutes*60+timer_seconds)-(minutes*60+seconds))/60)
            ptimer_seconds = int(((timer_minutes*60+timer_seconds)-(minutes*60+seconds))%60)
            if seconds >= 60:
                minutes += 1
                seconds = 0
        except KeyboardInterrupt:
            break
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()
    time.sleep(5)
    # print("Time Up")
except:
    print("Oops Something went Wrong")