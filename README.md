# Ergo Synced Node

[Direct Blockchain Archive Download Link](https://storage.googleapis.com/ergo_bucket_archive/ergo-full-node-data.7z)

Running a node from initial sync can take a long time, espically on older or low power devices. 

 To mitigate this problem I have taken the liberty to take a snapshot of about 1,054,000 blocks. \
 This will drastically reduce sync time.

 This program is neatly organized into a docker container to spin up a complete node in around 30 min.
## Prerequisites

Although the script tries to install docker for any linux distro, its best of docker and the docker compose plug-in are already installed.

The node currently takes about 25 GiBs of storage. It is best for your host system of have a minimum 50 GiBs free and 6 GiBs of RAM available. 

RAM may be able to be customized if you edit the `-Xmx6G` flag in `docker-compose.yml`
## Setup

Defaults:
```
localhost:9053 --This is the web address to the ergo node
API Key: hello --This is the api key to unlock the ergo node in the web panel
```
Change the hash in [ergo.conf](ergo-node/ergo.conf) and [python-conf/ergo.conf](ergo-node/python-conf/ergo.conf) to change the API Key
### ergo-node setup
```
git clone https://github.com/mgpai22/ergo-synced-node
```
```
cd ergo-synced-node/ergo-node
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
  - Warning, if run before the installer script, as ergo.conf will be overwritten
## Usage

The setup process should take under 30 min. This is depending on the download and extraction \
speed. The extraction process itself takes around 10 to 15 minutes.

`localhost:9053` will open up the webpage directly to the node.

Once setup is complete, the docker container can be left alone. The node can be used as any other node.

The config file can be edited while the node is running
- Edit as normal and save
- `docker-compose up --force-recreate -d`

The node will connect only to peers that are synced and healthy. To refresh this peer list run `./updatePeerList.sh` in the respective directory.  Then enter `docker-compose up --force-recreate -d` to start up the node.

The node instance can be removed with `docker-compose down` this will NOT delete the blockchain \
files.

## Roadmap
- Windows Guide
