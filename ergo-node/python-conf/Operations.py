import json
import requests
import asyncio
import aiohttp
from aiohttp import ClientSession
from pyhocon import ConfigFactory, HOCONConverter
from typing import List, Dict, Any


def writeToConf(peerList: List[str], conf_file: str) -> None:
    conf = ConfigFactory.parse_file(conf_file)
    knownPeers = conf.get_list('scorex.network.knownPeers')
    updatedPeers = knownPeers + peerList
    conf.put('scorex.network.knownPeers', updatedPeers)
    conf_string = HOCONConverter.to_hocon(conf)
    with open('ergo.conf', 'w') as f:
        f.write(conf_string)

def write_declared_address(ip_address: str, conf_file: str) -> None:
    conf = ConfigFactory.parse_file(conf_file)
    conf.put('scorex.network.declaredAddress', ip_address)
    conf_string = HOCONConverter.to_hocon(conf)
    with open('ergo.conf', 'w') as f:
        f.write(conf_string)

def write_api_key_hash(api_key_hash: str, conf_file: str) -> None:
    conf = ConfigFactory.parse_file(conf_file)
    conf.put('scorex.restApi.apiKeyHash', api_key_hash)
    conf_string = HOCONConverter.to_hocon(conf)
    with open('ergo.conf', 'w') as f:
        f.write(conf_string)

def write_node_name(node_name: str, conf_file: str) -> None:
    conf = ConfigFactory.parse_file(conf_file)
    conf.put('scorex.network.nodeName', node_name)
    conf_string = HOCONConverter.to_hocon(conf)
    with open('ergo.conf', 'w') as f:
        f.write(conf_string)
def write(new_data, filename: str) -> None:  # function that appends data to the specified file
    with open(filename, "r") as file1:
        data = json.load(file1)
        data.append(new_data)
    with open(filename, "w") as file1:
        # Sets file's current position at offset.
        file1.seek(0)
        json.dump(data, file1, indent=4)


def file(file_name: str):  # Function to load specified file
    with open(file_name, 'r+') as file:
        return json.load(file)


def clear(file: str) -> None:  # function to clear the file so appended data isn't constantly repeated
    dict1 = []  # After everything is cleared this is what will be put back into the fresh  file
    out_file = open(file, "w")

    json.dump(dict1, out_file, indent=6)

    out_file.close()


def NodeAPIcall(ip: str) -> Dict[str, Any]:
    URL = f'http://{ip}/peers/syncInfo'
    return requests.get(url=URL).json()

async def get(url: str, session: ClientSession) -> List[Dict[str, Any]]:
    URL = f'http://{url}/peers/syncInfo'
    data = []
    try:
        async with session.get(url=URL) as response:
            resp = await response.text()
            data.append(json.loads(resp))
    except Exception as e:
        pass
    return data


async def main(urls: List[str]):
    async with aiohttp.ClientSession() as session:
        resp = await asyncio.gather(*[get(url, session) for url in urls])
    return resp
