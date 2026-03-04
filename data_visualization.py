# import numpy as np
# import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5,6]
# y = [10, 12, 5, 8, 7,14]

# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot Example')
# plt.show()

# plt.scatter(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter Plot Example')
# plt.show()

# categories = ['A', 'B', 'C', 'D', ' E','F']
# values = [25, 30, 15, 20, 45, 34 ]

# plt.bar(categories, values)
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Plot Example')
# plt.show()

# data = [2, 3, 3,3,4 , 4, 4,  5, 5, 6, 6, 6, 6, 7]

# plt.hist(data, bins=5, edgecolor='k')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram Example')
# plt.show()

# labels = ['A', 'B', 'C', 'D']
# sizes = [30, 25, 20, 25]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title('Pie Chart Example')
# plt.show()

# age = [15, 20, 25, 30, 35, 40, 45, 50]

# plt.boxplot(age)
# plt.xlabel('Box Plot')
# plt.title('Box Plot Example')
# plt.show()

# import seaborn as sns


data = sns.load_dataset("iris")

# sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# plt.title("Line Plot of Sepal Length vs Sepal Width")
# plt.show()


# sns.scatterplot(x="sepal_length", y="sepal_width", data=data)
# plt.title("Scatter Plot of Sepal Length vs Sepal Width")
# plt.show()

sns.barplot(x="species", y="sepal_length", data=data)
plt.title("Bar Plot of Sepal Length by Species")
plt.show()
