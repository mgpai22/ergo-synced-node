sudo apt update
cd python-conf
docker-compose up 
cd ..
cp python-conf/ergo.conf ergo.conf
docker-compose down
echo node shutdown to load changes
docker-compose up --build -d
echo The node is back up! Changes are loaded.
