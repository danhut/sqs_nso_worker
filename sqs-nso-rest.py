#!/usr/bin/env python
import boto.sqs, time, json, requests
from datetime import datetime
# Connect to SQS
conn = boto.sqs.connect_to_region("us-west-2")
# Choose the used queue
queue = conn.get_queue('nso_queue')

nso_username = 'admin'
nso_password = 'admin'
nso_base_uri = 'http://localhost:8080/api/running/vpn'
m = None

# While true read the queue, if the program reads everything then it will wait (pass)
while 1:
    try:
        result_set = queue.get_messages()
        message = result_set[0]
        print (message)
        message_body = message.get_body()
        m = json.loads(message_body)
        print (str (datetime.now()) + ": Got message from SQS: ")
        print (m)
        conn.delete_message(queue, message)
    except IndexError:
        pass
    if m is not None:
        requests.post (nso_base_uri,json=m,auth=(nso_username, nso_password),headers={'content-type':'application/vnd.yang.data+json'})
        print (str (datetime.now()) + ": Created service on NSO")
        m = None
