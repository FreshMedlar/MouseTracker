import json
import sys, os
import pandas as pd

def mouseData(): 
    # formatter for the aim in /datastream/ 
    # probably inadequate data
    with open('datastream/game-20130219-121615.json', 'r') as f:
        data = json.load(f)

    mouse_events = []
    for event in data["events"]:
        event.pop('__Event__')
        
        if event.get('type') == "MouseEvent":
            event.pop('type')
            mouse_events.append(event)

    mouse_events = mouse_events [1:] # removing the first as it's strange
    return mouse_events

def dataFormatter(data):
    # transform from %H:%M:%S:%ms to milliseconds
    data = list(map(int, data.split(':')))
    data = data[0]*3600*1000 + data[1]*60*1000 + data[2]*1000 + data[3]
    return data

def mouseAimData():
    # transform the data in mouse_log.txt into easier to process data in the format
    # millisecond, x, y

    # initial format ---> '%(asctime)s.%(msecs)03d : %(message)s', datefmt='%H:%M:%S'
    # example ---> 12:05:50:758,571,502

    data = []
    with open('mouse_log.txt', 'r') as f:

        start = False
        for line in f:
            line = line.strip().split(',')
            
            if not start: # we ignore all the lines until the first middle button press, then it starts
                if line[-1] == 'Button.middle':
                    start = True

            else: # we stop when the middle button is pressed again

                if line[-1] == 'Button.middle':
                    break
                else:
                    data.append(line)

    with open('new_mouse_log.txt', 'w') as f:
        offset = dataFormatter(data[0][0])
        for n in data:
            n[0] = str(dataFormatter(n[0])- offset)
            f.write(",".join(n))
            f.write("\n")
        f.close()

def rawToFormattedMouseInput(newtxt):
    # final (hopefully) formatter to store each aim+shot data to feed the RNN

    with open(newtxt, 'r') as f:

        lines = [line.strip() for line in f.readlines()]
        sample = 1

        end = False 
        while not end: # for each shot
            timeOffset = int(lines[0].split(',')[0]) # we use the time of the initial click to set every timestamp to zero
            
            with open(f'aim_data/sample{str(sample)}.txt', 'w') as s:    

                s.write('t,x,y\n')
                while True: # for each new coord

                    if len(lines) > 0:
                        line = lines.pop(0).split(',')
                        line[0] = str(int(line[0])-timeOffset) # subtract offset
                        
                        if line[-1] == "Button.left":  # if there is a click, we stop the for and begin a new cycle to store the new path
                            line = [line[0],line[2],line[3]]
                            s.write(",".join(line))
                            s.close()
                            sample += 1
                            break

                        s.write(",".join(line))
                        s.write('\n')
                    else:
                        end = True
                        break
    
    # lazy approach to ignore the input between the last click and the middle click
    os.remove(f"aim_data/sample{sample}.txt")


def giveSampleN(n):
    data = pd.read_csv(f"aim_data/sample{n}.txt")
    return data

# to format the data right after recording use mouseAimData()
# then use rawToFormattedMouseInput("mouse_log.txt") to obtain the single txt samples in aim_data/

mouseAimData()
# rawToFormattedMouseInput("new_mouse_log.txt")
