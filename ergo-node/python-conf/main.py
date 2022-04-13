import json
import port
import Operations

nodeList = ["159.65.11.55:9053", "5.189.168.217:9053", "45.118.135.117:9053", "207.180.222.84:9053",
            "89.108.111.165:9053",
            "195.10.210.41:9053", "5.188.104.249:9053", "46.4.74.175:9053", "213.239.193.208:9053",
            "192.46.215.125:9053",
            "144.202.51.55:9053", "147.135.70.51:9053", "192.119.69.82:9053", "165.227.26.175:16042",
            "159.89.116.15:11088"]

Operations.clear('data.json')

for j in nodeList:  # calls all node in the nodeList and gets peerList info
    try:
        Operations.write(Operations.NodeAPIcall(j), 'data.json')
    except Exception as e:
        pass

data = Operations.file('data.json')[0]
dataList = []

for i in range(len(Operations.file('data.json'))):  # writes all synced and open peers to a list
    data = Operations.file('data.json')[i]
    for x in range(len(data)):
        if data[x]['address'] != 'N/A' and (data[x]['status'] == 'Equal' or 'Older') and data[x]['height'] > 725000:
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
