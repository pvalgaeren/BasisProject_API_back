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
def get_dish():
    return(menu[random.choice(menu)]['naam'])

        #print()
        #for value in i:
            #print(value)
            #for j in value:
                #print(j)
                #if value == "ID":
                    #list.append(j)
    #for n in list:
        #number = random.choice(list)
        #for k, v in menu:
            #if k == 'ID' and v == number:
                #if k == 'naam':
                   #return(v)
