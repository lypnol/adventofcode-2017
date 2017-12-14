from runners.python import Submission
from collections import OrderedDict

class AlsyiaSubmission(Submission):

	def getAdjacentCells(self, coords):
		adjValues = []
		for i in (-1, 0, +1):
			for j in (-1, 0, +1):
				if(i != 0 or j !=0):
					adjValues.append((coords[0] + i, coords[1] + j))
		return adjValues

	def fillSpirale(self, maxValue):

		pointsDict = {(0,0) : 1}
		layer = 0
		currentValue = 1
		lastPoint = (0,0)

		while (currentValue < maxValue):

			if(lastPoint[0] == layer and lastPoint[1] == -layer):
				nextPoint = (lastPoint[0] + 1, lastPoint[1])
				layer += 1
			elif(lastPoint[0] == layer and lastPoint[1] != layer):
				nextPoint = (lastPoint[0], lastPoint[1] + 1)
			elif(lastPoint[1] == layer and lastPoint[0] != -layer):
				nextPoint = (lastPoint[0] - 1, lastPoint[1])
			elif(lastPoint[0] == -layer and lastPoint[1] != -layer):
				nextPoint = (lastPoint[0], lastPoint[1] - 1)
			elif(lastPoint[1] == -layer and lastPoint[0] != layer):
				nextPoint = (lastPoint[0] + 1, lastPoint[1])

			newValue = sum([pointsDict.get(key, 0) for key in self.getAdjacentCells(nextPoint)])

			pointsDict[nextPoint] = newValue

			currentValue = newValue
			lastPoint = nextPoint

		return currentValue

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag

		return self.fillSpirale(int(s))