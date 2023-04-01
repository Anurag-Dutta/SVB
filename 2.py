#OPEN
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import rc
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y1 = np.array([0.660487805, 0.725528455, 0.374634146, 0.428617886, 0.335609756, 0.12195122, 0.059512195, 0.063739837, 0.087154472])
y2 = np.log10(1+1/x)
plt.clf()  # Ensures a clean plotting canvas.
plt.rc('text', usetex=True)
plt.rc('figure', figsize=(1920, 1080))
plt.rc('font', family='serif', serif=['Computer Modern Roman'], size=14)
plt.ylabel("$P(\delta)$")
plt.xlabel("$\delta$")
plt.plot(x, y1, "k--", label='$Actual\ Probability$')
plt.plot(x, y2, "k-", label='$Theoretical\  Probability$')
plt.legend(loc='upper right', frameon=False, handlelength=3)
plt.savefig('2.pdf', format="pdf")
plt.savefig('2.png', format="png")