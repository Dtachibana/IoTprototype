from time import sleep
import paho.mqtt.client as mqtt
from datetime import datetime
import json

host = 'mqtt.beebotte.com'
port = 1883
subtopic = 'ict/sound'
pubtopic = 'ict/ai'


def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))

    client.subscribe(subtopic)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    aSecond = datetime.now().second
    print(aSecond)
    if aSecond % 2 == 1:
        message_green = json.dumps({"data":"Hi"})
        print("Hi")
        client.publish(pubtopic, message_green,1,1)
    else:
        message_blue = json.dumps({"data":"No"})
        print("No")
        client.publish(pubtopic, message_blue,1,1)
    sleep(0.2)

if __name__ == '__main__':

    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("token:<token>")
    client.connect(host, port=port, keepalive=60)
    client.loop_forever()
