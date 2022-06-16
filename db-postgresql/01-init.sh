#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
  CREATE DATABASE $APP_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
  \connect $APP_DB_NAME $APP_DB_USER
  BEGIN;
    CREATE TABLE IF NOT EXISTS furniture(
	  id CHAR(26) NOT NULL CHECK (CHAR_LENGTH(id) = 26) PRIMARY KEY,
	  id_block INT,
      id_type_furniture INT,
	  number_furniture INT,
	  date DATE
	);
  COMMIT;
EOSQL