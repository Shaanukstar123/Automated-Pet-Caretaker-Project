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


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("35.177.203.22", 1883, 60)
print(datetime.datetime.timestamp)
print(timetable)



client.loop_forever()



if dispense:
    servo.set_angle(30)