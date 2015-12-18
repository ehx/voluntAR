# voluntAR

https://equalitycoop.slack.com - channel voluntAR
https://waffle.io/ehx/voluntAR

Instalar PostgreSQL:
sudo apt-get install libpq-dev python-dev
sudo apt-get install postgresql postgresql-contrib

Configurar Postrge:
sudo su - postgres
createdb voluntAR
createuser -P
psql
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
