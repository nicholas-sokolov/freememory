#!/usr/bin/env python
import subprocess
from subprocess import PIPE
import time


command = 'vmstat -s -S M'
stats_obj = subprocess.Popen(command, shell=True, stdout=PIPE)
stats = stats_obj.stdout.read().decode().split('\n')
free = stats[4].split()[0]


def start():
    clear = 'tee -a /proc/sys/vm/drop_caches'
    sync_command = 'sync'
    if int(free) < 250:
        subprocess.call(sync_command, shell=True)
        i = 1
        while i <= 3:
            p1 = subprocess.Popen(['echo 1'], shell=True, stdout=PIPE)
            subprocess.Popen(clear, shell=True, stdout=PIPE, stdin=p1.stdout)
            p1.stdout.close()
            i += 1
        pauseAndRepeat()
    else:
        pauseAndRepeat()


def pauseAndRepeat():
    time.sleep(30)
    start()

if __name__ == '__main__':
    start()
