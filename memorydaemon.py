#!/usr/bin/env python
import sys
import memory
from daemon import Daemon

class MyDaemon(Daemon):
    def run(self):
        memory.start()

if __name__ == '__main__':
    my_daemon = MyDaemon('/tmp/cleanmemory.pid')

    if len(sys.argv) >= 2:
        if 'start' == sys.argv[1]:
            print('Strarting memory cleaner')
            my_daemon.start()
        elif 'stop' == sys.argv[1]:
            print('Stopping memory cleaner')
            my_daemon.stop()
        elif 'restart' == sys.argv[1]:
            print('Restarting memory cleaner')
            my_daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)