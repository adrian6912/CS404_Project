'''
Created on Apr 19, 2019

@author: Adrian Ridder
'''
from EmergencyVehicles import EmerVehicles as EV

if __name__ == '__main__':
    thing = EV("EmerVehicles.txt", "Distance.txt", "Requests.txt")
    thing.processRequests()
    thing.printOutput()





    
    
    
    