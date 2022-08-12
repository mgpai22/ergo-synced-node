import json
import port
import Operations
import asyncio

nodeList = ["167.235.75.51:9053", "15.235.145.1:9053", "3.230.76.51:9053",
            "65.21.107.123:9053", "38.242.131.141:9053", "104.248.54.140:9053",
            "154.12.244.238:9053", "173.196.49.171:9053", "73.192.192.129:9053",
            "209.50.51.194:9053", "159.65.11.55:9053", "172.104.213.182:9053",
            "144.126.130.178:9053", "154.53.43.41:9053", "80.209.232.82:9053",
            "46.4.74.175:9053", "213.239.193.208:9053", "147.135.70.51:9053",
            "51.77.221.96:9053", "13.56.77.38:9053", "38.242.225.73:9053",
            "15.235.145.2:9053", "5.189.168.217:9053", "45.118.135.117:9053",
            "207.180.222.84:9053", "89.108.111.165:9053", "195.10.210.41:9053",
            "5.188.104.249:9053", "192.46.215.125:9053", "144.202.51.55:9053",
            "192.119.69.82:9053", "165.227.26.175:16042", "159.89.116.15:11088"]

Operations.clear('data.json')

api_response_list = asyncio.run(Operations.main(nodeList))

for response in api_response_list:
    empty = []
    if response != empty:
        Operations.write(response[0], 'data.json')

data = Operations.file('data.json')
dataList = []

for i in range(len(Operations.file('data.json'))):  # writes all synced and open peers to a list
    data = Operations.file('data.json')[i]
    for x in range(len(data)):
        if data[x]['address'] != 'N/A' and (data[x]['status'] == 'Equal' or 'Older') and data[x]['height'] > 800000:
            dataList.append(data[x]['address'][1:])

peerList = []
[peerList.append(x) for x in dataList if x not in peerList]  # gets rid of any duplicate peers in peerList

# print(peerList)
# print(len(peerList))

Operations.writeToConf(peerList)

# openList = []
# for x in peerList:  # checks if port 9053 is open which allows swagger (api) usage
#     ipAddr = str(port.splitIP(x))
#     sock = 9053
#     if port.portCheck(ipAddr, sock) == 'open':
#         openList.append(ipAddr + ':9053')
#
# finalList = openList + nodeList
# emp = []
# [emp.append(x) for x in finalList if x not in emp]
# print('final good nodeList below')
# print(json.dumps(emp))
# print(len(json.dumps(emp)))
