import paho.mqtt.client as mqtt
import servo_test as servo
import datetime
import json
import threading
import dispense as dispense
import ssl
import digitalpad as pad


###Communication###

timetable = []


def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe('#')
    

def on_message(client, userdata, msg):
    global timetable
    print(msg.topic + " " + str(msg.payload))
    if msg.topic == "timetable":
        timetable.append(json.loads(msg.payload))
    elif msg.topic == "deletion":
        record = json.loads(msg.payload)
        if (record) in timetable:
            print("deleting: ",record["pet"])
            timetable.remove(record)

def check_dispense(now,timetable):
    #print(timetable)
    for i in range(len(timetable)):
        if (timetable[i])["date"] == now:
            print(timetable[i]["date"])
            print("Dispense FOOD")
            (timetable[i])["date"] = "dispensed"
            dispense.start_dispense((timetable[i])["food"])
    #dispense.start_dispense(10)      

def mqtt_thread():
    client = mqtt.Client()
    ##TLS SSL
    client. tls_set(cert_reqs=ssl.CERT_NONE)
    #client. tls_insecure_set(True)
    #client.tls_set(ca_certs="chain.pem", certfile="cert.pem",keyfile="privkey.pem")
    client.connect("petsitter.ddnsgeek.com",port=8883)

    client.on_connect = on_connect
    client.on_message = on_message
    print("Working")
    client.loop_forever()

def manual_vending():
    val = []
    number =  0
    while True:
        print(val)
        val = pad.get_key(val)
        if "D" in val:
            while "D" in val:
                val.remove("D")
                dispense.stop()
                val = []
        if "#" in val:
            while "#" in val:
                val.remove("#")
            number = int("".join(val))
            print("number: ",number)
            val = []
            dispense.start_dispense(number)
        elif "*" in val or len(val)>3:
            val  = []


t = threading.Thread(target = mqtt_thread)
t.start()

vending = t = threading.Thread(target = manual_vending)
vending.start()

while True:
    
    now = datetime.datetime.now()
    date_format = "%d/%m/%Y, %H:%M"
    now_str = now.strftime(date_format)
    check_dispense(now_str,timetable)
    

