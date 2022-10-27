
plant_list = [
{
  "name": "Lavender",
  "sun": "Full Sun",
  "water": "low water",
},
{
  "name": "Sage",
  "sun": "Full Sun",
  "water": "low water",
},
]

def add_new_plant(plant_name, sun_exposure, water_needs):
    new_plant = {}
    new_plant["name"] = plant_name
    new_plant["sun"] = sun_exposure
    new_plant["water"] = water_needs
    plant_list.append(new_plant)

plant_name = input("What is your plant name? \n")
sun_exposure = input("What are the light requirements? Type 'Full Sun', 'Part Sun', or 'Shade' \n")
water_needs = input("What are the water needs?  Type 'Thirsty', 'Moderate', 'Low' or 'Xeric' \n")

add_new_plant(plant_name, sun_exposure, water_needs)

print(plant_list)