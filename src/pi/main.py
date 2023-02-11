import paho.mqtt.client as mqtt
import servo_test as servo
import datetime
import json
import threading


dispense = False
timetable = []

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("timetable")
    

def on_message(client, userdata, msg):
    global timetable
    print(msg.topic + " " + str(msg.payload))
    timetable.append(json.loads(msg.payload))

def check_dispense(now,timetable):
    for i in range(len(timetable)):
        if (timetable[i])["date"] == now:
            print("Dispense FOOD")
            (timetable[i])["date"] = "dispensed"


# timetable = [
# {"id": "afK04drjIsDxu9I6dWjY","pet": "silver","owner": "aaaa@gmail.coooom","date": "02/02/2023, 09:16",
#     "schedule": "once","food": 100},{"id": "bG2ngtZQ6Xu6LsiMIy8U","pet": "silver","owner": "aaaa@gmail.coooom",
# "date": "11/02/2023, 17:57","schedule": "everyday","food": 50}]

#write to a json

def mqtt_thread():
    client = mqtt.Client()
    client.connect("35.177.203.22", 1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    print("Working")
    client.loop_forever()

t = threading.Thread(target = mqtt_thread)
t.start()

while True:
    now = datetime.datetime.now()
    date_format = "%d/%m/%Y, %H:%M"
    now_str = now.strftime(date_format)
    check_dispense(now_str,timetable)
