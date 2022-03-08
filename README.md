
# Ergo Synced Node

There have been several issues with running a node on this blockchain. Most notably the node \
 program crashes several times during the initial sync. This makes it frustrating for most \
people to support the network.
 
 To mitigate this problem I have taken the liberty to take a snapshot of about 700,000 blocks. \
 This will drastically reduce sync time and consequently eliminate most crashes. 

 This program is neatly organized into a docker container to spin up a complete node in under an \
 hour. Furthermore, to provide easy access, ngrok is included which allows a direct tunnel (essentially a url) to the
 access the node from anywhere.
## Prerequisites

Docker and docker compose must be installed. This node program should work on both [Windows](https://docs.docker.com/desktop/windows/install/) \
and [Linux](https://docs.docker.com/engine/install/).

The computer should have about 30 GB of space available. 
## Setup

There are several files included in this repository.

The torrent folder includes the snapshot that will be downloaded via the torrent protocol. \
This is the most efficient method to obtain the snapshot. Seeding is disabled by default.

The centralized folder includes the snapshot that will be downloaded via a server. \
This will take a while download. No extra software to downloaded torrent files are included.

Defaults:
```
localhost:9053 --This is the web address to the ergo node 
localhost:4551 --This is the web address to the ngrok panel
API Key: Hello --This is the api key to unlock the ergo node in the web panel
```


### Torrent File Setup
```
git clone https://github.com/mgpai22/ergo-synced-node
```
```
cd ergo-synced-node && rm -rf ergo-node-centralized && cd ergo-node-torrent
```
```
nano ergo.conf
```
- Edit the config file as necessary
  - Defaults are fine
  - Make sure to save the file in nano with `ctrl + o ` then exit with `ctrl + x` 
```
nano docker-compose.yml
```
Make sure to add an API key for ngrok. 

To obtain one:

- Go to [ngrok](https://dashboard.ngrok.com/login)
- Sign in or make an account
- Look for the auth token it should look something like this:
  - `ngrok authtoken 292dLBeG3VamDeVqgawuKX0qaz5_2Z43xhaD2v2aCaBXFABDxa`
  - Note that the token is unique for each account and the one above will not work!
- Copy this token and paste it into the `docker-compose.yml` file 
  - The compose file should look like this after pasting:
    ```
    ...
        environment:
      DOMAIN: ergo-node
      PORT: '9053'
      AUTH_TOKEN: '292dLBeG3VamDeVqgawuKX0qaz5_2Z43xhaD2v2aCaBXFABDxa'
    ```
- If ngrok is not desired then simply delete that config from the `docker-compose.yml` file
  - The file should look as such after deletion:
  ```
    version: '3'
  services:
    ergo-node:
      build: .
      command: >
          bash -c "java -Xmx4G -jar /node/ergo-4.0.23.jar --mainnet -c /node/ergo.conf" 
      restart: unless-stopped
      ports:
        - '9053:9053'
        - '9030:9030'
  
  ```
  - It is recommend to change the ngrok port for security. Rather than `4551` choose another available port
  -For example if port `5555` is used rather than `4551`:

  ```
  ...
  ngrok:
    image: 'shkoliar/ngrok:latest'
    ports:
      - '5555:4551'
  
  ```
  - Now to access the web panel the url would be `localhost:5555`
- The `command` area is also customizable for anyone who wants to either add or remove the memory heap limit
- Make sure to save the file in nano with `ctrl + o ` then exit with `ctrl + x`

```
docker-compose up -d
```
### Centralized File Setup
```
git clone https://github.com/mgpai22/ergo-synced-node
```
```
cd ergo-synced-node && rm -rf ergo-node-torrent && cd ergo-node-centralized
```
- Follow the steps noted under the "Torrent File Setup" section to edit the `ergo.conf`
- Follow the steps noted under the "Torrent File Setup" section to add the ngrok token or to customize the program
```
docker-compose up -d
```
### Windows Setup

The steps above are clearly more linux centric. To install without the usage of a terminal perform the following:

- Download the [zip from extract](https://github.com/mgpai22/ergo-synced-node/archive/refs/heads/main.zip)
- Unextract
- Delete the unused folder and open the appropriate folder
- Open the `ergo.conf` file 
  - Defaults are fine
  - Save and exit the file once complete 
- Open the `docker-compose.yml` file
  - Add the token portion and edit the file as necessary
  - Further information is under the "Torrent File Setup" section
  - Save and exit the file once complete  
- Hold shift and right click. Look for "open in Windows terminal" and click it
- In the terminal, type `docker-compose up -d`
## Usage

The setup process should take under an hour. This is depending on the download and extraction \
speed. The extraction process itself takes around 10 to 15 minutes.

`localhost:9053` will open up the webpage directly to the node. 

`localhost:4551` will open up the ngrok web interface. From here the tunnel url is visible. \
Make sure to change `4551` if the port was changed during setup

If the node was setup on a remote machine replace `localhost` with the public  ip of the machine. \
Make sure to open ports `9053` and `4551` if firewall is enabled.

Once setup is complete, the docker container can be left alone. The node can be used as any other node.

The commands below must be run in their respective directories. For example, if I setup the Torrent File edition
I would first `cd ergo-synced-node && cd ergo-node-torrent`

To edit the `ergo.conf` file after everything is setup:
- `docker exec -ti <container name> /bin/bash`
  - container name is either 
    - `ergo-node-torrent_ergo-node`
    - `ergo-node-centralized_ergo-node`
- `apt-get update && apt-get install nano`
- `nano ergo.conf`
- edit as necessary
- `ctrl + o and ctrl + x` to save and exit 
-  `docker-compose down`
- `docker-compose up -d`

To reset the container:
- `docker-compose rm -y`
- This deletes the created containers which consequently deletes the blocks synced by your node and any initialized wallets!  
- This could be useful if one wanted to quickly reset their node wallet
- To create the container again : `docker-compose up -d`


## Support the project

If you have knowledge of seeding, please consider helping out by seeding the 10 GB compressed snapshot.
Just use the `ergo-4.0.23.7z.torrent` file to seed.



## Roadmap

- Guide to run without docker (just need time/patience to write)

- Docker container for starting nodes from scratch 

- Similar program for testnet nodes

- Volume support for the containers 

- Maybe some sort of frontend to create nodes so the user will just download an executable and have a nice node UI.

