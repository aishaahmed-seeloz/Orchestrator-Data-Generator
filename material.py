class Material:
    def __init__(self, material, name, unitPrice, shelfLife=None, batchNumber=None):
        self.material = material
        self.name = name
        self.unitPrice = unitPrice
        self.shelfLife = shelfLife
        self.batchNumber = batchNumber

    def incrementBatch(self):
        if self.batchNumber is not None:
            id, number = self.batchNumber.split('-')
            incremented_number = int(number) + 1
            new_id = f"{id}-{incremented_number}"
            self.batchNumber = new_id

    def to_dictionary(self):
        return {"material":self.material, "name":self.name}