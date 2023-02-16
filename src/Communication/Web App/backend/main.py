# This is importing the libraries that are needed for the code to run.
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Creating a new instance of the FastAPI class.
app = FastAPI(debug=True)
# This is a middleware that allows the server to receive requests from any origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# The Feeding class has a string id, a string pet, a string owner, a string date, a string schedule,
# and an integer food


class Feeding(BaseModel):
    id: str
    pet: str
    owner: str
    date: str
    schedule: str
    food: int


# This is the endpoint which receives the data
@app.post("/")
# """
# It creates a feeding
# :param feeding: Feeding - This is the request body. It's a Feeding object
# :type feeding: Feeding
# """
async def create_feeding(feeding: Feeding):
    # Converting the Feeding object into a dictionary.
    feeding_dict = feeding.dict()

    # Opening the file feedings.json in read mode.
    with open('feedings.json', 'r') as f:

        # Trying to load the file feedings.json.
        try:
            feedings = json.load(f)
        # If the file feedings.json is empty, then the json.load() function will raise a
        # JSONDecodeError. This code is handling that error by setting the feedings variable to an
        # empty list.
        except json.decoder.JSONDecodeError:
            feedings = []

    # Opening the file feedings.json in write mode.
    with open('feedings.json', 'w') as f:
        # Adding the new feeding to the list of feedings.
        feedings.append(feeding_dict)
        # Writing the list of feedings to the file feedings.json.
        f.write(json.dumps(feedings, indent=4))
    # Returning a dictionary with a message key and a value of "Feeding added".
    return {"message": "Feeding added"}

@app.delete("/")
async def delete_feeding(feeding: Feeding):
    # Converting the Feeding object into a dictionary.
    feeding_dict = feeding.dict()
    # Code for deleting the feeding goes here
    return {"message": f"Feeding deleted: ${feeding_dict}"}
