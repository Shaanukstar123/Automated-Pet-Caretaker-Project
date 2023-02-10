import paho.mqtt.client as mqtt
import servo_test as servo
import datetime
import json


dispense = False
timetable = {}

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("timetable")
    

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    timetable = json.loads(msg.payload)
    timetable = [
    {"id": "afK04drjIsDxu9I6dWjY","pet": "silver","owner": "aaaa@gmail.coooom","date": "02/02/2023, 09:16",
     "schedule": "once","food": 100},{"id": "bG2ngtZQ6Xu6LsiMIy8U","pet": "silver","owner": "aaaa@gmail.coooom",
    "date": "09/02/2023, 00:10","schedule": "everyday","food": 50}]


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("35.177.203.22", 1883, 60)
print(datetime.datetime.timestamp)
print(timetable)
time = datetime.datetime.now()
print(time)



client.loop_forever()



if dispense:
    servo.set_angle(30)
