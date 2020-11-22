docker run --name psql12-Flask -p 5432:5432 \
-v $PWD/psql/database:/var/lib/postgresql/data \
-e POSTGRES_PASSWORD=masterpython -d postgres:12.4
