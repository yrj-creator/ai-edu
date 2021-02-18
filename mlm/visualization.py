# -*- coding:utf-8 -*-
import csv
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lines = []

with open("mlm.csv") as f:
	reader = csv.reader(f)
	header = next(reader)
	for i in reader:
		line = []
		line.append(i[0])
		line.append(i[1])
		line.append(i[2])
		lines.append(line)

ax = plt.subplot(111, projection='3d')

for line in lines:
	ax.scatter(float(line[0]), float(line[1]), float(line[2]), c='r')

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()