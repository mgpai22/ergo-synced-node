import json
import requests


def writeToConf(peerList):
    data = ['ergo {', '    directory = "/ergo/.ergo"', '    node {mining = false}',
            '    wallet.secretStorage.secretDir = ${ergo.directory}"/wallet/keystore"', '}', 'scorex {',
            '    restApi {',
            '        apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"', '}',
            'network {', '    knownPeers = ' + str(json.dumps(peerList)), '    maxConnections = ' + str(len(peerList)),
            '}', '}']
    with open('ergo.conf', 'w') as conf:
        for line in data:
            conf.write(line)
            conf.write('\n')


def write(new_data, filename):  # function that appends data to the specified file
    with open(filename, "r") as file1:
        data = json.load(file1)
        data.append(new_data)
    with open(filename, "w") as file1:
        # Sets file's current position at offset.
        file1.seek(0)
        json.dump(data, file1, indent=4)


def file(x):  # Function to load specified file
    with open(x, 'r+') as file:
        return json.load(file)


def clear(file):  # function to clear the file so appended data isn't constantly repeated
    dict1 = []  # After everything is cleared this is what will be put back into the fresh  file
    out_file = open(file, "w")

    json.dump(dict1, out_file, indent=6)

    out_file.close()


def NodeAPIcall(ip):
    URL = f'http://{ip}/peers/syncInfo'
    return requests.get(url=URL).json()
