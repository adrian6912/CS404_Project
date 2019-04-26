class Vehicle:
    def __init__(self, ID, vType, zipcode, availability=True):
        self.ID = ID
        self.vType = vType
        self.zipcode = zipcode
        self.availability = availability
        
    def get_info(self):
        '''Import the information for this particular vehicle from a file'''
        

class Request:
    ID = 0
    type = 0
    zipcode = 00000
    
class distance:
    zipcode1 = 00000
    zipcode2 = 00000
    distance = 0
    