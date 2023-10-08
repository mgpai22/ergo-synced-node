#!/bin/bash
cd python-conf
docker compose up ergo-node-ip-tool
cd ..
cp python-conf/ergo.conf ergo.conf
docker compose down
echo node shutdown to load changes
docker compose up -d
echo The node is back up! Changes are loaded.
