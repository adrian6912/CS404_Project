'''
Created on Apr 19, 2019

@author: Adrian Ridder
'''

from EmergencyVehicles import Vehicle as V

if __name__ == '__main__':
    vehicleListy = []
    f = open("EmerVehicles.txt")
    for vehicle in f:
        info = vehicle.split()
        vehicleListy.append(V(info[0], info[1], info[2]))
    for vehicle in vehicleListy:
        print(vehicle.zipcode)
        