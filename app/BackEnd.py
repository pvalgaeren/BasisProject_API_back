import random
from fastapi import FastAPI
import json
from pydantic import BaseModel


data_tags = [
    {
        "name": "display_menu",
        "description": "Het volledige menu wordt hier getoont"
    },
    {
        "name": "dish-random",
        "description": "Hier wordt een random dish gegeven, zodat je zelf niet meer moet kiezen wat je gaat eten."
    },
    {
        "name": "new",
        "description": "Je kan een nieuw gerecht toevoegen aan de menu. "
    }
]


app = FastAPI(
    openapi_tags=data_tags,
    title="Food generator",
    description="Deze API maakt het jou gemakkelijker eten te kiezen.",
    contact={
        "naam": "Pauline Valgaeren",
        "email": "r0781850@student.thomasmore.be",
        "klas": "2CCS1"
    }
)



class Dish(BaseModel):
    Naam: str
    Categorie: str
    Allergie: str
    Oorsprong: str
    id: int

# Open json file
with open("food.json") as file:
  menu = json.load(file)
  print(menu)


# Het hele menu opvragen
@app.get("/menu", tags=["display_menu"])
async def get_menu():
    return {"menu": menu["menu"]}

# Een random gerecht uit het menu weergeven
@app.get("/dish", tags=["dish-random"])
async def get_dish():
    return{"dish": random.choice(menu["menu"])}


# Een gerecht toevoegen aan de menukaart
@app.post("/new_dish", response_model=Dish, tags=["new"])
async def make_new_dish(dish: Dish):
    menu["menu"].append(dish.dict())
    with open("food.json", "w") as file:
        json.dump(menu, file, indent=4)
    return dish
