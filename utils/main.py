import utils.plotter as plotter
import os
import re

files = [file for file in os.listdir("aim_data/")]

def get_number(s):
    match = re.search(r'\d+', s) 
    return int(match.group()) if match else 0

files.sort(key=get_number)

for file in files:
    plotter.mousePlot(f"aim_data/{file}")
