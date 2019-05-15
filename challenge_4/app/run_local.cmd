docker stop k8manager
docker rm k8manager
docker volume rm k8manager_mongo_volume
docker rm k8_mongo

docker volume create --name k8manager_mongo_volume
docker run -d -p 27017:27017 -v k8manager_mongo_volume:/data/db --name k8manager_mongo mongo

docker build -t k8manager .
docker run --name k8manager -p 80:80 -e MONGO_CONN_STRING="mongodb:27017" -v c:/data:/secrets/ k8manager