import json


food = {
    "menu": [
        {
            "Naam": "spaghetti bolognese",
            "Categorie": "pasta",
            "Allergie": "gluten, ei, selderij",
            "Oorsprong": "Zuid-Italie",
            "id": 1
        },
        {
            "Naam": "sushi",
            "Categorie": "rijst",
            "Allergie": "gluten, eieren, schaaldieren, vis, pinda, soja, melk, noten",
            "Oorsprong": "Zuidoost-Azie",
            "id": 2
        },
        {
            "Naam": "tiramisu",
            "Categorie": "dessert",
            "Allergie": "melk, gluten, ei",
            "Oorsprong": "Italie",
            "id": 3
        }

    ]
}

json_object = json.dumps(food, indent=4)

with open("food.json", "w") as file:
    file.write(json_object)