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

input_ = './rec_json'
input_open   = open(input_,'r+')
input_string = input_open.read()
print ("broken json")
print (type(input_string))
print (json.loads(input_string))
print (json.encoder(input_string))

input_ = './postman_json.py'
input_open   = open(input_,'r+')
input_string = input_open.read()
print ("working json")
print (type(input_string))
print (json.loads(input_string))
"""
x = 1
# While true read the queue, if the program reads everything then it will wait (pass)
while x == 1:
    try:
        m = input_string
        print (str (datetime.now()) + ": Got message from SQS: ")
        print (m)
        n = (json.loads(m))
        #conn.delete_message(queue, message)
    except IndexError:
        pass
    if m is not None:
        r = requests.post (nso_base_uri,json=n,auth=(nso_username, nso_password),headers={'content-type':'application/vnd.yang.data+json'})
        print (r.status_code)
        print (r.json)
        print (r.headers)
        print (r.text)
        print (str (datetime.now()) + ": Created service on NSO")
        m = None
        x = 2
"""
