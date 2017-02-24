from time import sleep
import paho.mqtt.client as mqtt

host = 'mqtt.beebotte.com'
port = 1883
subtopic = 'ict/sound'
pubtopic = 'ict/ai'
from time import sleep
import paho.mqtt.client as mqtt

host = 'mqtt.beebotte.com'
port = 1883
subtopic = 'ict/sound'
pubtopic = 'ict/ai'


def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))

    client.subscribe(subtopic)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    print('go publish')
    for i in range(3):
        print('yaaa')
        client.publish(pubtopic, 'Hi',1,1)
        sleep(0.2)
        client.subscribe(subtopic)


if __name__ == '__main__':

    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_message = on_message
#    client.on_subscribe = on_subscribe
    client.username_pw_set("token:<token>")
    client.connect(host, port=port, keepalive=60)

    client.loop_forever()
