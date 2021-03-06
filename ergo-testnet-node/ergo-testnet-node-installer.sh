sudo apt-get update && sudo apt install p7zip-full -y
wget -O ergo.7z https://pixeldrain.com/api/file/LTPocg3n?download
7z x ergo.7z
rm ergo.7z
wget https://github.com/ergoplatform/ergo/releases/download/testnet-sync/ergo-testnet-sync.jar
sudo apt update
sudo apt install python3-pip -y
pip3 install -r python-conf/requirements.txt
cd python-conf
python3 main.py
cd ..
cp python-conf/ergo.conf ergo.conf
chmod +x updatePeerList.sh
# These commands install docker and docker-compose for Ubuntu
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt install docker-ce -y
sudo usermod -aG docker ${USER}
sudo apt  install docker-compose -y
docker-compose up -d
# End of docker section
echo The ergo testnet node has installed! Wait for syncing to finish.
echo The node is accessible via localhost:9052/panel
echo Check the status of the node by running: docker-compose logs -f
echo Remember to change the api key for additional security 
