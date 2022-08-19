sudo apt update
sudo apt install python3-pip -y
pip3 install -r python-conf/requirements.txt
cd python-conf
python3 main.py
cd ..
cp python-conf/ergo.conf ergo.conf
