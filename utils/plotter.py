import matplotlib.pyplot as plt
# import time
# import mouseJsonParser
import pandas as pd

def mousePlot(file):

    # plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1920)
    ax.set_ylim(0, 1080)  
    plt.draw()

    mouse_data = pd.read_csv(file)

    x1, y1, time1 = mouse_data['x'][0], mouse_data['y'][0], mouse_data['t'][0]
    print(x1, y1, time1)

    ax.plot(x1, y1, 'ro')

    print("Inizio disegno plot")
    for row in mouse_data.iloc:
        x2,y2, time2 = row[1], row[2], row[0]
        print(f"Point {x1},{y1} to {x2},{y2}")
        
        plt.pause(((time2-time1)+1)/100)
        ax.plot([x1, x2], [y1, y2], 'b-')
        x1, y1, time1= x2, y2, time2

    print("Disegno finito")
    plt.show

def mousePlotWithList(lis):
    # plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1920)
    ax.set_ylim(0, 1080)  
    plt.draw()

    mouse_data = lis

    x1, y1 = mouse_data[0][0], mouse_data[0][1]
    print(x1, y1)

    ax.plot(x1, y1, 'ro')

    print("Inizio disegno plot")
    for row in mouse_data[1:]:
        x2,y2 = row[0], row[1]
        print(f"Point {x1},{y1} to {x2},{y2}")
        
        plt.pause(3/100)
        ax.plot([x1, x2], [y1, y2], 'b-')
        x1, y1 = x2, y2

    print("Disegno finito")
    plt.show



mousePlot("aim_data/sample8.txt")
