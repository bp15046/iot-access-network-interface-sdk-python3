from anif.mqttif import MQTTSubscribeInterface
import ast
import time


MQTT_BROKER_ADDR = "172.29.156.83"
MQTT_BROKER_PORT = 1883

interface = MQTTSubscribeInterface("172.29.156.83", 1883)
interface.open("TEST/test")

try:
    while True:
        payload_raw = interface.read()
        payload = payload_raw.decode('utf-8')
        payload_dit = ast.literal_eval(payload)
        print(payload_dit)
        time.sleep(1)

except KeyboardInterrupt:
    interface.close()