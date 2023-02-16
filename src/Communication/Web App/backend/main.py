# This is importing the libraries that are needed for the code to run.
import json
import paho.mqtt.client as mqtt
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ssl

# Creating a new instance of the FastAPI class.
client = mqtt.Client()
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.connect("35.177.203.22", port=8883)
app = FastAPI(debug=True)
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

# This is the endpoint which receives the data
@app.post("/")
# This is function that is going to handle the request received
async def create_feeding(feeding: Feeding):
    feeding_dict = feeding.dict()
    # Append dictionary into file and format file
    with open('feedings.json', 'r') as f:
        try:
            feedings = json.load(f)
        except json.decoder.JSONDecodeError:
            feedings = []
    with open('feedings.json', 'w') as f:
        feedings.append(feeding_dict)
        f.write(json.dumps(feedings, indent=4))
        #print(feedings)
        filtered_data = [{k: v for k, v in item.items() if k in ["pet", "date", "schedule", "food"]} for item in feedings] 
    client.publish("timetable", json.dumps(feeding_dict))
    return {"message": f"Feeding added {feeding}"}

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
