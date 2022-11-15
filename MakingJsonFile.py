import json


food = [
    {
        "Naam": "spaghetti bolognese",
        "Catergorie": "pasta",
        "Allergie": "gluten, ei, selderij",
        "Oorsprong": "Zuid-Italie",
        "ID": 1
    },
    {
        "Naam": "sushi",
        "Catergorie": "rijst",
        "Allergie": "gluten, eieren, schaaldieren, vis, pinda, soja, melk, noten",
        "Oorsprong": "Zuidoost-Azie",
        "ID": 2
    },
    {
        "Naam": "tiramisu",
        "Catergorie": "dessert",
        "Allergie": "melk, gluten, ei",
        "Oorsprong": "Italie",
        "ID": 3
    },

]

json_object = json.dumps(food, indent=4)

with open("food.json", "w") as file:
    file.write(json_object)