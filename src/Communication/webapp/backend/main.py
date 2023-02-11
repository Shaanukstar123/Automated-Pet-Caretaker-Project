import json
import paho.mqtt.client as mqtt
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

client = mqtt.Client()
client.connect("35.177.203.22", port=1883)
app = FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# This represents the data that the server is going to receive
class Feeding(BaseModel):
    id: str
    pet: str
    owner: str
    date: str
    schedule: str
    food: int


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
