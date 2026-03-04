import matplotlib 

import matplotlib.pyplot as plt
import numpy as np



# xpoints = np.array([1,2,7,10])
# ypoints = np.array([3,8,1, 10])

# x = ["Apples","Bananas"]
# y = [400,500]
# # plt.plot(ypoints, xpoints,marker = 'o',ms=20, mec = 'yellow',mfc ='black')

x = np.array([150,20,300])

plt.pie(x)

plt.title("my example")
plt.xlabel("x-side")
plt.ylabel("y-side")

plt.show()
