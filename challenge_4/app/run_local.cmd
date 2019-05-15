docker stop k8manager
docker rm k8manager
docker build -t k8manager .
docker run --name k8manager -p 80:80 -e MONGO_CONN_STRING="mongodb:27017" k8manager