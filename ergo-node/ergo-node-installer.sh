#!/bin/bash
sudo apt-get update && sudo apt install p7zip-full -y
wget -O ergo.7z https://pixeldrain.com/api/file/2rXoYooy?download
7z x ergo.7z
rm ergo.7z
wget https://github.com/ergoplatform/ergo/releases/download/v4.0.23/ergo-4.0.23.jar
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
echo The ergo node has installed! Wait for syncing to finish.
echo The node is accessible via localhost:9053/panel
echo Check the status of the node by running: docker-compose logs -f
echo Remember to change the api key for additional security 