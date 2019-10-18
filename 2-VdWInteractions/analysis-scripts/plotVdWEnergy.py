import sys, os
import FFEA_script, FFEA_measurement
from matplotlib import pyplot as plt
import numpy as np

if len(sys.argv) != 2:
	sys.exit("Please supply a valid ffea script (.ffea)")

try:
	script = FFEA_script.FFEA_script(sys.argv[1])
except:
	sys.exit("Could not load script file")

meas = script.load_measurement()
vdwE = meas.global_meas["VdWEnergy"] / script.params.kT # kt
vdwEbar = np.array([np.mean(vdwE[0:i + 1]) for i in range(vdwE.size)])

time = np.array([i * script.params.dt * script.params.check for i in range(vdwE.size)]) / 1e-9	# ns
v, = plt.plot(time, vdwE)
vb, = plt.plot(time, vdwEbar)
plt.title(os.path.basename(sys.argv[1]) + "\nVdW Energy Trace")
plt.xlabel("Time (ns)")
plt.ylabel("Energy (kT)")
plt.legend([v,vb], ["VdW Trace", "Running Average"])
plt.show()

