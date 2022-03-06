FROM openjdk:11
RUN apt-get update && apt-get install aria2 -y && apt-get install p7zip-full -y
WORKDIR /node
COPY . .
RUN aria2c --seed-time=0 ergo-4.0.23.7z.torrent && 7z x ergo-4.0.23.7z && rm ergo-4.0.23.7z