from pynput.mouse import Listener
import logging
import threading
import time
import os
import daemon
import argparse
import signal

# logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s:%(msecs)03d,%(message)s', datefmt='%H:%M:%S')



def on_move(x, y):
    logging.info("{0},{1}".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        print("premuto")
        logging.info('C,{0},{1},{2}'.format(x, y, button))

def moveListener():
    with Listener(on_move=on_move) as listener:
        listener.join()

def clickListener():
    with Listener(on_click=on_click) as listener:
        listener.join()

def main():

    try:
        os.remove("mouse_log.txt")
    except FileNotFoundError:
        pass

    logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s:%(msecs)03d,%(message)s', datefmt='%H:%M:%S')
    
    click = threading.Thread(target=clickListener).start()
    move = threading.Thread(target=moveListener).start()

    click.join()
    move.join()


parser = argparse.ArgumentParser()
parser.add_argument("cmd", choices=["start", "stop"])
args = parser.parse_args()

if args.cmd == "start":
    with daemon.DaemonContext():
        daemon_pid = os.getpid()
        print(daemon_pid)
        with open("mouse.pid", "w") as f:
            f.write(str(daemon_pid))

            try:
                print("daemon started")
                main()
            except Exception as e:
                print(e)

elif args.cmd == "stop":
    try:
        with open("mouse.pid", "r") as pidfile:
            pid = int(pidfile.read())
        os.kill(pid, signal.SIGTERM)
        os.remove("mouse.pid")
        print("Daemon stopped")
    except FileNotFoundError:
        print("Daemon is not running")
