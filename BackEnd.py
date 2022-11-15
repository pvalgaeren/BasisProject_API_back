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


# Een gerecht uit de menukaart halen via het id
@app.get("/dish/{number}", tags=["id"])
async def get_dish(number: int | None = Query(
    default=None,
    description="Het id van het gerecht waar je meer informatie over wil.")):
    if number in menu:
        return menu[number]
    else:
        return "Het id dat u heb opgegeven hoort niet bij een gerecht"


# Een gerecht toevoegen aan de menukaart
@app.post("/new_dish", response_model=Dish, tags=["menu"])
async def make_new_dish(dish: Dish):
    key= max(menu, key=menu.get) + 1
    menu[key] = dish
    return menu[key]
