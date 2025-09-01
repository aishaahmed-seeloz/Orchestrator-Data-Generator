class ShippingLocation:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    def to_dictionary(self):
        return {"id":self.id, "name":self.name, "location": {"lat":self.location[0], "lng":self.location[1]}}