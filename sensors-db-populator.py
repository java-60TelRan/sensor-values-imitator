import logging
import json
import boto3
import random 
import time
REGION = "il-central-1"
SENSOR_IDS = ["123", "124", "125", "126"]
SENSORS_NORMAL_VALUES = {
    SENSOR_IDS[0]: (30, 60),
    SENSOR_IDS[1]: (10, 80),
    SENSOR_IDS[2]: (20, 30),
    SENSOR_IDS[3]: (60, 120)
}
SENSORS_LOW_VALUES = {
    SENSOR_IDS[0]: (10, 29),
    SENSOR_IDS[1]: (0, 9),
    SENSOR_IDS[2]: (3, 19),
    SENSOR_IDS[3]: (20, 59)
}
SENSORS_HIGH_VALUES = {
    SENSOR_IDS[0]: (61, 100),
    SENSOR_IDS[1]: (81, 100),
    SENSOR_IDS[2]: (31, 50),
    SENSOR_IDS[3]: (121, 200)
}
PROBABILITY_ABNORMAL_VALUES = 15
PROBABILITY_LOW_VALUES = 60
N_PROBES = 20
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("app")
dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table("sensors-data")
def populate(id:str, value: int): 
    table.put_item(Item={
        "sensorId":id,
        "timestamp":int(time.time() * 1000),
        "value":value
    })
def getAbnormalValue(id: str) :
    return random.randint(SENSORS_LOW_VALUES[id][0],SENSORS_LOW_VALUES[id][1] )  if random.random() < PROBABILITY_LOW_VALUES\
         / 100 else random.randint(SENSORS_HIGH_VALUES[id][0],SENSORS_HIGH_VALUES[id][1] )

def getNormalValue(id: str) :
    return random.randint(SENSORS_NORMAL_VALUES[id][0],SENSORS_NORMAL_VALUES[id][1] )
 
def getIdValue():
    id = random.choice(SENSOR_IDS) 
    value = getAbnormalValue(id) if random.random() < PROBABILITY_ABNORMAL_VALUES / 100  else getNormalValue(id)
    return id, value
def main():
    for i in range(N_PROBES):
        id, value = getIdValue()
        populate(id, value) 
if __name__ == "__main__":
    main()      
        
        
    