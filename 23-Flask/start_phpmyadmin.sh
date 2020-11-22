docker run --name phpmyadmin-Flask  \
-p 8080:80 \
-e MYSQL_ROOT_PASSWORD=masterpython \
-v $PWD/phpmyadmin/config.user.inc.php:/etc/phpmyadmin/config.user.inc.php \
-d phpmyadmin:5.0.4-apache
