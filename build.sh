docker build -t order order -f order/Dockerfile
docker build -t store store -f order/Dockerfile
docker build -t delivery delivery -f order/Dockerfile
docker-compose down
docker-compose up -d
docker-compose logs -f