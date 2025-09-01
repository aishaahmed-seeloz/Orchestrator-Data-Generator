import random
from datetime import date, timedelta
from constants import LEAD_TIME_COST, MINIMUM_REVENUE, MAX_QUANTITY, MIN_QUANTITY, BATCH_STOCK_DIVISOR, PRIORITIES

class OptimizedPlan:
    def __init__(self, shippingLocation, distributionCenter, material):
        self.shippingFrom = shippingLocation
        self.shippingTo = distributionCenter
        self.material = material
        self.batchNumber = material.batchNumber
        self.priority = random.choice(PRIORITIES)
        self.quantity = random.choice(range(MIN_QUANTITY, MAX_QUANTITY))
        self.targetQuantity = random.choice(range(self.quantity,MAX_QUANTITY+1000))
        self.dcStock = random.choice(range(0,self.targetQuantity-self.quantity))
        self._generate_lead_time(distributionCenter)
        self.cost = (material.unitPrice* self.quantity)+ (LEAD_TIME_COST*self.leadTime)
        self.revenue = random.choice(range(MINIMUM_REVENUE,round(self.cost*100)))/100
        self.unitPrice = material.unitPrice
        self.shipDate = self._generate_ship_date(distributionCenter)
        self.arrivalDate = self._date_addition(self.shipDate, self.leadTime)
        self.shelfLife = material.shelfLife
        self._generate_batch_stock(material)
        self._generate_expiry_date(material)

    def _generate_lead_time(self, distributionCenter):
        if(distributionCenter.region == "regional" or distributionCenter.region == "local"):
            self.leadTime =  random.choice(range(1,4))
        elif(distributionCenter.region == "cross-country"):
            self.leadTime = random.choice(range(4,8))
        elif(distributionCenter.region == "international"):
            self.leadTime = random.choice(range(8,31))

    def _generate_ship_date(self, distributionCenter):
        years = list(range(2022, 2026))   # 2022 → 2025
        months = list(range(1, 13))       # 1 → 12
        month_lengths = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        y = random.choice(years)
        m = random.choice(months)
        max_day = month_lengths[m]
        if m == 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            max_day = 29
        d = random.randint(1, max_day)
        return date(y,m,d)

    def _date_addition(self, startDate, daysToAdd):
        return startDate + timedelta(daysToAdd)
    
    def _generate_batch_stock(self, material):
        if material.shelfLife is None:
            self.batchStock = None
        else:
            self.batchStock = random.choice(range(round(self.quantity/BATCH_STOCK_DIVISOR),self.quantity))

    def _generate_expiry_date(self, material):
        if material.shelfLife is None:
            self.expiryDate = None
        else:
            self.expiryDate = self._date_addition(self.arrivalDate, material.shelfLife)

    def to_dictionary(self):
        expiry = self.expiryDate
        if expiry is not None:
            expiry = f"{expiry}"

        return {
            "from": self.shippingFrom.id, 
            "to": self.shippingTo.id, 
            "material": self.material.material, 
            "batchNumber": self.batchNumber,
            "batchStock": self.batchStock,
            "priority": self.priority, 
            "quantity": self.quantity, 
            "targetQuantity": self.targetQuantity, 
            "dcStock": self.dcStock, 
            "leadTime":self.leadTime, 
            "cost": round(self.cost, 2), 
            "revenue": self.revenue,
            "unitPrice": self.unitPrice,
            "shipDate": f"{self.shipDate}",
            "arrivalDate": f"{self.arrivalDate}",
            "shelfLife": self.shelfLife,
            "expiryDate": None if self.expiryDate is None else f"{self.expiryDate}",
            "selectedModel": None,
            "demandForecast": [],
            "weeklyDemandForecast": [],
            "modelDetails": {
                "chosenModel": None,
                "reasoning": None,
                "alternatives": []
            }
            }