import numpy as np
import matplotlib.pyplot as plt
with open("settings.txt","r") as settings:
    settings = [float(i) for i in settings.read().split("\n")]

k = settings[2]
nt = settings[1]

data_new_array = np.loadtxt("data.txt",dtype = int)*k
data_time = np.array([i*nt for i in range(data_new_array.size)])

fig, ax = plt.subplots(figsize=(6,5),dpi = 400)

ax.set_title("график зарядки и разрядки конденсатора")
ax.set_ylabel("U, V")
ax.set_xlabel("t, c")

ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', color = 'lightgray', linestyle = '--')
ax.grid(which='major', color = 'dimgray', linestyle = '-')


ax.plot(data_time, data_new_array, linewidth=1, label = 'U(t)', marker = "D",ms = 2,markevery = 20)

  

#ax.scatter(data_time[0:data_new_array.size:20], data_new_array[0:data_new_array.size:20], marker = 's', c = 'red', s=10)
ax.legend()

#ax.plot(data_array)
plt.show()
fig.savefig('graphic.png')
fig.savefig('graphic.svg')