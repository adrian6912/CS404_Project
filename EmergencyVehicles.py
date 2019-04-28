class Vehicle:
    def __init__(self, ID=0, vType=0, zipcode=00000, availability=True):
        self.ID = ID
        self.vType = vType
        self.zipcode = zipcode
        self.availability = availability       

class Request:
    def __init__(self, ID, vType, zipcode):
        self.ID = ID
        self.vType = vType
        self.zipcode = zipcode
    
class Distance:
    def __init__(self, zip1, zip2, distance):
        self.zip1 = zip1
        self.zip2 = zip2
        self.distance = distance
    