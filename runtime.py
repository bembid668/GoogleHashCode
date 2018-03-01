import Maths
import numpy as np
import sys

def process(filename):
	queue = []
	output = ""
	with open(filename,'r') as file:
		count = 0
		for line in file:
			if count == 0:
				[numRows,nuymCols,numVehicles,numRides,perRideBonus,numSteps] = line.strip().split(" ")
				count += 1
			else:
				[xCoordStrt,yCoordStrt,xCoordEnd,yCoordEnd,strtTm,endTm] = line.strip().split(" ")
				queue.append({
					"start":[xCoordStrt,yCoordStrt],
					"end":[xCoordStrt,yCoordStrt],
					"startTime":[xCoordStrt,yCoordStrt],
					"endTime":[xCoordStrt,yCoordStrt],
				})
	cars = []
	for x in range(0, numVehicles):
		cars.append([0, 0, None])

for x in range(0, numSteps):
		excTrips = []
		for car in cars:
			tripIndex = None
			distance = None

			for index, trip in enumerate(queue[]:
				temp_distance = Math.abs(cars[0]-xCoordStrt)+Maths.abs(cars[1]-yCoordStrt)
				if temp_distance < distance:
					distance = temp_distance
					tripIndex = index
					move_intersection()

				elif(temp_distance == 0){
					car[3] = tripIndex
				}

				temp_end_distance = Math.abs(cars[0]-xCoordEnd)+Maths.abs(cars[1]-yCoordEnd)
				if temp_end_distance < distance:
					distance = temp_end_distance
					tripIndex = tripIndex
					move_intersection()
				elif(temp_distance == 0){
					car[3] = None;
					output += 
					}


def move_intersection(self, carsID, tripIndex):
				if(tripIndex != None):
					xDif = cars[carsID][0] - xCoordStrt
					yDif = cars[carsID][1] - yCoordStrt
					if(xDif>0){cars[carsID][0] = cars[carsID][0] + 1}
					elif(xDif<0){cars[carsID][0] = cars[carsID][0] - 1}
					elif(yDif>0){cars[carsID][1] = cars[carsID][1] + 1}
					elif(yDif<0){cars[carsID][1] = cars[carsID][1] - 1}
					excTrips.append(tripIndex)


output = ""
def write_file(, filename):
	output +=
	with open(filename) as f:
		string s =



process("a_example.in")
