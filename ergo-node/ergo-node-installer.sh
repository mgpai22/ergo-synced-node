#!/bin/sh

set -e # exit if anything fails

which curl &> /dev/null || sudo apt install curl # install curl if needed

curl -fsSL https://raw.githubusercontent.com/mgpai22/docker-install-script/main/docker-install-ubuntu.sh | bash # installs docker if it isn't already there

if ! [ -x "$(command -v docker)" ]; then
    echo docker not installed # exit if docker not installed
    exit 1
fi

ERGO_REF_CLIENT_VERSION="v5.0.12"

curl -O https://storage.googleapis.com/ergo_bucket_archive/ergo-full-node-data.7z # download archived blockchain data

sudo apt-get install p7zip-full -y # install 7-zip utility
7z x ergo-full-node-data.7z #extract directory
rm ergo-full-node-data.7z # delete archive

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
