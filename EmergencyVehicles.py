from copy import copy

class Vehicle(object):
    def __init__(self, ID=0, vType=0, zipcode=00000, availability=True):
        self.ID = ID
        self.vType = vType
        self.zipcode = zipcode
        self.availability = availability  
        
    def relocate(self, newZipcode):
        self.zipcode = newZipcode
        return

class Request(object):
    def __init__(self, ID, vType, zipcode):
        self.ID = ID
        self.vType = vType
        self.zipcode = zipcode
    
class Distance(object):
    def __init__(self, zip1, zip2, distance):
        self.zip1 = zip1
        self.zip2 = zip2
        self.distance = distance
    
class EmerVehicles(object):
    def __init__(self, emergencyVehicles, distances, requests):
        emergencyVehiclesFile = open(emergencyVehicles)
        distancesFile = open(distances)
        requestsFile = open(requests)
        self.vehicles = self.getVehicles(emergencyVehiclesFile)
        self.distances = self.getDistances(distancesFile)
        self.requests = self.getRequest(requestsFile)
        
    def printOutput(self):
        file = open("ProcessedRequests.txt", "r")
        for line in file:
            print(line)
        
    def processRequests(self):
        '''Processes requests and stores them in a .txt file'''
        output = open("ProcessedRequests.txt", "w+")
        for r in self.requests:
            j = self.findClosest(r)
            closest, dist = j[0], j[1]
            string = "{} {} {} {} {} \n".format(r.ID, r.vType, r.zipcode, closest.ID, dist)
            output.write(string)
            closest.relocate(r.zipcode)
        
    def getVehicles(self, file):
        '''Returns list of vehicles from provided file'''
        vehicleList = []
        for vehicle in file:
            info = vehicle.split()
            try:
                vehicleList.append(Vehicle(int(info[0]), int(info[1]), int(info[2])))
            except IndexError:
                pass
        return vehicleList
        
    def getDistances(self, file):
        '''Returns list of distances from provided file'''
        distanceList = []
        for distance in file:
            info = distance.split()
            try:
                distanceList.append(Distance(int(info[0]), int(info[1]), int(info[2])))
            except IndexError:
                pass
        return distanceList
            
    def getRequest(self, file):
        '''Returns list of requests from provided file'''
        requestList = []
        for request in file:
            info = request.split()
            try:
                requestList.append(Request(int(info[0]), int(info[1]), int(info[2])))
            except IndexError:
                    pass
        return requestList
    
    def findClosest(self, request):
        '''Returns closest vehicles to given request'''
        lowestDist = Vehicle()
        for vehicle in self.vehicles:
            if vehicle.vType == request.vType:
                newDist = self.calcDist(vehicle.zipcode, request.zipcode)
                oldDist = self.calcDist(lowestDist.zipcode, request.zipcode)
                if (newDist < oldDist):
                    lowestDist = vehicle
                if (self.calcDist(lowestDist.zipcode, request.zipcode)) == 0:
                    return [lowestDist, 0]
        finalDistance = self.calcDist(lowestDist.zipcode, request.zipcode)
        return [lowestDist, finalDistance]
    
    
    def calcDist(self, location1, location2):
        '''Returns the distance between two zipcodes'''
        
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
        for loc in self.distances:
            if loc.zip1 == t:
                if loc.zip2 == location2:
                    distance = distance + loc.distance
                    return distance
                distance = distance + loc.distance
                t = copy(loc.zip2)
    
    
    
