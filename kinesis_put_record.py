import boto3
import random
import names
import random
import json
import uuid

client = boto3.client('kinesis')
while True:
    #mydata = {'firstname': names.get_first_name(), 'lastname': names.get_last_name(), 'age': random.randint(1, 100)}
    mydata = { 'id': str(uuid.uuid4()), 'firstname': names.get_first_name(), 'lastname': names.get_last_name(), 'age': random.randint(1, 100)}
    partitionkey = random.randint(10, 100);
    response = client.put_record(StreamName='demo-stream', Data=json.dumps(mydata), PartitionKey=str(partitionkey))
    print(response)