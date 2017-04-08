from pypot.vrep.io import VrepIO
from pypot.vrep.controller import VrepController
import time
import math

#k = ['m1','m2','m3','m4','m5','m6' ]
c = VrepIO()
#d = VrepController(c,str('poppy_ergo_jr.ttt'),k, sync_freq=50. )


#d.setup()

#d.update()

c.load_scene('poppy_ergo_jr.ttt',False)

c.start_simulation()

print(c.get_motor_position('m6'))

time.sleep(5)

c.set_motor_position('m6', math.radians(180))

time.sleep(5)

print(c.get_motor_position('m6'))




time.sleep(5)

c.stop_simulation()

