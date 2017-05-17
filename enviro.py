import pandas as pd
import numpy as np
import sklearn
safety = []

data = pd.read_csv('stream_c.csv'); 
k_range = range(len(data))

for new_data in k_range:    
    if humidity > 55:
        safety = 2
    else:    
        safety = 1        
    if temperature > 26:
        safety = 2        
    else:
        safety = 1
    if pressure > 970:
        safety = 2
    else:
        safety = 1        
    if humidity >= 60 and temperature >= 26:
        safety = 3 
    if humidity >= 60 and pressure >= 970:
        safety = 3
    if humidity >= 60 and temperature >= 26 and pressure > 970:
        safety = 4
data[: 6] = [new_data]