#!/bin/sh

set -e # exit if anything fails

which curl &> /dev/null || sudo DEBIAN_FRONTEND=noninteractive apt-get install -y curl # install curl if needed

# Check if Docker is not installed
if ! [ -x "$(command -v docker)" ]; then
    # Download Docker installation script
    curl -fsSL https://get.docker.com -o install-docker.sh 

    # Run the Docker installation script
    sudo sh install-docker.sh

    # install docker compose
    sudo DEBIAN_FRONTEND=noninteractive apt-get install docker-compose -y

    if ! [ -x "$(command -v docker)" ]; then
        echo docker not installed # exit if docker not installed
        exit 1
    fi
fi

ERGO_REF_CLIENT_VERSION="5.0.14"

curl -O https://storage.googleapis.com/ergo_bucket_archive/ergo-full-node-data.7z # download archived blockchain data

sudo DEBIAN_FRONTEND=noninteractive apt-get install p7zip-full -y # install 7-zip utility
7z x ergo-full-node-data.7z #extract directory
rm ergo-full-node-data.7z # delete archive

curl -LO https://github.com/ergoplatform/ergo/releases/download/v${ERGO_REF_CLIENT_VERSION}/ergo-${ERGO_REF_CLIENT_VERSION}.jar # download reference client jar

chmod +x updatePeerList.sh
sudo apt update
cd python-conf
docker compose up
cd ..
cp python-conf/ergo.conf ergo.conf
# spins up a temporary container to retrieve a list of known peers via api calls and outputs it in ergo.conf
# the more peer connections your node has the better it is for the network

docker compose up -d # start ergo node

echo The ergo node has installed! Wait for syncing to finish.
echo The node is accessible via http://localhost:9053/panel
echo Check the logs of the node by running: docker compose logs -f
echo Remember to change the api key for additional security
echo api key is set to "hello"
