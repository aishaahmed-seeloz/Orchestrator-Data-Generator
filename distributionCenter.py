class DistributionCenter:
    def __init__(self, id, name, location, region):
        self.id = id
        self.name = name
        self.location = location
        self.region = region
    
    def to_dictionary(self):
        return {"id":self.id, "name":self.name, "location": {"lat":self.location[0], "lng":self.location[1]}}