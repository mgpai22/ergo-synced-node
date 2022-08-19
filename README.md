# Ergo Synced Node

There have been several issues with running a node on this blockchain. Most notably the node \
 program crashes several times during the initial sync. This makes it frustrating for most \
people to support the network.

 To mitigate this problem I have taken the liberty to take a snapshot of about 800,000 blocks. \
 This will drastically reduce sync time and consequently eliminate most crashes.

 This program is neatly organized into a docker container to spin up a complete node in under an \
 hour.
## Prerequisites

Docker and docker compose must be installed. This node program should work on both [Windows](https://docs.docker.com/desktop/windows/install/) \
and [Linux](https://docs.docker.com/engine/install/).

Python3 must be installed on Linux. The script will not do this. It only installs pip3 if not already present.
The script will also install docker automatically on Ubuntu.

The computer should have about 30 GB of space and 6 GB of RAM.

RAM may be able to be customized if you edit the `-Xmx6G` flag in `docker-compose.yml`
## Setup

There are several files included in this repository.

The torrent folder includes the snapshot that will be downloaded via the torrent protocol. \
This is the most efficient method to obtain the snapshot. Seeding is disabled by default.

The centralized folder includes the snapshot that will be downloaded via a server. \
This will take a while download. No extra software to downloaded torrent files are included.

Defaults:
```
localhost:9053 --This is the web address to the ergo node
API Key: hello --This is the api key to unlock the ergo node in the web panel
```
### ergo-node setup
```
git clone https://github.com/mgpai22/ergo-synced-node
```
```
cd ergo-synced-node && rm -rf ergo-node-testnet && rm -rf .git && cd ergo-node
```
```
chmod +x ergo-node-installer.sh
```
```
./ergo-node-installer.sh
```
```
nano ergo.conf
```
- Edit the config file as necessary
  - Defaults are fine
  - Make sure to save the file in nano with `ctrl + o ` then exit with `ctrl + x`
  - After editing do this `docker compose up --force-recreate -d` to make sure the changes load
  - Warning, if run before the installer script, then the ergo.conf will be overwritten

### ergo-testnet-node setup
```
git clone https://github.com/mgpai22/ergo-synced-node
```
- Do this only if you haven't already
```
cd ergo-synced-node && rm -rf ergo-node && rm -rf .git && cd ergo-testnet-node
```
- Do this only if you want to get rid of the mainnet node files

```
chmod +x ergo-testnet-node-installer.sh
```
```
./ergo-testnet-node-installer.sh
```
```
nano ergo.conf
```
- Edit the config file as necessary
  - Defaults are fine
  - Make sure to save the file in nano with `ctrl + o ` then exit with `ctrl + x`
  - After editing do this `docker compose up --force-recreate -d` to make sure the changes load
  - Warning, if run before the installer script, then the ergo.conf will be overwritten

## Usage

The setup process should take under an hour. This is depending on the download and extraction \
speed. The extraction process itself takes around 10 to 15 minutes.

`localhost:9053` will open up the webpage directly to the node.

Once setup is complete, the docker container can be left alone. The node can be used as any other node.

The config file can be edited while the node is running
- Edit as normal and save
- `docker-compose up --force-recreate -d`

Due to the node getting stuck on blocks, in the config there are now known peers set. The node will connect only to \
peers that are synced and healthy. To refresh this peer list run `./updatePeerList.sh` in the respective directory.  Then enter `docker-compose up --force-recreate -d` to start up the node.

The node instance can be removed with `docker-compose down` this will NOT delete the blockchain \
files.

## Roadmap
- Windows Guide
