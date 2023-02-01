import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    #here
    return {"message": f"Feeding added {feeding}"}
