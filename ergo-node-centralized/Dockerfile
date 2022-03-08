FROM openjdk:11
RUN apt-get update && apt-get install p7zip-full -y
WORKDIR /node
COPY . .
RUN wget https://pixeldrain.com/api/file/2rXoYooy?download && mv 2rXoYooy?download ergo-4.0.23.7z && 7z x ergo-4.0.23.7z && rm ergo-4.0.23.7z