import random
import json
from distributionCenter import DistributionCenter
from shippingLocation import ShippingLocation
from material import Material
from optimizedPlan import OptimizedPlan
from constants import NUMBER_OF_ROWS

shippingLocations = [
    ShippingLocation("SL001", "Dallas Production", (32.7767, -96.7970)),
    ShippingLocation("SL002", "Los Angeles Manufacturing", (34.0549, -118.2426)),
    ShippingLocation("SL003", "Atlanta Manufacturing", (33.7501, -84.3885)),
    ShippingLocation("SL004", "Chicago Production Center", (41.8832, -87.6324)),
    ShippingLocation("SL005", "Miami Manufacturing", (25.7617, -80.1918)),
    ShippingLocation("SL006", "Charleston Production Center", (32.7833, -79.9320)),
    ShippingLocation("SL007", "Charlotte Production", (35.2216, -80.8401)),
    ShippingLocation("SL008", "New York Production", (40.7128, -74.0060)),
    ShippingLocation("SL009", "Cleveland Manufacturing", (41.4993, -81.6944)),
    ShippingLocation("SL010", "Detroit Production Center", (42.3297, -83.0425)),
    ShippingLocation("SL011", "Phoenix Manufacturing", (33.4482, -112.0777)),
    ShippingLocation("SL012", "Seattle Production Center", (47.6061, -122.3328)),
    ShippingLocation("SL013", "Denver Production", (39.7392, -104.9903)),
    ShippingLocation("SL014", "Boston Manufacturing", (42.3555, -71.0565)),
    ShippingLocation("SL015", "Houston Production Center", (29.7601, -95.3701)),
    ShippingLocation("SL016", "San Francisco Production", (37.7749, -122.4194)),
    ShippingLocation("SL017", "Philadelphia Manufacturing", (39.9526, -75.1652))
]

distributionCenters = [
    DistributionCenter("DC001", "Northeast Regional DC", (43.2994, -74.2179), "regional"),
    DistributionCenter("DC002", "Southwest Distribution", (37.5498, -111.0060), "regional"),
    DistributionCenter("DC003", "West Coast Center", (42.9278, -124.2336), "regional"),
    DistributionCenter("DC004", "Midwest Distribution Hub", (44.9154, -90.2035), "regional"),
    DistributionCenter("DC005", "Southeast Regional DC", (32.1929, -82.6290), "regional"),
    DistributionCenter("DC006", "Central Distribution Center", (39.1137, -101.4595), "regional"),
    DistributionCenter("DC007", "Pacific Northwest Hub", (45.6959, -123.6833), "regional"),
    DistributionCenter("DC008", "Southern Regional DC", (32.7819, -100.2407), "regional"),
    DistributionCenter("DC009", "Mountain States Distribution", (46.1475, -108.8199), "regional"),
    DistributionCenter("DC010", "East Coast Center", (41.6445, -71.7787), "regional"),
    DistributionCenter("DC011", "Northwest Distribution", (40.7128, -74.0060), "regional"),
    DistributionCenter("DC012", "Great Lakes Regional DC", (40.7128, -74.0060), "regional"),
    DistributionCenter("DC013", "Dallas Local DC", (40.7128, -74.0060), "local"),
    DistributionCenter("DC014", "Chicago Metro Distribution", (40.7128, -74.0060), "local"),
    DistributionCenter("DC015", "Atlanta City Center", (40.7128, -74.0060), "local"),
    DistributionCenter("DC016", "Los Angeles Urban Hub", (40.7128, -74.0060), "local"),
    DistributionCenter("DC017", "Miami Local Distribution", (40.7128, -74.0060), "local"),
    DistributionCenter("DC017", "National Fulfillment Center", (40.7128, -74.0060), "cross-country"),
    DistributionCenter("DC018", "Continental U.S. Distribution", (40.7128, -74.0060), "cross-country"),
    DistributionCenter("DC019", "North America Central Hub", (40.7128, -74.0060), "cross-country"),
    DistributionCenter("DC020", "Domestic Operations Center", (40.7128, -74.0060), "cross-country"),
    DistributionCenter("DC021", "Europe Regional DC", (40.7128, -74.0060), "international"),
    DistributionCenter("DC022", "Asia-Pacific Distribution Hub", (40.7128, -74.0060), "international"),
    DistributionCenter("DC023", "Middle East Logistics Center", (40.7128, -74.0060), "international"),
    DistributionCenter("DC024", "South America Distribution", (40.7128, -74.0060), "international"),
    DistributionCenter("DC025", "Global Export Hub", (40.7128, -74.0060), "international"),
    DistributionCenter("DC026", "International Gateway DC", (40.7128, -74.0060), "international")   
   ]

materials = [
   Material("material_A", "frozen fries", 8.55, random.choice(range(1,8)),"A789-0"), #frozen perishable
   Material("material_B", "potato chips", 5.69, random.choice(range(30,365)),"B789-0"), #packaged good
   Material("material_C", "fedora", 25.45, random.choice(range(90,180)),"A244-0"), #fashion/seasonal
   Material("material_D", "screwdriver", 3.50), #staple
   Material("material_E", "isopropyl alcohol", 4.99, random.choice(range(30,730)),"A725-0"), #chemical/pharmecutical
   Material("material_F", "latest smart phone", 896.75), #electronic/new product
   Material("material_G", "scarf", 22.13, random.choice(range(90,180)),"B244-0"), #fashion/seasonal
   Material("material_H", "canned food", 4.33, random.choice(range(30,365)),"C789-0") #packaged good
]


def main():
    
    #put shipping locations, distribution centers, and materials all in a list of dictionaries
    locations = []
    for location in shippingLocations:
        locations.append(location.to_dictionary())
    output = {"shippingLocations": locations}
    centers = []
    for center in distributionCenters:
        centers.append(center.to_dictionary())
    output["distributionCenters"] = centers
    rows = []

    #generate values for rows, and compile a list of each in dictionary form
    for index in range(NUMBER_OF_ROWS):
        shippingFrom = random.choice(shippingLocations)
        shippingTo = random.choice(distributionCenters)
        material = random.choice(materials)
        material.incrementBatch() #increment batch number of that material
        row = OptimizedPlan(shippingFrom, shippingTo, material)
        rows.append(row.to_dictionary())
         
    output["optimizedPlan"] = rows

    #write to output file all the data in json form
    with open("output.json", "w") as file:
        file.write(json.dumps(output, indent=4))

        


if __name__ == "__main__":
    main()