import paho.mqtt.client as mqtt
from  fastapi import FastAPI

app = FastAPI()

@app.get("/getdata")

async def root():
    client = mqtt.Client()
    #client.connect("ip",888,10) #ip port and timeout in seconds
    client.subscribe("dispense_time")

    messages = []
    def on_message(client,userdata, msg):
        messages.append(msg.payload)

    client.on_message = on_message
    client.loop_forever()

    return {"messages": messages}
