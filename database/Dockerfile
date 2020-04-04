FROM mysql/mysql-server:5.7.17
  ENV MYSQL_ROOT_PASSWORD=changeme
  COPY setup.sql /docker-entrypoint-initdb.d/
