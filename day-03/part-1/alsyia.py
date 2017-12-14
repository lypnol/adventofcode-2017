from runners.python import Submission


class AlsyiaSubmission(Submission):

	def findSpiraleLayer(self, number):

		layerMaxValue = 1
		layerNumber = 0
		while(layerMaxValue < number):
			layerNumber += 1
			layerMaxValue += 8*layerNumber

		return (layerNumber, layerMaxValue)

	def findCoordinates(self, number, layer, layerMaxValue):

		currentValue = layerMaxValue
		currentX = layer
		currentY = -layer

		while(currentValue != number):
			if(currentY == -layer and currentX != -layer):
				currentX -= 1
			elif(currentX == -layer and currentY != layer):
				currentY += 1
			elif(currentY == layer and currentX != layer):
				currentX += 1
			elif(currentX == layer and currentY != -layer):
				currentY -= 1

			currentValue -= 1

		return (currentX, currentY)

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		inputLayer, inputLayerMaxValue = self.findSpiraleLayer(int(s))
		x, y = self.findCoordinates(int(s), inputLayer, inputLayerMaxValue)

		return (abs(x) + abs(y))
