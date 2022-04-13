import json
import port
import Operations

nodeList = ["72.82.0.222:9052", "176.9.15.237:9052", "213.239.193.208:9052", "195.201.82.115:9052"]

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
        if data[x]['address'] != 'N/A' and (data[x]['status'] == 'Equal' or 'Older') and data[x]['height'] > 200000:
            dataList.append(data[x]['address'][1:])

peerList = []
[peerList.append(x) for x in dataList if x not in peerList]  # gets rid of any duplicate peers in peerList

# print(peerList)
# print(len(peerList))

Operations.writeToConf(peerList)

# openList = []
# for x in peerList:  # checks if port 9053 is open which allows swagger (api) usage
#     ipAddr = str(port.splitIP(x))
#     sock = 9052
#     if port.portCheck(ipAddr, sock) == 'open':
#         openList.append(ipAddr + ':9052')
# 
# finalList = openList + nodeList
# emp = []
# [emp.append(x) for x in finalList if x not in emp]
# print('final good nodeList below')
# print(json.dumps(emp))
