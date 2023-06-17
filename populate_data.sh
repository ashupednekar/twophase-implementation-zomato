docker exec -it order-svc python manage.py migrate
docker exec -it store-svc python manage.py migrate
docker exec -it delivery-svc python manage.py migrate
docker exec -it delivery-svc python manage.py populate_agents 20
docker exec -it store-svc python manage.py populate_food 10 50

