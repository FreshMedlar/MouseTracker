import matplotlib.pyplot as plt
import time
import mouseJsonParser
import pandas as pd

def mousePlot(file):

    # plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 3000)
    ax.set_ylim(0, 3000)  
    plt.draw()

    mouse_data = pd.read_csv(file)

    x1, y1, time1 = mouse_data['x'][0], mouse_data['y'][0], mouse_data['t'][0]
    
    ax.plot(x1, y1, 'ro')

    print("Inizio disegno plot")
    for row in mouse_data.iloc:
        x2,y2, time2 = row[2], row[1], row[0]
        print(f"Point {x1},{y1} to {x2},{y2}")
        
        plt.pause(((time2-time1)+1)/100)
        ax.plot([x1, x2], [y1, y2], 'b-')
        x1, y1, time1= x2, y2, time2

    print("Disegno finito")
    plt.show

mousePlot("aim_data/sample2.txt")
