import random
from fastapi import FastAPI, Query
import json
from pydantic import BaseModel


app = FastAPI(debug=True)

class Dish(BaseModel):
    Naam: str
    Categorie: str
    Allergie: str
    Oorsprong: str
    id: int


with open("food.json") as file:
  menu = json.load(file)
  print(menu)


# Het hele menu opvragen
@app.get("/menu")
async def get_menu():
    return {"menu": menu}

# Een random gerecht uit het menu weergeven
@app.get("/dish")
async def get_dish():
    return{"dish": random.choice(menu)}



# Een gerecht toevoegen aan de menukaart
@app.post("/new_dish", response_model=Dish, tags=["menu"])
async def make_new_dish(dish: Dish):
    key = max(menu, key=menu.get) + 1
    menu[key] = dish
    return menu[key]
