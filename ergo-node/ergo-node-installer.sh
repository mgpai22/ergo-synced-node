wget https://raw.githubusercontent.com/mgpai22/docker-install-script/main/docker-install-ubuntu.sh
chmod +x docker-install-ubuntu.sh
./docker-install-ubuntu.sh # installs docker only if system doesn't have it
rm docker-install-ubuntu.sh
cd blockchain_download
docker-compose up # temporary container to download blockchain with arweave cli
cd ..
cat .ergo/blockchain_parts/ergo-mainnet-blockchain.tar.gz.parta* >blockchain.tar.gz
rm -rf .ergo
tar -xvf blockchain.tar.gz
rm blockchain.tar.gz
wget https://github.com/ergoplatform/ergo/releases/download/v4.0.46/ergo-4.0.46.jar
chmod +x updatePeerList.sh
sudo apt update
cd python-conf
docker-compose up 
cd ..
cp python-conf/ergo.conf ergo.conf
# spins up a temporary container to retrive a list of known peers via api calls and outputs it in ergo.conf
docker-compose up -d
echo The ergo node has installed! Wait for syncing to finish.
echo The node is accessible via localhost:9053/panel
echo Check the status of the node by running: docker-compose logs -f
echo Remember to change the api key for additional security 
