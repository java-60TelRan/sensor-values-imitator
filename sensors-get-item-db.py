import boto3
dynamodb = boto3.resource("dynamodb", region_name="il-central-1")
table = dynamodb.Table("sensors-data")
response = table.get_item(Key={
    "sensorId": "126",
    "timestamp":1769971155547
})
print(response.get("Item"))
response = table.query(
   KeyConditionExpression=boto3.dynamodb.conditions.Key("sensorId").eq("126")
)
print(response.get("Items"))