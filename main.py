import time
import datetime
import sys, traceback
import json

from mqtt import *
from playsound import *
from dotenv import load_dotenv
load_dotenv()


def runApps():
    timestamp = datetime.datetime.now()
    sec = timestamp.second
    
    sampling_time = eval(os.getenv('SAMPLING_TIME'))

    if sec % sampling_time == 0:
        # ROOM SENSOR
        detection_data = get_detection_data()
        print(f"MAIN - {timestamp} {detection_data}")
        try:
            if(detection_data["detection"] == 1):
                play_sound()
                reset_detection_data()
        except Exception as e:
            print("Error get detection")
    time.sleep(1)

if __name__ == '__main__':
    try:
        mqttc = runMQTT()
    except Exception as e:
        print("Main - Unable to connect to MQTT")
        print(e)
    
    time.sleep(1)

    while True:
        try:
            runApps()
        except Exception as e:
            print("Error : ",e)
        except KeyboardInterrupt:
            print('Syxtem Exit, Keyboard Interrupt Detected')
            sys.exit(0)
