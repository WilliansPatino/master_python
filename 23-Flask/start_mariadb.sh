docker run --name mariadb-Flask -p 3306:3306 \
-v $PWD/mariadb/database:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=masterpython \
-v $PWD/mariadb/config:/etc/mysql/ \
-d mariadb:10.5.8-focal
