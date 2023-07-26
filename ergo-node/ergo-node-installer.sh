#!/bin/sh

set -e # exit if anything fails

if ! command -v curl &> /dev/null # check if curl is installed
then
    echo "curl not installed"
    exit
fi

curl -fsSL https://raw.githubusercontent.com/mgpai22/docker-install-script/main/docker-install-ubuntu.sh | bash
./docker-install-ubuntu.sh # installs docker only if system doesn't have it
rm docker-install-ubuntu.sh

if ! command -v docker &> /dev/null # check if docker installed
then
    echo "Docker could not be installed"
    exit
fi

ERGO_REF_CLIENT_VERSION="v5.0.12"

curl -O https://storage.googleapis.com/ergo_bucket_archive/ergo-full-node-data.7z # download archived blockchain data

sudo apt-get install p7zip-full -y # install 7-zip utility
7z x ergo-full-node-data.7z #extract directory

curl -O https://github.com/ergoplatform/ergo/releases/download/${ERGO_REF_CLIENT_VERSION}/ergo-${ERGO_REF_CLIENT_VERSION}.jar # download reference client jar

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
