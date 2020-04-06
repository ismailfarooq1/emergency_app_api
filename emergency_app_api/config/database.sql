-- Database: emergency_app_2

SELECT * FROM users

-- DATABASE

----03/04/2020

-- SCHEMA 
---- 03/04/2020
CREATE TABLE IF NOT EXISTS users(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL,
	gender VARCHAR(10) NOT NULL,
	dob DATE NOT NULL,
	phone_number VARCHAR(15) NOT NULL,
	created DATE DEFAULT CURRENT_DATE,
	MODIFIED DATE
);
CREATE TABLE IF NOT EXISTS contacts(
	id SERIAL PRIMARY KEY,
	user_id INT NOT NULL REFERENCES users(id),
	email VARCHAR(100) NOT NULL,
	phone_number VARCHAR(15) NOT NULL,
	email_verfied BOOLEAN NOT NULL DEFAULT false,
	phone_verfied BOOLEAN NOT NULL DEFAULT false,
	created DATE DEFAULT CURRENT_DATE,
	modified DATE
);

-- DROP DATABASE emergency_app_2;

CREATE DATABASE emergency_app_2
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;