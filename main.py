'''
Created on Apr 19, 2019

@author: Adrian Ridder
'''

from EmergencyVehicles import Vehicle as V
from EmergencyVehicles import Request as R
from EmergencyVehicles import Distance as D

def getVehicles():
    vehicleList = []
    file = open("EmerVehicles.txt")
    for vehicle in file:
        info = vehicle.split()
        try:
            vehicleList.append(V(info[0], info[1], info[2]))
        except IndexError:
            pass
    return vehicleList

def getRequest():
    requestList = []
    file = open("Requests.txt")
    for request in file:
        info = request.split()
        try:
            requestList.append(R(info[0], info[1], info[2]))
        except IndexError:
            pass
    return requestList

def getDistance():
    distanceList = []
    file = open("Distance.txt")
    for distance in file:
        info = distance.split()
        try:
            distanceList.append(D(info[0], info[1], info[2]))
        except IndexError:
            pass
    return distanceList

def calcDist(location1, location2):
    pass

def findClosest(location, distances):
    pass

if __name__ == '__main__':
    vehicles = getVehicles()
    requests = getRequest()
    distances = getDistance()
    for request in requests:
        request.vType
        pass
