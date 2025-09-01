import random
from datetime import date, timedelta

number_of_rows = 10 # sets the value for how much data rows will generate

#Generates values for quantity. Quantity can be 1000-10000
new_quantity = random.choices(range(1000, 10000), k=number_of_rows)

new_target = []
new_dcstock = []

#generates vales for target quantity. Target quantity can be quantity-11000
#generates values for distribution center stock. Values can be 0-(target quantity - quantity)
for q in new_quantity:
   target = random.choice(range(q,11000))
   new_target.append(target)
   new_dcstock.append(random.choice(range(0,target-q)))

# shipping locations
shipping_locations = [
   "Dallas Production",
   "Los Angeles Manufacturing",
   "Atlanta Manufacturing",
   "Chicago Production Center",
   "Miami Manufacturing",
   "Charleston Production Center",
   "Charlotte Production",
   "New York Production",
   "Cleveland Manufacturing",
   "Detroit Production Center",
   "Las Vegas Production",
   "Phoenix Manufacturing",
   "Seattle Production Center",
   "Denver Production",
   "Boston Manufacturing",
   "Houston Production Center",
   "San Francisco Production",
   "Philadelphia Manufacturing"
]

#generates random shipping locations
new_ship = random.choices(shipping_locations, k=number_of_rows)

# distribution centers
#represents distribution centers that will have regional shipping
reg = [
   "Northeast Regional DC",
   "Southwest Distribution",
   "West Coast Center",
   "Midwest Distribution Hub",
   "Southeast Regional DC",
   "Central Distribution Center",
   "Pacific Northwest Hub",
   "Southern Regional DC",
   "Mountain States Distribution",
   "East Coast Center",
   "Northwest Distribution",
   "Great Lakes Regional DC"
   ]

#represents distribution centers that will have local shipping
local = [
   "Dallas Local DC",
   "Chicago Metro Distribution",
   "Atlanta City Center",
   "Los Angeles Urban Hub",
   "Miami Local Distribution"
   ]

#represents distribution centers that will have cross country shipping
cross = [
   "National Fulfillment Center",
   "Continental U.S. Distribution",
   "North America Central Hub",
   "Domestic Operations Center"
   ]

#represents distribution centers that will have international shipping
inter = [
   "Europe Regional DC",
   "Asia-Pacific Distribution Hub",
   "Middle East Logistics Center",
   "South America Distribution",
   "Global Export Hub",
   "International Gateway DC"
   ]

#all distribution centers
t = reg + local + cross + inter

#generates random distribution centers
new_distr = random.choices(t, k=number_of_rows)

#Generates values for lead time based on distribution center's category
new_lead= []
for i in range(len (new_distr)):
   if(new_distr[i] in reg or new_distr[i] in local):
       new_lead.append(random.choice(range(1,4)))
   elif(new_distr[i] in cross):
       new_lead.append(random.choice(range(4,8)))
   elif(new_distr[i] in inter):
       new_lead.append(random.choice(range(8,31)))

#materials
materials = [
   ["material_A", "frozen fries", 8.55, random.choice(range(1,8)),"A789-0"], #frozen perishable
   ["material_B", "potato chips", 5.69, random.choice(range(30,365)),"B789-0"], #packaged good
   ["material_C", "fedora", 25.45, random.choice(range(90,180)),"A244-0"], #fashion/seasonal
   ["material_D", "screwdriver", 3.50, None], #staple
   ["material_E", "isopropyl alcohol", 4.99, random.choice(range(30,730)),"A725-0"], #chemical/pharmecutical
   ["material_F", "latest smart phone", 896.75, None], #electronic/new product
   ["material_G", "scarf", 22.13, random.choice(range(90,180)),"B244-0"], #fashion/seasonal
   ["material_H", "canned food", 4.33, random.choice(range(30,365)),"C789-0"] #packaged good
]

#generates values for materials
new_materials = random.choices(materials, k=number_of_rows)

#Date logic
years = list(range(2022, 2026))   # 2022 → 2025
months = list(range(1, 13))       # 1 → 12
month_lengths = {
   1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
   7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# generates shipping dates
new_ship_dates = []
new_arr= []
new_exp = []

for _ in range(number_of_rows):
   y = random.choice(years)
   m = random.choice(months)
   max_day = month_lengths[m]
   if m == 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
       max_day = 29
   d = random.randint(1, max_day)
   new_arr.append(date(y,m,d))
   new_exp.append(date(y,m,d))
   new_ship_dates.append(f"{y}-{m}-{d}")

#generates arrival dates
new_arr_dates = []

for i in range(number_of_rows):
   lead_time = timedelta(new_lead[i])
   new_arr[i] += lead_time

   new_arr_dates.append(f"{new_arr[i].year}-{new_arr[i].month}-{new_arr[i].day}")


#generates expiary dates
new_exp_dates = []

for i in range(number_of_rows):
   if new_materials[i][3] is None:
       new_exp_dates.append(None)
       continue
   expiary_time = timedelta(new_materials[i][3])
   new_exp[i] += expiary_time

   new_exp_dates.append(f"{new_exp[i].year}-{new_exp[i].month}-{new_exp[i].day}")

#generates priority
new_priority = random.choices(["low", "medium", "high"], k=number_of_rows)


new_cost = []
new_revenue = []

#generates cost and revenue
for i in range(number_of_rows):
    cost = (new_materials[i][2]* new_quantity[i])+ (8*new_lead[i])#here is a random multiplier to scale cost by lead time
    new_cost.append(cost)
    new_revenue.append(random.choice(range(10000,round(cost*100)))/100)

new_batch_number = []
new_batch_stock = []

#generates batch number and batch stock
for i in range(number_of_rows):
    if new_materials[i][3] is None:
        new_batch_number.append(None)
        new_batch_stock.append(None)
        continue
    id, number = new_materials[i][4].split('-')
    incremented_number = int(number) + 1
    new_id = f"{id}-{incremented_number}"
    new_materials[i][4] = new_id
    new_batch_number.append(new_id)
    new_batch_stock.append(random.choice(range(round(new_quantity[i]/4),new_quantity[i])))

#To Do
#write shipping locations ot json

#write distribution centers to json

#write materials to json

#write optimizedPlan to json

#Clean up code

#manual testing
for i in range(number_of_rows):
    print(f"from:{new_ship[i]}\nto:{new_distr[i]}\nmaterial:{new_materials[i][0]}\nbatch number:{new_batch_number[i]}\nbatch stock:{new_batch_stock[i]}\npriority:{new_priority[i]}\nquantity:{new_quantity[i]}\ntarget:{new_target[i]}\ndcstock:{new_dcstock[i]}\nlead time:{new_lead[i]}\ncost:{new_cost[i]:.2f}\nrevenue:{new_revenue[i]:.2f}\nunitPrice:{new_materials[i][2]:.2f}\nship date:{new_ship_dates[i]}\narrival date:{new_arr_dates[i]}\nshelf life:{new_materials[i][3]}\nexpiary date:{new_exp_dates[i]}\n")

new_data={'from':new_ship, 'to':new_distr, 'quantity':new_quantity, 'target':new_target, 'lead time':new_lead} 
