import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn;
seaborn.set()


data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

print()
print("mean height: ", heights.mean())
print("standard deviation: ", heights.std())
print("minimum height: ", heights.min())
print("maximum height: ", heights.max())

print("\n25th percentile: ", np.percentile(heights, 25))
print("50th percentile: ", np.percentile(heights, 50))
print("75th percentile: ", np.percentile(heights, 75))
print("\nMedian: ", np.median(heights))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('Height (cm)')
plt.ylabel('number')

plt.figure()
