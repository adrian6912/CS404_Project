'''
Created on Apr 19, 2019

@author: Adrian Ridder
'''

from EmergencyVehicles import Vehicle as V
from EmergencyVehicles import Request as R
from EmergencyVehicles import Distance as D
from copy import copy

def getVehicles():
    vehicleList = []
    file = open("EmerVehicles.txt")
    for vehicle in file:
        info = vehicle.split()
        try:
            vehicleList.append(V(int(info[0]), int(info[1]), int(info[2])))
        except IndexError:
            pass
    return vehicleList

def getRequest():
    requestList = []
    file = open("Requests.txt")
    for request in file:
        info = request.split()
        try:
            requestList.append(R(int(info[0]), int(info[1]), int(info[2])))
        except IndexError:
            pass
    return requestList

def getDistances():
    distanceList = []
    file = open("Distance.txt")
    for distance in file:
        info = distance.split()
        try:
            distanceList.append(D(int(info[0]), int(info[1]), int(info[2])))
        except IndexError:
            pass
    return distanceList

def calcDist(location1, location2):
    if (location1 == 00000 or location2 == 00000):
        return 500
    elif location1 == location2:
        return 0
    elif location1 > location2:
        temp = copy(location2)
        location2 = copy(location1)
        location1 = copy(temp)
    distance = 0
    t = copy(location1)
    for loc in distances:
        if loc.zip1 == t:
            if loc.zip2 == location2:
                distance = distance + loc.distance
                return distance
            distance = distance + loc.distance
            t = copy(loc.zip2)
                
def findClosest(request):
    lowestDist = V()
    for vehicle in vehicles:
        if vehicle.vType == request.vType:
            newDist = calcDist(vehicle.zipcode, request.zipcode)
            oldDist = calcDist(lowestDist.zipcode, request.zipcode)
            if (newDist < oldDist):
                lowestDist = vehicle
            if (calcDist(lowestDist.zipcode, request.zipcode)) == 0:
                return [lowestDist, 0]
    finalDistance = calcDist(lowestDist.zipcode, request.zipcode)
    return [lowestDist, finalDistance]


if __name__ == '__main__':
    vehicles = getVehicles()
    requests = getRequest()
    distances = getDistances()
    for r in requests:
        j = findClosest(r)
        closest, dist = j[0], j[1]
        print(r.ID, r.vType, r.zipcode, closest.ID, dist)
        closest.relocate(r.zipcode)









    
    
    
    