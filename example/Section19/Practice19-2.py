import random
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x = [n for n in range(101)]
y1 = []
y2 = []
for i in range(101):
    y1.append(random.randint(0, 100))
    y2.append(random.randint(0, 100))
axes.plot(x, y1, color='r', marker='.')
axes.bar(x, y2, color='g')
plt.show()
