import json
from pypot.vrep import from_vrep
with open('poppy_ergo_jr.json') as f:
    config = json.load(f)
    
#print(config)



simulated_robot = from_vrep(config, '127.0.0.1', 19997, 'poppy_ergo_jr.ttt')  #讀取檔案

