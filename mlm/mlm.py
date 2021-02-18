# -*- coding:utf-8 -*-
import csv
import numpy as np

xArr = []
yArr = []
zArr = []

with open("mlm.csv") as f:
	reader = csv.reader(f)
	header = next(reader)
	for i in reader:
		xArr.append(np.float64(i[0]))
		yArr.append(np.float64(i[1]))
		zArr.append(np.float64(i[2]))

xArr = np.array(xArr)
yArr = np.array(yArr)

x = np.hstack((xArr.reshape(1000, 1), yArr.reshape(1000, 1), np.ones((1000, 1), dtype = int)))
y = np.array(zArr).reshape(1000, 1)

xMatrix = np.matrix(x)
yMatrix = np.matrix(y)
wMatrix = xMatrix.T.dot(xMatrix).I.dot(xMatrix.T).dot(yMatrix)

w = np.array(wMatrix)
print(w)