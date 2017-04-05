import requests

url = "http://localhost:8080/api/running/vpn"

payload = "{\n    \"l3vpn\": [\n      {\n        \"name\": \"goonbag\",\n        \"endpoint\": [\n          {\n            \"id\": \"c1\",\n            \"as-number\": 65001,\n            \"ce\": {\n              \"device\": \"ce0\",\n              \"local\": {\n                \"interface-name\": \"GigabitEthernet\",\n                \"interface-number\": \"0/9\",\n                \"ip-address\": \"192.168.0.1\"\n              },\n              \"link\": {\n                \"interface-name\": \"GigabitEthernet\",\n                \"interface-number\": \"0/2\",\n                \"ip-address\": \"10.1.1.1\"\n              }\n            },\n            \"pe\": {\n              \"device\": \"pe2\",\n              \"link\": {\n                \"interface-name\": \"GigabitEthernet\",\n                \"interface-number\": \"0/0/0/1\",\n                \"ip-address\": \"10.1.1.2\"\n              }\n            }\n          },\n          {\n            \"id\": \"c2\",\n            \"as-number\": 65001,\n            \"ce\": {\n              \"device\": \"ce2\",\n              \"local\": {\n                \"interface-name\": \"GigabitEthernet\",\n                \"interface-number\": \"0/3\",\n                \"ip-address\": \"192.168.1.1\"\n              },\n              \"link\": {\n                \"interface-name\": \"GigabitEthernet\",\n                \"interface-number\": \"0/1\",\n                \"ip-address\": \"10.2.1.1\"\n              }\n            },\n            \"pe\": {\n              \"device\": \"pe2\",\n              \"link\": {\n                \"interface-name\": \"GigabitEthernet\",\n                \"interface-number\": \"0/0/0/2\",\n                \"ip-address\": \"10.2.1.2\"\n              }\n            }\n          }\n        ]\n      }\n    ]\n  }"
headers = {
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'content-type': "application/vnd.yang.data+json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
