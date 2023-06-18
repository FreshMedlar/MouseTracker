from pynput.mouse import Listener
import logging
import threading
import time
import os

try:
    os.remove("mouse_log.txt")
except FileNotFoundError:
    pass

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s:%(msecs)03d,%(message)s', datefmt='%H:%M:%S')



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



    
click = threading.Thread(target=clickListener).start()
move = threading.Thread(target=moveListener).start()