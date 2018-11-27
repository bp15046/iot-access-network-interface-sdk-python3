from anif.mqttif import MQTTPublishInterface
import json
import time


MQTT_BROKER_ADDR = "172.29.156.83"
MQTT_BROKER_PORT = 1883

interface = MQTTPublishInterface(MQTT_BROKER_ADDR, MQTT_BROKER_PORT)
interface.open("TEST/test")
counter = 0

try:
    while True:
        payload_dit = {"counter" : counter}
        payload = json.dumps(payload_dit)
        interface.write(payload)
        counter += 1
        time.sleep(1)
        
except KeyboardInterrupt:
    interface.close()