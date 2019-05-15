docker rm minecraft_volume
docker volume create --name minecraft_volume
docker run -e EULA=TRUE -v minecraft_volume:/data -p 25565:25565 -p 25575:25575 openhack/minecraft-server