from fastapi import FastAPI
import json
import random

app = FastAPI(debug=True)

with open("food.json") as file:
  menu = json.load(file)
  print(menu)

@app.get("/menu")
async def get_menu():
    return {"menu": menu}

@app.get("/dish")
async def get_dish():
    list = []
    for key, value in menu:
        if key == "ID":
            list.append(value)
    for n in list:
        print(n)
        number = random.randrange(len(list))
        for k, v in menu:
            if k == 'ID' and v == number:
                if k == 'naam':
                    return(v)
